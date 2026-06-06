#!/usr/bin/env python3
"""
Pick the next unprocessed topic for the creative asset cron job.
Outputs JSON with topic info on stdout, or {"done": true} if all processed.

Uses the creative manifest to track which topics have been generated.
"""

import json, os, sys, glob
from pathlib import Path

CONTENT_DIR = "/opt/data/.hermes/content"
CREATIVE_MANIFEST = os.path.join(CONTENT_DIR, "creative", "manifest.json")

# All curriculum JSONs (excluding problem files)
def scan_topics():
    topics = []
    for root, dirs, files in os.walk(os.path.join(CONTENT_DIR, "curriculum")):
        for fn in sorted(files):
            if not fn.endswith(".json") or "_problems" in fn or fn.startswith("."):
                continue
            fp = os.path.join(root, fn)
            with open(fp) as f:
                try:
                    data = json.load(f)
                except:
                    continue
            topic_id = data.get("topic_id", "")
            title = data.get("title", "")
            track = data.get("track", "")
            unit = data.get("unit", "")
            if topic_id:
                topics.append({
                    "topic_id": topic_id,
                    "title": title,
                    "track": track,
                    "unit": unit,
                    "path": fp,
                })
    return topics

# Load manifest to see what's been done
def load_manifest():
    if os.path.isfile(CREATIVE_MANIFEST):
        with open(CREATIVE_MANIFEST) as f:
            return json.load(f)
    return {"concepts": []}

def save_manifest(manifest):
    os.makedirs(os.path.dirname(CREATIVE_MANIFEST), exist_ok=True)
    with open(CREATIVE_MANIFEST, "w") as f:
        json.dump(manifest, f, indent=2)

def main():
    topics = scan_topics()
    manifest = load_manifest()
    done_ids = {c.get("concept_id", ""): c for c in manifest.get("concepts", [])
                if c.get("concept_id", "")}

    # Find first unprocessed topic (skip ones that already have assets)
    for t in topics:
        tid = t["topic_id"]
        if tid in done_ids:
            continue
        # Output this topic as JSON
        print(json.dumps(t))
        return

    # All done
    print(json.dumps({"done": True, "total": len(topics), "generated": len(done_ids)}))

if __name__ == "__main__":
    main()
