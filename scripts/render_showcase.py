#!/usr/bin/env python3
"""Capture fixed GitHub README pages and render exact showcase comparison cards."""

from __future__ import annotations

import argparse
import html
import json
from pathlib import Path
import subprocess
import time


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


def render_html(case: dict) -> str:
    preview = case["preview"]
    accent = html.escape(case["accent"])
    action = html.escape(preview["action"]).replace("\n", "<br>")
    proof = "".join(f"<li>{html.escape(item)}</li>" for item in preview["proof"])
    before_uri = (ROOT / case["before_image"]).resolve().as_uri()
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(case['category'])} README comparison</title>
<style>
* {{ box-sizing: border-box; }}
html, body {{ width: 1400px; height: 900px; margin: 0; overflow: hidden; }}
body {{ background: #07101f; color: #e5edf8; font-family: Inter, "Segoe UI", Arial, sans-serif; }}
.page {{ width: 1400px; height: 900px; padding: 42px; background: radial-gradient(circle at 90% 0%, {accent}22, transparent 32%), linear-gradient(145deg, #07101f, #0f172a); }}
.top {{ height: 76px; display: flex; align-items: flex-start; justify-content: space-between; }}
.kicker {{ color: {accent}; font-size: 14px; font-weight: 800; letter-spacing: .14em; }}
.repo {{ margin-top: 10px; font-size: 27px; font-weight: 750; color: #f8fafc; }}
.sha {{ color: #94a3b8; font: 14px ui-monospace, SFMono-Regular, Consolas, monospace; padding-top: 8px; }}
.grid {{ display: grid; grid-template-columns: 1fr 1fr; gap: 26px; height: 716px; }}
.panel {{ position: relative; overflow: hidden; border: 1px solid #26364f; border-radius: 24px; background: #0b1424; box-shadow: 0 22px 60px #02061799; }}
.label {{ position: absolute; z-index: 4; top: 18px; left: 18px; padding: 9px 12px; border-radius: 999px; background: #020617e8; color: #dbeafe; font-size: 12px; font-weight: 800; letter-spacing: .08em; border: 1px solid #334155; }}
.before {{ background: #f8fafc; }}
.before img {{ position: absolute; width: 1400px; height: 1200px; max-width: none; left: -325px; top: -165px; object-fit: cover; }}
.before:after {{ content: ""; position: absolute; inset: 0; box-shadow: inset 0 0 0 1px #ffffff22; pointer-events: none; }}
.after {{ padding: 78px 42px 38px; border-color: {accent}88; }}
.eyebrow {{ color: {accent}; font-size: 13px; font-weight: 800; letter-spacing: .1em; }}
h1 {{ margin: 18px 0 10px; color: #f8fafc; font-size: 42px; line-height: 1.06; letter-spacing: -.03em; }}
.tagline {{ color: #cbd5e1; font-size: 18px; line-height: 1.5; }}
.status {{ margin: 24px 0; padding: 16px 18px; border-left: 4px solid {accent}; border-radius: 8px; background: #111f33; color: #e2e8f0; font-size: 15px; line-height: 1.45; }}
.action-title {{ margin-top: 26px; color: #94a3b8; font-size: 12px; font-weight: 800; letter-spacing: .1em; }}
pre {{ margin: 10px 0 22px; padding: 16px 18px; border: 1px solid #26364f; border-radius: 12px; background: #050b15; color: #d9f99d; font: 15px/1.55 ui-monospace, SFMono-Regular, Consolas, monospace; white-space: normal; }}
ul {{ margin: 0; padding-left: 20px; color: #cbd5e1; font-size: 15px; line-height: 1.7; }}
li::marker {{ color: {accent}; }}
.footer {{ height: 52px; display: flex; align-items: flex-end; justify-content: space-between; color: #64748b; font-size: 13px; }}
.footer strong {{ color: #94a3b8; }}
</style>
</head>
<body>
<main class="page">
  <header class="top">
    <div><div class="kicker">README SKILLS · BEFORE / AFTER</div><div class="repo">{html.escape(case['repository'])}</div></div>
    <div class="sha">fixed {html.escape(case['sha'][:12])}</div>
  </header>
  <section class="grid">
    <article class="panel before"><div class="label">BEFORE · GitHub snapshot</div><img src="{before_uri}" alt=""></article>
    <article class="panel after">
      <div class="label">AFTER · Matched first screen</div>
      <div class="eyebrow">{html.escape(preview['eyebrow'])}</div>
      <h1>{html.escape(preview['title'])}</h1>
      <div class="tagline">{html.escape(preview['tagline'])}</div>
      <div class="status">{html.escape(preview['status'])}</div>
      <div class="action-title">PRIMARY READER ACTION</div>
      <pre>{action}</pre>
      <ul>{proof}</ul>
    </article>
  </section>
  <footer class="footer"><span>Illustrative first-screen comparison; full rewrite and evidence remain in the repository.</span><strong>readme-skills</strong></footer>
</main>
</body>
</html>"""


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--capture", action="store_true", help="capture fixed GitHub README pages")
    parser.add_argument("--render", action="store_true", help="render local comparison cards")
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
            screenshot(edge, case["source_readme"], before, profile, "1440,1200")
            print(f"captured {before.relative_to(ROOT)}")
        if render:
            ensure_png(before)
            page = WORK / "pages" / f"{case['id']}.html"
            page.parent.mkdir(parents=True, exist_ok=True)
            page.write_text(render_html(case), encoding="utf-8")
            output = ROOT / case["comparison_image"]
            if args.force or not output.exists():
                profile = WORK / "profiles" / f"{case['id']}-card-{time.time_ns()}"
                screenshot(edge, page.resolve().as_uri(), output, profile, "1400,900")
                print(f"rendered {output.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
