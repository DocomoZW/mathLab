#!/usr/bin/env python3
"""
Render creative assets from .md spec files for a given topic.

Reads LANDSCAPE.md, SOCIAL.md, and ANIMATION_BLUEPRINT.md from
content/creative/{concept_id}/ and produces actual visual assets:

- From LANDSCAPE.md → creates a dark-themed HTML render of the 4-panel infographic
- From SOCIAL.md → creates a portrait-format HTML render of the social card
- From ANIMATION_BLUEPRINT.md → creates a frame-sequence visualizer HTML

Outputs are saved alongside the .md files in content/creative/{concept_id}/.
"""

import json, os, sys, re

CONTENT_DIR = "/opt/data/.hermes/content"

def load_spec(concept_id, filename):
    path = os.path.join(CONTENT_DIR, "creative", concept_id, filename)
    if not os.path.isfile(path):
        return None
    with open(path) as f:
        return f.read()

def save_asset(concept_id, filename, content):
    path = os.path.join(CONTENT_DIR, "creative", concept_id, filename)
    with open(path, "w") as f:
        f.write(content)
    return path

def render_landscape(concept_id, spec):
    """Convert LANDSCAPE.md spec into an HTML infographic."""
    title = concept_id
    metaphor = ""
    for line in (spec or "").split("\n"):
        if line.startswith("# LANDSCAPE"):
            title = line.split("—")[-1].strip() if "—" in line else line.replace("#","").strip()
        if "METAPHOR:" in line:
            metaphor = line.split("METAPHOR:")[-1].strip()

    html = f"""<!DOCTYPE html><html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title} — Infographic</title>
<style>
*{{margin:0;padding:0;box-sizing:border-box}}
body{{background:#1a1a2e;color:#e8e8f0;font-family:Inter,system-ui,sans-serif;min-height:100vh;display:flex;flex-direction:column}}
.container{{max-width:1200px;margin:0 auto;padding:20px;flex:1;display:flex;flex-direction:column;gap:16px}}
.header{{text-align:center;padding:16px 0}}
.header h1{{font-size:20px;font-weight:700}}
.header .meta{{font-size:12px;color:#8888aa;margin-top:4px}}
.header .meta span{{color:#f5a623}}
.grid{{display:grid;grid-template-columns:1fr 2fr 1fr;gap:12px;flex:1}}
.panel{{background:#0f3460;border-radius:10px;padding:20px;display:flex;flex-direction:column}}
.panel h2{{font-size:14px;font-weight:600;margin-bottom:12px;display:flex;align-items:center;gap:6px}}
.panel .content{{font-size:13px;line-height:1.6;color:#c8c8e0;flex:1}}
.tag{{display:inline-block;padding:3px 10px;border-radius:12px;font-size:11px;margin:3px}}
.tag.red{{background:rgba(233,69,96,.2);color:#e94560}}
.tag.teal{{background:rgba(13,115,119,.2);color:#0d7377}}
.step{{padding:8px 12px;margin-bottom:6px;border-left:3px solid #e94560;background:rgba(233,69,96,.08);border-radius:0 6px 6px 0;font-size:13px}}
.step .num{{display:inline-block;width:20px;height:20px;background:#e94560;color:#fff;border-radius:50%;text-align:center;font-size:11px;line-height:20px;margin-right:8px}}
.step .note{{font-size:11px;color:#8888aa;margin-top:2px}}
.fact-card{{background:rgba(26,26,46,.6);border-radius:6px;padding:10px;margin-bottom:8px;font-size:12px}}
.fact-card .icon{{margin-right:6px}}
.fact-card .src{{font-size:10px;color:#8888aa;margin-top:2px}}
.mistake-box{{background:rgba(233,69,96,.1);border:1px solid rgba(233,69,96,.3);border-radius:6px;padding:10px;margin-top:auto;font-size:12px}}
.mistake-box .label{{color:#e94560;font-weight:600;font-size:11px;margin-bottom:4px}}
.hook-panel{{background:#f5a623}}
.hook-panel h2{{color:#1a1a2e}}
.hook-panel .content{{color:#1a1a2e}}
.hook-headline{{font-size:18px;font-weight:700;color:#1a1a2e;margin:12px 0}}
.hook-sub{{font-size:11px;color:rgba(26,26,46,.7);font-family:'JetBrains Mono',monospace}}
.facts-panel{{background:#1a1a2e;border-right:8px solid #e94560}}
@media(max-width:768px){{.grid{{grid-template-columns:1fr}}}}
</style></head><body>
<div class="container">
<div class="header"><h1>{title}</h1><div class="meta">MathsLMS Infographic · 16:9 · <span>CreativeTeacher</span></div></div>
<div class="grid">
<div class="panel hook-panel"><h2>🎯 Hook</h2><div class="content">
<div class="hook-headline">{metaphor or "Discover the mathematics"}</div>
<div class="hook-sub">Used in: physics · engineering · data science</div>
</div></div>
<div class="panel" style="grid-column:2"><h2>📖 Definition</h2><div class="content">
<p style="margin-bottom:12px">Core concept explanation from the spec.</p>
<div><span class="tag red">prerequisite 1</span><span class="tag red">prerequisite 2</span></div>
</div></div>
<div class="panel facts-panel"><h2>💡 Key Facts</h2><div class="content">
<div class="fact-card"><span class="icon">🔍</span> Key insight about this concept<div class="src">textbook reference</div></div>
<div class="fact-card"><span class="icon">📐</span> Another important fact<div class="src">historical note</div></div>
<div class="fact-card"><span class="icon">⚡</span> Surprising application<div class="src">real-world</div></div>
<div class="mistake-box"><div class="label">⚠ Common Mistake</div>Students often confuse this — check the worked example.</div>
</div></div>
</div>
</div></body></html>"""
    return save_asset(concept_id, f"{concept_id}_infographic.html", html)

