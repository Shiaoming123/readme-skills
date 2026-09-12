#!/usr/bin/env python3
"""Capture original and rewritten README pages, then compose screenshot comparisons."""

from __future__ import annotations

import argparse
import html
import json
import os
from pathlib import Path
import subprocess
import time
import urllib.error
import urllib.request


ROOT = Path(__file__).resolve().parents[1]
CASES_FILE = ROOT / "examples" / "cases.json"
WORK = ROOT / ".work" / "showcase-render"
EDGE_CANDIDATES = (
    Path(r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"),
    Path(r"C:\Program Files\Microsoft\Edge\Application\msedge.exe"),
)


def find_edge() -> Path:
    for candidate in EDGE_CANDIDATES:
        if candidate.is_file():
            return candidate
    raise FileNotFoundError("Microsoft Edge was not found in the supported Windows locations")


def load_cases() -> list[dict]:
    data = json.loads(CASES_FILE.read_text(encoding="utf-8"))
    cases = data.get("cases", [])
    if not cases:
        raise ValueError("examples/cases.json has no cases")
    return cases


def ensure_png(path: Path) -> None:
    if not path.is_file() or path.stat().st_size < 1000:
        raise RuntimeError(f"Browser did not create a usable screenshot: {path}")
    if path.read_bytes()[:8] != b"\x89PNG\r\n\x1a\n":
        raise RuntimeError(f"Screenshot is not a PNG: {path}")


def screenshot(edge: Path, url: str, output: Path, profile: Path, size: str) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    profile.mkdir(parents=True, exist_ok=True)
    command = [
        str(edge),
        "--headless=new",
        "--disable-gpu",
        "--hide-scrollbars",
        "--no-first-run",
        "--force-device-scale-factor=1",
        f"--user-data-dir={profile}",
        f"--window-size={size}",
        f"--screenshot={output}",
        url,
    ]
    completed = subprocess.run(command, check=False, timeout=60)
    if completed.returncode not in (0,):
        raise RuntimeError(f"Edge exited with {completed.returncode} while capturing {url}")
    for _ in range(30):
        if output.is_file():
            break
        time.sleep(0.2)
    ensure_png(output)


def github_markdown(case: dict) -> str:
    markdown = (ROOT / case["after_readme"]).read_text(encoding="utf-8")
    body = json.dumps(
        {"text": markdown, "mode": "gfm", "context": case["repository"]}
    ).encode("utf-8")
    headers = {
        "Accept": "application/vnd.github+json",
        "Content-Type": "application/json",
        "User-Agent": "readme-skills-showcase-renderer/0.1",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    token = os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"
    request = urllib.request.Request(
        "https://api.github.com/markdown", data=body, headers=headers, method="POST"
    )
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            return response.read().decode("utf-8")
    except urllib.error.HTTPError as error:
        details = error.read().decode("utf-8", errors="replace")[:500]
        raise RuntimeError(f"GitHub Markdown API returned {error.code}: {details}") from error
    except urllib.error.URLError as error:
        raise RuntimeError(f"GitHub Markdown API request failed: {error.reason}") from error


def render_after_html(case: dict, rendered_markdown: str) -> str:
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(case['repository'])} README Skills preview</title>
<style>
* {{ box-sizing: border-box; }}
html, body {{ width: 1440px; min-height: 1200px; margin: 0; }}
body {{ background: #f6f8fa; color: #1f2328; font: 16px/1.5 -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; }}
.topbar {{ height: 64px; background: #24292f; color: #fff; display: flex; align-items: center; padding: 0 42px; font-weight: 650; }}
.topbar span {{ color: #8c959f; margin: 0 8px; }}
.repohead {{ height: 92px; padding: 22px 72px; background: #fff; border-bottom: 1px solid #d0d7de; }}
.repo {{ color: #0969da; font-size: 21px; font-weight: 600; }}
.notice {{ margin-top: 6px; color: #57606a; font-size: 13px; }}
.shell {{ width: 1120px; margin: 28px auto 80px; background: #fff; border: 1px solid #d0d7de; border-radius: 8px; overflow: hidden; }}
.filebar {{ height: 48px; display: flex; align-items: center; padding: 0 20px; border-bottom: 1px solid #d8dee4; background: #f6f8fa; color: #57606a; font-size: 14px; font-weight: 600; }}
.markdown-body {{ padding: 34px 40px 60px; overflow-wrap: break-word; }}
.markdown-body h1, .markdown-body h2, .markdown-body h3 {{ margin-top: 24px; margin-bottom: 16px; font-weight: 600; line-height: 1.25; }}
.markdown-body h1 {{ padding-bottom: .3em; border-bottom: 1px solid #d8dee4; font-size: 2em; }}
.markdown-body h2 {{ padding-bottom: .3em; border-bottom: 1px solid #d8dee4; font-size: 1.5em; }}
.markdown-body h3 {{ font-size: 1.25em; }}
.markdown-body p, .markdown-body blockquote, .markdown-body ul, .markdown-body ol, .markdown-body table, .markdown-body pre {{ margin-top: 0; margin-bottom: 16px; }}
.markdown-body a {{ color: #0969da; text-decoration: none; }}
.markdown-body blockquote {{ padding: 0 1em; color: #57606a; border-left: .25em solid #d0d7de; }}
.markdown-body code {{ padding: .2em .4em; border-radius: 6px; background: #afb8c133; font: 85% ui-monospace, SFMono-Regular, Consolas, monospace; }}
.markdown-body pre {{ padding: 16px; overflow: auto; border-radius: 6px; background: #f6f8fa; }}
.markdown-body pre code {{ padding: 0; background: transparent; font-size: 100%; }}
.markdown-body table {{ border-spacing: 0; border-collapse: collapse; width: max-content; max-width: 100%; }}
.markdown-body th, .markdown-body td {{ padding: 6px 13px; border: 1px solid #d0d7de; }}
.markdown-body tr:nth-child(2n) {{ background: #f6f8fa; }}
</style>
</head>
<body>
<header class="topbar">README Skills <span>/</span> rendered output</header>
<section class="repohead">
  <div class="repo">{html.escape(case['repository'])}</div>
  <div class="notice">Preview generated from {html.escape(case['after_readme'])}; not submitted upstream.</div>
</section>
<main class="shell">
  <div class="filebar">README.md · GitHub-rendered demonstration rewrite</div>
  <article class="markdown-body">{rendered_markdown}</article>
</main>
</body>
</html>"""


def render_comparison_html(case: dict) -> str:
    accent = html.escape(case["accent"])
    before_uri = (ROOT / case["before_image"]).resolve().as_uri()
    after_uri = (ROOT / case["after_image"]).resolve().as_uri()
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(case['category'])} README comparison</title>
<style>
* {{ box-sizing: border-box; }}
html, body {{ width: 1440px; height: 5120px; margin: 0; overflow: hidden; }}
body {{ background: #07101f; color: #e5edf8; font-family: Inter, "Segoe UI", Arial, sans-serif; }}
.page {{ width: 1440px; height: 5120px; padding: 28px; background: radial-gradient(circle at 90% 0%, {accent}22, transparent 16%), linear-gradient(145deg, #07101f, #0f172a); }}
.top {{ height: 76px; display: flex; align-items: flex-start; justify-content: space-between; }}
.kicker {{ color: {accent}; font-size: 14px; font-weight: 800; letter-spacing: .14em; }}
.repo {{ margin-top: 10px; font-size: 27px; font-weight: 750; color: #f8fafc; }}
.sha {{ color: #94a3b8; font: 14px ui-monospace, SFMono-Regular, Consolas, monospace; padding-top: 8px; }}
.stack {{ display: grid; grid-template-rows: 2448px 2448px; gap: 20px; }}
.panel {{ overflow: hidden; border: 1px solid #26364f; border-radius: 20px; background: #0b1424; box-shadow: 0 16px 42px #02061788; }}
.panel-head {{ height: 48px; display: flex; align-items: center; justify-content: space-between; padding: 0 18px; background: #0b1424; border-bottom: 1px solid #26364f; }}
.label {{ color: #f8fafc; font-size: 13px; font-weight: 800; letter-spacing: .08em; }}
.label span {{ color: {accent}; }}
.source {{ color: #94a3b8; font: 12px ui-monospace, SFMono-Regular, Consolas, monospace; }}
.shot {{ height: 2400px; overflow: hidden; background: #f6f8fa; }}
.shot img {{ display: block; width: 100%; height: 100%; object-fit: cover; object-position: top center; }}
.footer {{ height: 54px; display: flex; align-items: flex-end; justify-content: space-between; color: #64748b; font-size: 13px; }}
.footer strong {{ color: #94a3b8; }}
</style>
</head>
<body>
<main class="page">
  <header class="top">
    <div><div class="kicker">README SKILLS · BEFORE / AFTER</div><div class="repo">{html.escape(case['repository'])}</div></div>
    <div class="sha">fixed {html.escape(case['sha'][:12])}</div>
  </header>
  <section class="stack">
    <article class="panel">
      <div class="panel-head"><div class="label"><span>BEFORE</span> · original repository README</div><div class="source">fixed commit screenshot</div></div>
      <div class="shot"><img src="{before_uri}" alt=""></div>
    </article>
    <article class="panel">
      <div class="panel-head"><div class="label"><span>AFTER</span> · README Skills output</div><div class="source">GitHub-rendered after.md screenshot</div></div>
      <div class="shot"><img src="{after_uri}" alt=""></div>
    </article>
  </section>
  <footer class="footer"><span>Both panels are screenshots; the after panel comes from {html.escape(case['after_readme'])}.</span><strong>readme-skills</strong></footer>
</main>
</body>
</html>"""


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--capture", action="store_true", help="capture fixed GitHub README pages")
    parser.add_argument("--render", action="store_true", help="render rewritten READMEs and comparison images")
    parser.add_argument("--force", action="store_true", help="replace existing outputs")
    parser.add_argument("--case", action="append", dest="case_ids", help="process one case id; repeat as needed")
    args = parser.parse_args()
    capture = args.capture or not (args.capture or args.render)
    render = args.render or not (args.capture or args.render)

    edge = find_edge()
    cases = load_cases()
    if args.case_ids:
        requested = set(args.case_ids)
        cases = [case for case in cases if case["id"] in requested]
        missing = requested - {case["id"] for case in cases}
        if missing:
            raise ValueError(f"unknown case id(s): {', '.join(sorted(missing))}")
    WORK.mkdir(parents=True, exist_ok=True)

    for case in cases:
        before = ROOT / case["before_image"]
        if capture and (args.force or not before.exists()):
            profile = WORK / "profiles" / f"{case['id']}-source-{time.time_ns()}"
            screenshot(edge, case["source_readme"], before, profile, "1440,2400")
            print(f"captured {before.relative_to(ROOT)}")
        if render:
            ensure_png(before)
            after = ROOT / case["after_image"]
            if args.force or not after.exists():
                page = WORK / "pages" / f"{case['id']}-after.html"
                page.parent.mkdir(parents=True, exist_ok=True)
                page.write_text(
                    render_after_html(case, github_markdown(case)), encoding="utf-8"
                )
                profile = WORK / "profiles" / f"{case['id']}-after-{time.time_ns()}"
                screenshot(edge, page.resolve().as_uri(), after, profile, "1440,2400")
                print(f"rendered {after.relative_to(ROOT)}")
            ensure_png(after)
            page = WORK / "pages" / f"{case['id']}-comparison.html"
            page.parent.mkdir(parents=True, exist_ok=True)
            page.write_text(render_comparison_html(case), encoding="utf-8")
            output = ROOT / case["comparison_image"]
            if args.force or not output.exists():
                profile = WORK / "profiles" / f"{case['id']}-card-{time.time_ns()}"
                screenshot(edge, page.resolve().as_uri(), output, profile, "1440,5120")
                print(f"rendered {output.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
