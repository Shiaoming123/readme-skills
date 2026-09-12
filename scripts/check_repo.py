#!/usr/bin/env python3
"""Validate the Skill package, bilingual README, and fixed showcase artifacts."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
import re
import struct
import sys
import xml.etree.ElementTree as ET


ROOT = Path(__file__).resolve().parents[1]
SHA_RE = re.compile(r"^[0-9a-f]{40}$")
SEMVER_RE = re.compile(r"^\d+\.\d+\.\d+(?:[-+][0-9A-Za-z.-]+)?$")
LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
NAMED_LINK_RE = re.compile(r"(?<!!)\[([^\]]+)\]\(([^)]+)\)")
HEADING_RE = re.compile(r"^#{1,6}\s+(.+?)\s*#*\s*$", re.MULTILINE)


def fail(message: str) -> None:
    raise AssertionError(message)


def require_file(relative: str) -> Path:
    path = ROOT / relative
    if not path.is_file():
        fail(f"missing file: {relative}")
    return path


def png_size(path: Path) -> tuple[int, int]:
    header = path.read_bytes()[:24]
    if len(header) != 24 or header[:8] != b"\x89PNG\r\n\x1a\n":
        fail(f"invalid PNG: {path.relative_to(ROOT)}")
    return struct.unpack(">II", header[16:24])


def check_local_links(path: Path) -> int:
    text = path.read_text(encoding="utf-8")
    checked = 0
    for raw in LINK_RE.findall(text):
        target = raw.strip().strip("<>").split("#", 1)[0]
        if not target or re.match(r"^[a-z][a-z0-9+.-]*:", target, re.I):
            continue
        resolved = (path.parent / target).resolve()
        if not resolved.exists():
            fail(f"broken local link in {path.relative_to(ROOT)}: {raw}")
        checked += 1
    return checked


def heading_anchor(heading: str) -> str:
    plain = re.sub(r"<[^>]+>|[`*_~]", "", heading).strip().lower()
    return re.sub(r"[^\w\- ]", "", plain).replace(" ", "-")


def check_preserved_navigation(before_text: str, after_text: str, case_id: str) -> None:
    source_links = [
        (label.strip(), target.strip())
        for label, target in NAMED_LINK_RE.findall(before_text)
        if target.strip().startswith("#")
    ]
    if not source_links:
        return
    after_links: dict[str, list[str]] = {}
    for label, target in NAMED_LINK_RE.findall(after_text):
        after_links.setdefault(label.strip(), []).append(target.strip())
    after_anchors = {heading_anchor(heading) for heading in HEADING_RE.findall(after_text)}
    for label, _ in source_links:
        targets = after_links.get(label, [])
        if not any(target.startswith("#") and target[1:] in after_anchors for target in targets):
            fail(f"source navigation label is no longer a working jump link in {case_id}: {label}")


def main() -> int:
    required = [
        "SKILL.md",
        "agents/openai.yaml",
        "references/workflow-and-structure.md",
        "references/repository-profiles.md",
        "references/evidence-and-validation.md",
        "references/presentation-and-governance.md",
        "README.md",
        "README.zh-CN.md",
        "LICENSE",
        "VERSION",
        "PROVENANCE.md",
        "examples/README.md",
        "examples/cases.json",
        "assets/workflow.svg",
    ]
    for relative in required:
        require_file(relative)

    skill_text = require_file("SKILL.md").read_text(encoding="utf-8")
    if not skill_text.startswith("---\nname: readme-skills\n"):
        fail("SKILL.md name does not match the repository")
    if "[TODO" in skill_text or "TODO:" in skill_text:
        fail("SKILL.md still contains a TODO placeholder")

    version = require_file("VERSION").read_text(encoding="utf-8").strip()
    if not SEMVER_RE.fullmatch(version):
        fail(f"VERSION is not semantic: {version!r}")
    license_text = require_file("LICENSE").read_text(encoding="utf-8")
    if not license_text.startswith("MIT License\n") or "Copyright (c) 2026 Shiaoming123" not in license_text:
        fail("LICENSE is not the approved MIT license for Shiaoming123")

    data = json.loads(require_file("examples/cases.json").read_text(encoding="utf-8"))
    cases = data.get("cases", [])
    if len(cases) < 8:
        fail(f"expected at least 8 showcase cases, found {len(cases)}")
    categories = {case["category"] for case in cases}
    if len(categories) != len(cases):
        fail("showcase categories must be unique")

    root_readmes = [require_file("README.md"), require_file("README.zh-CN.md")]
    root_text = "\n".join(path.read_text(encoding="utf-8") for path in root_readmes)
    if f"v{version}" not in root_text or "(LICENSE)" not in root_text:
        fail("root READMEs do not expose the current version and license")
    for readme in root_readmes:
        text = readme.read_text(encoding="utf-8")
        if "img.shields.io/badge/version" not in text or "img.shields.io/badge/license" not in text:
            fail(f"default version/license badges are missing from {readme.name}")
        if "img.shields.io/badge/README-English" not in text or "README-%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87" not in text:
            fail(f"language navigation badges are missing from {readme.name}")
        if '<td width="50%"' in text:
            fail(f"showcase comparisons are still constrained to half width in {readme.name}")
    for case in cases:
        if case.get("mode") != "optimize":
            fail(f"showcase case is not preservation-first optimize mode: {case.get('id')}")
        if not SHA_RE.fullmatch(case.get("sha", "")):
            fail(f"invalid fixed SHA for {case.get('id')}")
        if not case.get("source_readme", "").startswith("https://github.com/"):
            fail(f"non-GitHub source README for {case['id']}")
        if not case.get("license_url", "").startswith("https://github.com/"):
            fail(f"missing source license URL for {case['id']}")
        before_readme = require_file(case["before_readme"])
        if hashlib.sha256(before_readme.read_bytes()).hexdigest() != case.get("source_sha256"):
            fail(f"fixed source README changed: {case['id']}")
        after_readme = require_file(case["after_readme"])
        after_text = after_readme.read_text(encoding="utf-8")
        check_preserved_navigation(before_readme.read_text(encoding="utf-8"), after_text, case["id"])
        for target in case.get("preserved_links", []):
            if target not in after_text:
                fail(f"preserved source link missing from {case['id']}: {target}")
        if len(after_text) <= len(before_readme.read_text(encoding="utf-8")):
            fail(f"optimized README does not retain and extend source content: {case['id']}")
        before = require_file(case["before_image"])
        after = require_file(case["after_image"])
        comparison = require_file(case["comparison_image"])
        before_size = png_size(before)
        after_size = png_size(after)
        comparison_size = png_size(comparison)
        if before_size[0] != 1440 or not 160 <= before_size[1] <= 3600:
            fail(f"unexpected content-sized before image for {case['id']}: {before_size}")
        if after_size[0] != 1440 or not 160 <= after_size[1] <= 3600:
            fail(f"unexpected content-sized after image for {case['id']}: {after_size}")
        if comparison_size[0] != 1440 or not 160 <= comparison_size[1] <= 7600:
            fail(f"unexpected comparison image size for {case['id']}: {comparison_size}")
        if comparison_size[1] >= 7600 and before_size[1] + after_size[1] < 7300:
            fail(f"comparison image appears padded instead of content-sized: {case['id']}")
        if case["comparison_image"] not in root_text:
            fail(f"comparison image is not linked from a root README: {case['id']}")

    ET.parse(require_file("assets/workflow.svg"))
    markdown = root_readmes + [require_file("examples/README.md")]
    markdown.extend(require_file(case["after_readme"]) for case in cases)
    link_count = sum(check_local_links(path) for path in markdown)
    print(f"OK: v{version}, MIT, {len(cases)} cases, {len(categories)} categories, {link_count} local links, source/after/comparison images and SVG valid")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (AssertionError, KeyError, json.JSONDecodeError, ET.ParseError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        raise SystemExit(1)