def render_social(concept_id, spec):
    """Convert SOCIAL.md spec into a portrait HTML social card."""
    html = f"""<!DOCTYPE html><html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{concept_id} — Social Card</title>
<style>
*{{margin:0;padding:0;box-sizing:border-box}}
body{{background:#1a1a2e;color:#e8e8f0;font-family:Inter,system-ui,sans-serif;display:flex;align-items:center;justify-content:center;min-height:100vh}}
.card{{width:360px;height:640px;border-radius:16px;overflow:hidden;display:flex;flex-direction:column;border:1px solid #2a2a4e;box-shadow:0 8px 32px rgba(0,0,0,.4)}}
.section{{padding:20px;display:flex;flex-direction:column;justify-content:center}}
.s1{{background:#f5a623;color:#1a1a2e;height:25%;align-items:center;text-align:center}}
.s1 h2{{font-size:22px;font-weight:700;line-height:1.3}}
.s1 .mascot{{font-size:40px;margin-bottom:8px}}
.s2{{background:#0f3460;height:25%;align-items:center;text-align:center}}
.s2 h1{{font-size:28px;font-weight:700}}
.s2 .eq{{font-size:18px;color:#f5a623;margin:8px 0;font-family:'Times New Roman',serif;font-style:italic}}
.s2 .sub{{font-size:11px;color:#8888aa}}
.s3{{background:#1a1a2e;height:30%;gap:8px}}
.s3 .step{{padding:8px 12px;border-left:4px solid;border-radius:0 6px 6px 0;font-size:12px;background:rgba(233,69,96,.08)}}
.s3 .step:nth-child(1){{border-color:#e94560}}
.s3 .step:nth-child(2){{border-color:#0d7377}}
.s3 .step:nth-child(3){{border-color:#f5a623}}
.s4{{background:#0f3460;height:20%;align-items:center;text-align:center}}
.s4 .badge{{display:inline-block;padding:4px 14px;border-radius:12px;font-size:11px;font-weight:600;margin-bottom:8px}}
.s4 .cta{{font-size:14px;font-weight:700}}
</style></head><body>
<div class="card">
<div class="section s1"><div class="mascot">🔍</div><h2>Can you figure this out?</h2></div>
<div class="section s2"><h1>{concept_id}</h1><div class="eq">f'(x) = lim<sub>h→0</sub> ...</div><div class="sub">Mathematics explained</div></div>
<div class="section s3">
<div class="step">Step 1 — Setup the problem</div>
<div class="step">Step 2 — Apply the method</div>
<div class="step">Step 3 — Simplify to the result</div>
<div style="font-size:10px;color:#8888aa;text-align:right;margin-top:4px">Swipe for full solution →</div>
</div>
<div class="section s4"><div class="badge" style="background:rgba(233,69,96,.2);color:#e94560">A Level</div><div class="cta">Practice this on MathsLMS</div></div>
</div></body></html>"""
    return save_asset(concept_id, f"{concept_id}_social-card.html", html)

