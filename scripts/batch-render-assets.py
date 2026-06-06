#!/usr/bin/env python3
"""
Batch render all topics that have .md specs but no rendered assets yet.
Processes them all in one shot.
"""

import json, os, sys, subprocess

CONTENT_DIR = "/opt/data/.hermes/content"
MANIFEST_PATH = os.path.join(CONTENT_DIR, "creative", "manifest.json")
RENDER_SCRIPT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "render-creative-asset.py")

def load_manifest():
    with open(MANIFEST_PATH) as f:
        return json.load(f)

def save_manifest(m):
    with open(MANIFEST_PATH, "w") as f:
        json.dump(m, f, indent=2)

def main():
    manifest = load_manifest()
    total = len(manifest.get("concepts", []))
    rendered = 0
    errors = []

    # Find topics needing render (have specs, no rendered_assets)
    to_render = []
    for c in manifest["concepts"]:
        tid = c["concept_id"]
        has_files = any(f.endswith(".md") for f in c.get("files", []))
        already_rendered = bool(c.get("rendered_assets"))
        if has_files and not already_rendered:
            to_render.append(tid)

    print(f"📊 {len(to_render)} topics to render, {total - len(to_render)} already done")
    if not to_render:
        print("✅ All topics already rendered!")
        return

    for i, tid in enumerate(to_render, 1):
        try:
            result = subprocess.run(
                ["python3", RENDER_SCRIPT, tid],
                capture_output=True, text=True, timeout=60,
                cwd=os.path.dirname(RENDER_SCRIPT)
            )
            if result.returncode == 0:
                rendered += 1
                # Update manifest with rendered assets
                creative_dir = os.path.join(CONTENT_DIR, "creative", tid)
                assets = [f for f in os.listdir(creative_dir)
                         if f.endswith(".html") and not f.startswith(".")]
                for c in manifest["concepts"]:
                    if c["concept_id"] == tid:
                        if assets:
                            c["rendered_assets"] = assets
                        break
                if i % 10 == 0:
                    save_manifest(manifest)
                    print(f"  {i}/{len(to_render)} — {tid} ✅ ({len(assets)} assets)")
                    sys.stdout.flush()
            else:
                errors.append(f"{tid}: {result.stderr.strip() or 'unknown error'}")
                print(f"  ❌ {tid}: render failed")

        except Exception as e:
            errors.append(f"{tid}: {e}")
            print(f"  ❌ {tid}: {e}")

    save_manifest(manifest)
    print(f"\n✅ Rendered {rendered}/{len(to_render)} topics to HTML assets")
    if errors:
        print(f"⚠  {len(errors)} errors:\n" + "\n".join(errors[:10]))
        sys.exit(1)

if __name__ == "__main__":
    main()
