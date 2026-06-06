#!/usr/bin/env python3
"""
render_gifs.py — Render all Manim animation scripts to GIF

Usage:
  python render_gifs.py                        # render all 224 scripts
  python render_gifs.py --unit A1_Number       # one unit only
  python render_gifs.py --quality l            # low quality (faster)
  python render_gifs.py --dry-run              # preview what would run

Output: gifs/<script-stem>.gif  (flat folder, skip already-rendered)

Quality options:
  l = low   (480p15)  ~5-15s per animation
  m = medium (720p30)  ~15-40s per animation  [default]
  h = high  (1080p60)  ~60-120s per animation
"""

import re
import sys
import subprocess
import shutil
import time
import argparse
from pathlib import Path

ANIMATIONS_DIR = Path(__file__).parent / "animations"
OUTPUT_DIR     = Path(__file__).parent / "gifs"
TMP_MEDIA_DIR  = OUTPUT_DIR / "_manim_tmp"

QUALITY_FLAGS = {"l": "-ql", "m": "-qm", "h": "-qh"}

def find_class_name(script: Path) -> str | None:
    text = script.read_text(encoding="utf-8", errors="replace")
    m = re.search(r"^class (\w+)\(", text, re.MULTILINE)
    return m.group(1) if m else None

def render_script(script: Path, class_name: str, quality: str) -> tuple[bool, str]:
    out_gif = OUTPUT_DIR / f"{script.stem}.gif"
    if out_gif.exists():
        return True, f"skip ({out_gif.stat().st_size // 1024} KB already exists)"

    cmd = [
        sys.executable, "-m", "manim",
        QUALITY_FLAGS[quality],
        "--format", "gif",
        "--media_dir", str(TMP_MEDIA_DIR),
        "--disable_caching",
        str(script),
        class_name,
    ]

    result = subprocess.run(cmd, capture_output=True, text=True, timeout=300)

    if result.returncode != 0:
        # Surface the last 400 chars of stderr for diagnosis
        snippet = (result.stderr or result.stdout or "no output")[-400:].strip()
        return False, snippet

    # Find the GIF Manim produced (deepest match = most recent render)
    gifs = sorted(TMP_MEDIA_DIR.rglob("*.gif"), key=lambda p: p.stat().st_mtime)
    if not gifs:
        return False, "manim exited 0 but produced no .gif file"

    shutil.copy2(gifs[-1], out_gif)
    return True, f"{out_gif.stat().st_size // 1024} KB"

def main():
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--quality", choices=["l", "m", "h"], default="m",
                        help="Render quality: l/m/h (default: m)")
    parser.add_argument("--unit", metavar="FOLDER",
                        help="Only render scripts inside this unit subfolder, e.g. A1_Number")
    parser.add_argument("--dry-run", action="store_true",
                        help="Print what would be rendered without running Manim")
    args = parser.parse_args()

    OUTPUT_DIR.mkdir(exist_ok=True)
    TMP_MEDIA_DIR.mkdir(parents=True, exist_ok=True)

    scripts = sorted(ANIMATIONS_DIR.rglob("*.py"))
    if args.unit:
        scripts = [s for s in scripts if args.unit in s.parts]

    if not scripts:
        print(f"No scripts found{' for unit ' + args.unit if args.unit else ''}.")
        return

    total    = len(scripts)
    ok = fail = skip = 0
    failed   = []

    q_labels = {"l": "low (480p15)", "m": "medium (720p30)", "h": "high (1080p60)"}
    print(f"Rendering {total} scripts  |  quality = {q_labels[args.quality]}")
    print(f"Output -> {OUTPUT_DIR}\n")

    session_start = time.time()

    for i, script in enumerate(scripts, 1):
        class_name = find_class_name(script)
        if not class_name:
            print(f"[{i:3}/{total}] SKIP  {script.name}  (no class found)")
            skip += 1
            continue

        label = f"{script.parent.name}/{script.stem}"

        if args.dry_run:
            already = (OUTPUT_DIR / f"{script.stem}.gif").exists()
            status = "exists" if already else "would render"
            print(f"[{i:3}/{total}] {status:13}  {label}  ({class_name})")
            continue

        print(f"[{i:3}/{total}] rendering  {label} ...", end="", flush=True)
        t0 = time.time()
        success, msg = render_script(script, class_name, args.quality)
        elapsed = time.time() - t0

        if success:
            ok += 1
            marker = "skip" if msg.startswith("skip") else "OK  "
            print(f"\r[{i:3}/{total}] {marker}       {label}  ({msg})  [{elapsed:.0f}s]")
        else:
            fail += 1
            failed.append((script.name, msg))
            print(f"\r[{i:3}/{total}] FAIL       {label}  [{elapsed:.0f}s]")
            print(f"             {msg[:120]}")

    if args.dry_run:
        return

    total_time = time.time() - session_start
    print(f"\n{'='*60}")
    print(f"Finished in {total_time/60:.1f} min  |  {ok} OK  |  {fail} failed  |  {skip} skipped")

    if failed:
        print("\nFailed scripts:")
        for name, msg in failed:
            print(f"  ✗ {name}")
            print(f"    {msg[:120]}")

    # Clean up Manim's temp media tree
    if TMP_MEDIA_DIR.exists():
        shutil.rmtree(TMP_MEDIA_DIR)
        print(f"\nCleaned up {TMP_MEDIA_DIR}")

if __name__ == "__main__":
    main()