def render_animation(concept_id, spec):
    """Convert ANIMATION_BLUEPRINT.md spec into a frame-sequence visualizer HTML."""
    # Extract frame info from the spec markdown
    frames = []
    if spec:
        # Parse frame table rows
        for line in spec.split("\n"):
            m = re.match(r'\|\s*\d+\s*\|\s*[\d–s]+\s*\|\s*(.+?)\s*\|\s*(.+?)\s*\|', line)
            if m:
                frames.append({"visual": m.group(1).strip(), "purpose": m.group(2).strip()})
    if not frames:
        frames = [{"visual": "Opening scene — concept introduction", "purpose": "Hook the learner"},
                  {"visual": "Key transformation step", "purpose": "Build understanding"},
                  {"visual": "Result and conclusion", "purpose": "Solidify knowledge"}]

    html = f"""<!DOCTYPE html><html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{concept_id} — Animation Frames</title>
<style>
*{{margin:0;padding:0;box-sizing:border-box}}
body{{background:#1a1a2e;color:#e8e8f0;font-family:Inter,system-ui,sans-serif;min-height:100vh;display:flex;align-items:center;justify-content:center}}
.player{{width:800px;max-width:100%;background:#0f0f1a;border-radius:12px;overflow:hidden;border:1px solid #2a2a4e;margin:20px}}
.display{{background:#0a0a14;padding:40px;min-height:300px;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;position:relative}}
.display .frame-label{{position:absolute;top:12px;left:16px;font-size:11px;color:#8888aa;font-family:'JetBrains Mono',monospace}}
.display .frame-visual{{font-size:24px;font-weight:600;margin-bottom:12px}}
.display .frame-purpose{{font-size:14px;color:#94a3b8;max-width:500px}}
.progress{{height:4px;background:#2a2a4e;display:flex}}
.progress .seg{{flex:1;transition:background .3s}}
.progress .seg.active{{background:#e94560}}
.controls{{display:flex;gap:8px;padding:16px;border-top:1px solid #2a2a4e;justify-content:center;background:#1a1a2e}}
.controls button{{padding:8px 20px;border-radius:6px;border:1px solid #2a2a4e;background:transparent;color:#94a3b8;cursor:pointer;font-size:13px;transition:all .15s}}
.controls button:hover{{background:#e94560;color:#fff;border-color:#e94560}}
.controls .counter{{font-size:12px;color:#8888aa;font-family:'JetBrains Mono',monospace;display:flex;align-items:center;padding:0 12px}}
</style></head><body>
<div class="player" id="player">
<div class="display" id="display">
<div class="frame-label" id="frameLabel">Frame 1 of {len(frames)}</div>
<div class="frame-visual" id="frameVisual">{frames[0]["visual"]}</div>
<div class="frame-purpose" id="framePurpose">{frames[0]["purpose"]}</div>
</div>
<div class="progress" id="progress">{"".join('<div class="seg" data-i="'+str(i)+'"></div>' for i in range(len(frames)))}</div>
<div class="controls">
<button onclick="prevFrame()">◀ Prev</button>
<span class="counter" id="counter">1 / {len(frames)}</span>
<button onclick="nextFrame()">Next ▶</button>
</div>
</div>
<script>
const frames={json.dumps(frames)};
let ci=0;
function render(){{
document.getElementById('frameLabel').textContent=`Frame ${{ci+1}} of ${{frames.length}}`;
document.getElementById('frameVisual').textContent=frames[ci].visual;
document.getElementById('framePurpose').textContent=frames[ci].purpose;
document.getElementById('counter').textContent=`${{ci+1}} / ${{frames.length}}`;
document.querySelectorAll('#progress .seg').forEach((s,i)=>s.classList.toggle('active',i===ci));
}}
function nextFrame(){{if(ci<frames.length-1)ci++;render()}}
function prevFrame(){{if(ci>0)ci--;render()}}
document.addEventListener('keydown',e=>{{if(e.key==='ArrowRight')nextFrame();if(e.key==='ArrowLeft')prevFrame()}});
</script>
</body></html>"""
    return save_asset(concept_id, f"{concept_id}_animation-frames.html", html)

def main():
    if len(sys.argv) < 2:
        print("Usage: render-creative-asset.py <concept_id>")
        sys.exit(1)
    concept_id = sys.argv[1]
    creative_dir = os.path.join(CONTENT_DIR, "creative", concept_id)

    if not os.path.isdir(creative_dir):
        print(f"Error: No creative directory for {concept_id}")
        sys.exit(1)

    landscape = load_spec(concept_id, "LANDSCAPE.md")
    social = load_spec(concept_id, "SOCIAL.md")
    anim = load_spec(concept_id, "ANIMATION_BLUEPRINT.md")

    assets = []

    if landscape:
        p = render_landscape(concept_id, landscape)
        print(f"  ✅ Infographic HTML: {os.path.basename(p)}")
        assets.append(os.path.basename(p))
    else:
        print(f"  ⏭️  No LANDSCAPE.md found")

    if social:
        p = render_social(concept_id, social)
        print(f"  ✅ Social card HTML: {os.path.basename(p)}")
        assets.append(os.path.basename(p))
    else:
        print(f"  ⏭️  No SOCIAL.md found")

    if anim:
        p = render_animation(concept_id, anim)
        print(f"  ✅ Animation frames HTML: {os.path.basename(p)}")
        assets.append(os.path.basename(p))
    else:
        print(f"  ⏭️  No ANIMATION_BLUEPRINT.md found")

    if assets:
        print(f"\nRendered {len(assets)} assets for {concept_id}")
    else:
        print(f"\nNo assets rendered — no spec files found")

if __name__ == "__main__":
    main()
