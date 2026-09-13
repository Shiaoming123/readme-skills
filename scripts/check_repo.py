#!/usr/bin/env python3
"""Validate the Skill package, bilingual README, and fixed showcase artifacts."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import re
import struct
import sys
import xml.etree.ElementTree as ET


ROOT = Path(__file__).resolve().parents[1]
CAPTURE_WIDTH = 1440
COMPARISON_WIDTH = CAPTURE_WIDTH * 2 + 76
SHA_RE = re.compile(r"^[0-9a-f]{40}$")
SEMVER_RE = re.compile(r"^\d+\.\d+\.\d+(?:[-+][0-9A-Za-z.-]+)?$")
LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
NAMED_LINK_RE = re.compile(r"(?<!!)\[([^\]]+)\]\(([^)]+)\)")
HEADING_RE = re.compile(r"^#{1,6}\s+(.+?)\s*#*\s*$", re.MULTILINE)
EVALUATION_MODES = {"audit-only", "generate", "restructure", "release-sync"}


def fail(message: str) -> None:
    raise AssertionError(message)


def require_file(relative: str) -> Path:
    path = ROOT / relative
    if not path.is_file():
        fail(f"missing file: {relative}")
    return path


def require_directory(relative: str) -> Path:
    path = ROOT / relative
    if not path.is_dir():
        fail(f"missing directory: {relative}")
    return path


def safe_relative(value: str, context: str) -> Path:
    path = Path(value)
    if path.is_absolute() or ".." in path.parts:
        fail(f"unsafe relative path in {context}: {value}")
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


def check_contract_text(text: str, contract: dict, label: str) -> None:
    for needle in contract.get("contains", []):
        if needle not in text:
            fail(f"expected output missing required text for {label}: {needle}")
    for choices in contract.get("contains_any", []):
        if not isinstance(choices, list) or not choices or any(
            not isinstance(choice, str) or not choice for choice in choices
        ):
            fail(f"invalid contains_any contract for {label}")
        if not any(choice in text for choice in choices):
            fail(f"expected output is missing every allowed alternative for {label}: {choices}")
    for forbidden in contract.get("excludes", []):
        if forbidden in text:
            fail(f"expected output retains forbidden text for {label}: {forbidden}")


def check_evaluation_contracts() -> int:
    data = json.loads(require_file("evals/cases.json").read_text(encoding="utf-8"))
    if data.get("schema_version") != 1:
        fail("unsupported evals/cases.json schema")
    cases = data.get("cases")
    if not isinstance(cases, list) or not cases:
        fail("evals/cases.json has no cases")

    seen_ids: set[str] = set()
    seen_modes: set[str] = set()
    for case in cases:
        case_id = case.get("id")
        mode = case.get("mode")
        if not isinstance(case_id, str) or not case_id or case_id in seen_ids:
            fail(f"invalid or duplicate evaluation case id: {case_id!r}")
        if mode not in EVALUATION_MODES:
            fail(f"unsupported evaluation mode for {case_id}: {mode!r}")
        seen_ids.add(case_id)
        seen_modes.add(mode)

        input_dir = require_directory(str(safe_relative(case.get("input", ""), case_id)))
        expected_dir = require_directory(str(safe_relative(case.get("expected", ""), case_id)))
        request_path = require_file(str(safe_relative(case.get("request", ""), case_id)))
        if not request_path.read_text(encoding="utf-8").strip():
            fail(f"evaluation request is empty: {case_id}")
        allowed_changes = case.get("allowed_changes")
        if not isinstance(allowed_changes, list) or any(
            not isinstance(path, str) or not path for path in allowed_changes
        ):
            fail(f"evaluation case has invalid allowed changes: {case_id}")
        for source in case.get("required_input_files", []):
            source_path = input_dir / safe_relative(source, case_id)
            if not source_path.is_file():
                fail(f"missing fixture input for {case_id}: {source}")
        for missing in case.get("missing_input_files", []):
            if (input_dir / safe_relative(missing, case_id)).exists():
                fail(f"fixture input unexpectedly contains {missing}: {case_id}")

        outputs = case.get("outputs")
        if not isinstance(outputs, dict) or not outputs:
            fail(f"evaluation case has no output contract: {case_id}")
        output_texts: dict[str, str] = {}
        for output, contract in outputs.items():
            if not isinstance(contract, dict):
                fail(f"evaluation output contract must be an object: {case_id}/{output}")
            output_path = expected_dir / safe_relative(output, case_id)
            if not output_path.is_file():
                fail(f"missing expected output for {case_id}: {output}")
            text = output_path.read_text(encoding="utf-8")
            output_texts[output] = text
            check_contract_text(text, contract, f"{case_id}/{output}")

        localized = case.get("localized_outputs", [])
        if localized:
            if len(localized) < 2:
                fail(f"localized output contract needs at least two files: {case_id}")
            for output in localized:
                if output not in output_texts:
                    fail(f"localized output is not a declared output for {case_id}: {output}")
            for token in case.get("synchronized_tokens", []):
                if any(token not in output_texts[output] for output in localized):
                    fail(f"localized output is out of sync for {case_id}: {token}")

        if mode == "audit-only" and (
            case.get("source_files_modified") is not False or allowed_changes
        ):
            fail(f"audit fixture must explicitly preserve source files: {case_id}")

    if seen_modes != EVALUATION_MODES:
        missing_modes = ", ".join(sorted(EVALUATION_MODES - seen_modes))
        fail(f"evaluation modes are incomplete: {missing_modes}")
    return len(cases)


def file_hashes(directory: Path) -> dict[str, str]:
    return {
        path.relative_to(directory).as_posix(): hashlib.sha256(path.read_bytes()).hexdigest()
        for path in directory.rglob("*")
        if path.is_file()
    }


def evaluate_workspace(case_id: str, workspace: Path) -> int:
    data = json.loads(require_file("evals/cases.json").read_text(encoding="utf-8"))
    cases = data.get("cases", [])
    case = next((item for item in cases if item.get("id") == case_id), None)
    if not case:
        fail(f"unknown evaluation case: {case_id}")
    if not workspace.is_dir():
        fail(f"evaluation workspace is not a directory: {workspace}")

    source_dir = require_directory(str(safe_relative(case["input"], case_id)))
    source_hashes = file_hashes(source_dir)
    workspace_hashes = file_hashes(workspace)
    changed = sorted(
        path
        for path in set(source_hashes) | set(workspace_hashes)
        if source_hashes.get(path) != workspace_hashes.get(path)
    )
    allowed_changes = {str(safe_relative(path, case_id)).replace("\\", "/") for path in case["allowed_changes"]}
    unexpected = [path for path in changed if path not in allowed_changes]
    if unexpected:
        fail(f"evaluation workspace changed files outside the contract for {case_id}: {', '.join(unexpected)}")

    if case["mode"] != "audit-only":
        for output, contract in case["outputs"].items():
            output_path = workspace / safe_relative(output, case_id)
            if not output_path.is_file():
                fail(f"evaluation workspace is missing required output for {case_id}: {output}")
            check_contract_text(output_path.read_text(encoding="utf-8"), contract, f"{case_id}/{output}")
        for token in case.get("synchronized_tokens", []):
            localized = case.get("localized_outputs", [])
            if any(token not in (workspace / output).read_text(encoding="utf-8") for output in localized):
                fail(f"evaluation workspace has unsynchronized locale output for {case_id}: {token}")

    print(
        f"OK: evaluation {case_id}, mode={case['mode']}, "
        f"allowed changes={len(allowed_changes)}, observed changes={len(changed)}"
    )
    return 0


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
        "COMPATIBILITY.md",
        "LICENSE",
        "VERSION",
        "PROVENANCE.md",
        "examples/README.md",
        "examples/cases.json",
        "assets/workflow.svg",
        "assets/readme-skills-hero.png",
    ]
    for relative in required:
        require_file(relative)

    evaluation_cases = check_evaluation_contracts()

    skill_text = require_file("SKILL.md").read_text(encoding="utf-8")
    if not skill_text.startswith("---\nname: readme-skills\n"):
        fail("SKILL.md name does not match the repository")
    if "\nlicense: MIT\n" not in skill_text:
        fail("SKILL.md is missing portable license metadata")
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
        if "img.shields.io/badge/Agent_Skills-compatible" not in text or "(COMPATIBILITY.md)" not in text:
            fail(f"Agent Skills compatibility link is missing from {readme.name}")
        if "assets/readme-skills-hero.png" not in text:
            fail(f"generated hero is missing from {readme.name}")
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
        if before_size[0] != CAPTURE_WIDTH or not 160 <= before_size[1] <= 3600:
            fail(f"unexpected content-sized before image for {case['id']}: {before_size}")
        if after_size[0] != CAPTURE_WIDTH or not 160 <= after_size[1] <= 3600:
            fail(f"unexpected content-sized after image for {case['id']}: {after_size}")
        if comparison_size[0] != COMPARISON_WIDTH or not 380 <= comparison_size[1] <= 3900:
            fail(f"comparison is not a full-width horizontal layout for {case['id']}: {comparison_size}")
        expected_height = max(before_size[1], after_size[1]) + 236
        if not expected_height - 4 <= comparison_size[1] <= expected_height + 4:
            fail(f"comparison image is stacked or padded instead of content-height: {case['id']}")
        if case["comparison_image"] not in root_text:
            fail(f"comparison image is not linked from a root README: {case['id']}")
        for readme in root_readmes:
            text = readme.read_text(encoding="utf-8")
            image_link = f'<a href="{case["comparison_image"]}"><img src="{case["comparison_image"]}"'
            if image_link not in text:
                fail(f"comparison preview does not open the full-size image in {readme.name}: {case['id']}")

    ET.parse(require_file("assets/workflow.svg"))
    hero = require_file("assets/readme-skills-hero.png")
    if png_size(hero) != (2172, 724) or hero.stat().st_size > 2_000_000:
        fail(f"unexpected hero asset dimensions or size: {png_size(hero)}, {hero.stat().st_size} bytes")
    compatibility = require_file("COMPATIBILITY.md").read_text(encoding="utf-8")
    for client in ("Codex", "Claude Code", "GitHub Copilot", "Gemini CLI", "Cursor", "OpenCode"):
        if client not in compatibility:
            fail(f"compatibility guide is missing {client}")
    markdown = root_readmes + [require_file("examples/README.md")]
    markdown.extend(require_file(case["after_readme"]) for case in cases)
    link_count = sum(check_local_links(path) for path in markdown)
    print(
        f"OK: v{version}, MIT, {len(cases)} showcase cases, {evaluation_cases} evaluation contracts, "
        f"{len(categories)} categories, {link_count} local links, source/after/comparison images and SVG valid"
    )
    return 0


def cli() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--evaluate", metavar="CASE", help="check an Agent-produced disposable workspace")
    parser.add_argument("--workspace", type=Path, help="workspace produced from the selected fixture input")
    args = parser.parse_args()
    if args.evaluate:
        if not args.workspace:
            parser.error("--workspace is required with --evaluate")
        return evaluate_workspace(args.evaluate, args.workspace)
    if args.workspace:
        parser.error("--workspace requires --evaluate")
    return main()


if __name__ == "__main__":
    try:
        raise SystemExit(cli())
    except (AssertionError, KeyError, json.JSONDecodeError, ET.ParseError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        raise SystemExit(1)
