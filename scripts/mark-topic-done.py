#!/usr/bin/env python3
"""
Mark a topic as having creative assets generated (called after the cron job finishes).
Updates the creative manifest to record what was generated.
"""

import json, os, sys, datetime

CONTENT_DIR = "/opt/data/.hermes/content"
CREATIVE_MANIFEST = os.path.join(CONTENT_DIR, "creative", "manifest.json")

def main():
    if len(sys.argv) < 2:
        print("Usage: mark-topic-done.py <topic_id> [files...]")
        sys.exit(1)

    topic_id = sys.argv[1]
    generated_files = sys.argv[2:] if len(sys.argv) > 2 else []

    if os.path.isfile(CREATIVE_MANIFEST):
        with open(CREATIVE_MANIFEST) as f:
            manifest = json.load(f)
    else:
        manifest = {"description": "Creative asset outputs", "skills": [
            "infographic-architect", "animation-blueprint"
        ], "concepts": []}

    # Remove existing entry for this topic if present
    manifest["concepts"] = [c for c in manifest["concepts"]
                           if c.get("concept_id") != topic_id]

    manifest["concepts"].append({
        "concept_id": topic_id,
        "generated_at": datetime.datetime.now().isoformat(),
        "files": generated_files,
    })

    os.makedirs(os.path.dirname(CREATIVE_MANIFEST), exist_ok=True)
    with open(CREATIVE_MANIFEST, "w") as f:
        json.dump(manifest, f, indent=2)

    print(f"✅ Marked {topic_id} as done with {len(generated_files)} files")

if __name__ == "__main__":
    main()
