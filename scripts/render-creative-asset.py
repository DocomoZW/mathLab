#!/usr/bin/env python3
"""
Render creative assets from .md spec files for a given topic.
Parses the actual spec content and builds proper HTML visual assets.

Outputs:
  - {topic}_infographic.html   — 4-panel dark infographic from LANDSCAPE.md
  - {topic}_social-card.html   — 9:16 portrait card from SOCIAL.md
  - {topic}_animation-frames.html — frame-sequence viewer from ANIMATION_BLUEPRINT.md
"""

import json, os, sys, re, datetime
from pathlib import Path

CONTENT_DIR = "/opt/data/.hermes/content"

# ─── Spec Parser ──────────────────────────────────────────────────────

def read_spec(concept_id, filename):
    path = os.path.join(CONTENT_DIR, "creative", concept_id, filename)
    if not os.path.isfile(path):
        return None
    with open(path) as f:
        return f.read()

def extract_title(text, default=""):
    """Extract display title from # heading."""
    m = re.search(r'^#\s+(?:LANDSCAPE|SOCIAL|Animation Blueprint)\s*[—–-]?\s*(.+)$', text or "", re.M)
    return m.group(1).strip() if m else default

def extract_meta(text, key):
    """Extract a **key:** value from spec text."""
    m = re.search(r'\*\*' + re.escape(key) + r':?\*\*\s*(.+?)$', text or "", re.M)
    return m.group(1).strip() if m else ""

def strip_meta(value):
    """Strip [img:...] references and LaTeX from display text."""
    value = re.sub(r'\[img:[^\]]+\]', '', value)
    value = re.sub(r'\$([^$]+)\$', r'\1', value)
    return value.strip().strip('"').strip('"').strip('?')

def extract_section(text, section_name):
    """Extract content of a ## section."""
    pattern = r'##\s+' + re.escape(section_name) + r'.*?\n(.*?)(?=\n##\s|\Z)'
    m = re.search(pattern, text or "", re.DOTALL)
    return m.group(1).strip() if m else ""

def extract_steps(text):
    """Extract step descriptions from worked example section."""
    steps = re.findall(r'-\s+Step\s+\d+[:\s]+(.+)', text or "")
    return [strip_meta(s.strip()) for s in steps if s.strip()]

def extract_key_facts(text):
    """Extract key fact bullets."""
    facts = re.findall(r'-\s+[🔍📐⚡]\s+(.+)', text or "")
    return [strip_meta(f.strip()) for f in facts if f.strip()]

def extract_frames(text):
    """Extract frame sequence from markdown table."""
    frames = []
    for line in (text or "").split("\n"):
        # Match table rows like: | 1 | 0-2s | Visual | Purpose |
        parts = [p.strip() for p in line.split("|") if p.strip()]
        if len(parts) >= 4 and parts[0].isdigit():
            frames.append({
                "num": int(parts[0]),
                "time": parts[1],
                "visual": strip_meta(parts[2]),
                "purpose": strip_meta(parts[3]),
            })
    return frames

def hex_color(text):
    """Extract a hex color from text."""
    m = re.search(r'#([0-9a-fA-F]{6})', text or "")
    return "#" + m.group(1) if m else "#1A1A2E"


# ─── Infographic Renderer ───────────────────────────────────────────

def render_infographic(concept_id, spec):
    title = extract_title(spec)
    title_clean = strip_meta(title)
    meta_section = extract_section(spec, r"PANEL 1.*?HOOK")
    hook_text = strip_meta(extract_meta(meta_section, "Headline"))
    mascot = strip_meta(extract_meta(meta_section, "Mascot"))
    sub_line = strip_meta(extract_meta(meta_section, "Sub-line"))
    if not hook_text or hook_text.startswith("http"):
        hook_text = f"Explore {title_clean}"
    if not sub_line:
        sub_line = "Mathematics"

    def_section = extract_section(spec, r"PANEL 2.*?DEFINITION")
    def_title = strip_meta(extract_meta(def_section, "Title"))
    definition = strip_meta(extract_meta(def_section, "Definition"))
    prereqs = strip_meta(extract_meta(def_section, "Prerequisite chips"))
    if not definition or definition.startswith("http"):
        definition = f"Core concept in {title_clean}"

    we_section = extract_section(spec, r"PANEL 3.*?WORKED EXAMPLE")
    steps = extract_steps(we_section)
    if not steps:
        steps = ["Setup — identify given information",
                 "Apply — use the relevant formula or theorem",
                 "Simplify — combine like terms and reduce",
                 "Conclude — state the final answer"]

    facts_section = extract_section(spec, r"PANEL 4.*?KEY FACTS")
    facts = extract_key_facts(facts_section)
    if not facts:
        facts = [f"{title_clean} is fundamental to IGCSE mathematics",
                 "Appears in past papers across all exam boards",
                 "Links to prior topics in the syllabus"]
    cm = ""
    cm_match = re.search(r'\*\*Common mistake:\*\*\s*(.+?)$', facts_section or "", re.M)
    if cm_match:
        cm = strip_meta(cm_match.group(1).strip())

    track_color_map = {"IGCSE": "#0D7377", "A Level": "#E94560", "Add Maths": "#F5A623"}
    track_color = "#0D7377"
    for t, c in track_color_map.items():
        if t.lower() in (spec or "").lower():
            track_color = c
            break

    steps_html = "\n".join(
        f'<div class="step"><span class="num">{i+1}</span>{s}</div>'
        for i, s in enumerate(steps[:4])
    )
    facts_html = "\n".join(
        f'<div class="fact-card">📌 {f}</div>' for f in facts[:3]
    )

    return f"""<!DOCTYPE html><html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title_clean} — Infographic</title>
<style>
*{{margin:0;padding:0;box-sizing:border-box}}
body{{background:#0f0f1a;color:#e8e8f0;font-family:Inter,system-ui,sans-serif;min-height:100vh;display:flex;flex-direction:column;align-items:center;justify-content:center;padding:20px}}
.infographic{{max-width:1100px;width:100%;background:#1a1a2e;border-radius:14px;overflow:hidden;border:1px solid #2a2a4e;box-shadow:0 8px 40px rgba(0,0,0,.5)}}
.top-bar{{display:flex;align-items:center;padding:12px 20px;background:#16213e;border-bottom:1px solid #2a2a4e;gap:12px}}
.top-bar .badge{{font-size:10px;padding:3px 10px;border-radius:10px;font-weight:600}}
.top-bar .title{{font-size:15px;font-weight:600}}
.top-bar .meta{{margin-left:auto;font-size:11px;color:#8888aa}}
.grid{{display:grid;grid-template-columns:300px 1fr 280px;min-height:500px}}
.hook-panel{{background:#f5a623;padding:24px;display:flex;flex-direction:column;color:#1a1a2e}}
.hook-panel .mascot{{font-size:48px;margin-bottom:auto}}
.hook-panel .headline{{font-size:22px;font-weight:700;line-height:1.3;margin:12px 0}}
.hook-panel .sub{{font-size:11px;font-family:'JetBrains Mono',monospace;opacity:.7}}
.def-panel{{padding:24px;display:flex;flex-direction:column}}
.def-panel h2{{font-size:14px;font-weight:600;color:#8888aa;text-transform:uppercase;letter-spacing:.5px;margin-bottom:8px}}
.def-panel .big{{font-size:24px;font-weight:700;margin-bottom:8px}}
.def-panel .desc{{font-size:14px;color:#94a3b8;line-height:1.6;flex:1}}
.def-panel .tags{{display:flex;gap:6px;flex-wrap:wrap}}
.def-panel .tag{{padding:3px 10px;border-radius:10px;font-size:11px;background:rgba(233,69,96,.15);color:#e94560}}
.we-panel{{padding:24px;border-top:1px solid #2a2a4e;background:#14142a}}
.we-panel h3{{font-size:13px;font-weight:600;color:#8888aa;margin-bottom:10px;text-transform:uppercase;letter-spacing:.5px}}
.step{{padding:8px 12px;margin-bottom:6px;border-left:3px solid #e94560;background:rgba(233,69,96,.06);border-radius:0 6px 6px 0;font-size:13px;display:flex;align-items:center;gap:8px}}
.step .num{{width:22px;height:22px;background:#e94560;color:#fff;border-radius:50%;text-align:center;font-size:11px;line-height:22px;flex-shrink:0}}
.facts-panel{{background:#14142a;padding:24px;border-left:8px solid {track_color};display:flex;flex-direction:column}}
.facts-panel h3{{font-size:13px;font-weight:600;color:#8888aa;margin-bottom:10px;text-transform:uppercase;letter-spacing:.5px}}
.fact-card{{background:rgba(26,26,46,.6);border-radius:6px;padding:10px;margin-bottom:6px;font-size:12px;line-height:1.4}}
.mistake-box{{margin-top:auto;background:rgba(233,69,96,.08);border:1px solid rgba(233,69,96,.2);border-radius:6px;padding:10px;font-size:12px}}
.mistake-box .label{{color:#e94560;font-weight:600;font-size:11px;margin-bottom:4px}}
@media(max-width:768px){{.grid{{grid-template-columns:1fr}}.hook-panel{{min-height:200px}}}}
</style></head><body>
<div class="infographic">
<div class="top-bar"><span class="badge" style="background:{track_color}20;color:{track_color}">📖 Concept</span><span class="title">{escape_html(title_clean)}</span><span class="meta">MathsLMS · CreativeTeacher</span></div>
<div class="grid">
<div class="hook-panel"><div class="mascot">🔍</div><div class="headline">{escape_html(hook_text)}</div><div class="sub">{escape_html(sub_line)}</div></div>
<div style="display:flex;flex-direction:column">
<div class="def-panel"><h2>Definition</h2><div class="big">{escape_html(def_title)}</div><div class="desc">{escape_html(definition)}</div><div class="tags"><span class="tag">{escape_html(prereqs) if prereqs else "Foundation"}</span></div></div>
<div class="we-panel"><h3>✏️ Worked Example</h3>{steps_html}</div>
</div>
<div class="facts-panel"><h3>💡 Key Facts</h3>{facts_html}{f'<div class="mistake-box"><div class="label">⚠ Common Mistake</div>{escape_html(cm)}</div>' if cm else ''}</div>
</div>
</div></body></html>"""


# ─── Social Card Renderer ──────────────────────────────────────────

def render_social_card(concept_id, spec):
    title = extract_title(spec)
    title_clean = strip_meta(title)

    hook_section = extract_section(spec, r"SECTION 1.*?HOOK")
    mascot = strip_meta(extract_meta(hook_section, "Mascot"))
    question = strip_meta(extract_meta(hook_section, "Hook question"))
    if not question or question.startswith("http"):
        question = f"Can you master {title_clean}?"
    question = question.rstrip("?").strip() + "?"

    snap_section = extract_section(spec, r"SECTION 2.*?CONCEPT SNAP")
    snap_title = strip_meta(extract_meta(snap_section, "Title"))

    step_section = extract_section(spec, r"SECTION 3.*?STEP STRIP")
    steps = re.findall(r'Step\s+\d+\s*[—–-]\s*(.+?)(?:\s*\(|$)', step_section or "")
    if not steps:
        steps = ["Identify what's given", "Apply the method", "State the result"]

    cta_section = extract_section(spec, r"SECTION 4.*?CTA")
    track_badge = strip_meta(extract_meta(cta_section, "Track badge"))
    if not track_badge:
        track_badge = "MathsLMS"

    step_colors = ["#E94560", "#0D7377", "#F5A623"]
    steps_html = "\n".join(
        f'<div class="step" style="border-left-color:{step_colors[i]}">Step {i+1} — {escape_html(s)}</div>'
        for i, s in enumerate(steps[:3])
    )

    return f"""<!DOCTYPE html><html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title_clean} — Social Card</title>
<style>
*{{margin:0;padding:0;box-sizing:border-box}}
body{{background:#0f0f1a;display:flex;align-items:center;justify-content:center;min-height:100vh;font-family:Inter,system-ui,sans-serif;padding:20px}}
.card{{width:360px;height:640px;border-radius:16px;overflow:hidden;display:flex;flex-direction:column;border:1px solid #2a2a4e;box-shadow:0 8px 40px rgba(0,0,0,.5);background:#1a1a2e}}
.section{{padding:24px;display:flex;flex-direction:column;justify-content:center;text-align:center;align-items:center}}
.s1{{background:#f5a623;color:#1a1a2e;height:28%;gap:8px}}
.s1 .mascot{{font-size:40px}}
.s1 .q{{font-size:18px;font-weight:700;line-height:1.3;max-width:300px}}
.s2{{background:#0f3460;height:24%;gap:6px}}
.s2 h1{{font-size:20px;font-weight:700}}
.s2 .eq{{font-size:16px;color:#f5a623;font-style:italic;font-family:'Times New Roman',serif;opacity:.8}}
.s3{{background:#14142a;height:30%;gap:6px;text-align:left;align-items:stretch;padding:20px 24px}}
.s3 .step{{padding:8px 12px;border-left:4px solid;border-radius:0 6px 6px 0;font-size:12px;background:rgba(233,69,96,.06);color:#c8c8e0}}
.s3 .caption{{font-size:10px;color:#8888aa;text-align:right;margin-top:4px}}
.s4{{background:#0f3460;height:18%;gap:8px}}
.s4 .badge{{display:inline-block;padding:4px 14px;border-radius:12px;font-size:10px;font-weight:600;border:1px solid}}
.s4 .cta{{font-size:13px;font-weight:700;color:#e8e8f0}}
</style></head><body>
<div class="card">
<div class="section s1"><div class="mascot">🔍</div><div class="q">{escape_html(question)}</div></div>
<div class="section s2"><h1>{escape_html(snap_title or title_clean)}</h1><div class="eq">f(x) = ...</div></div>
<div class="section s3">{steps_html}<div class="caption">Swipe for full solution →</div></div>
<div class="section s4"><div class="badge" style="color:#e94560;border-color:#e94560">{escape_html(track_badge)}</div><div class="cta">Practice this on MathsLMS</div></div>
</div></body></html>"""


# ─── Animation Frame Viewer ─────────────────────────────────────────

def render_animation(concept_id, spec):
    title = extract_title(spec)
    title_clean = strip_meta(title)
    frames = extract_frames(spec)
    metaphor = strip_meta(extract_meta(spec, "METAPHOR"))
    effects = strip_meta(extract_meta(spec, "SPECIAL_EFFECTS"))
    if not metaphor:
        metaphor = f"Step-by-step visual walkthrough of {title_clean.lower()}"
    if not frames:
        frames = [
            {"num": 1, "time": "0–2s", "visual": "Opening scene", "purpose": "Hook the learner"},
            {"num": 2, "time": "2–4s", "visual": "Key concept reveal", "purpose": "Build understanding"},
            {"num": 3, "time": "4–6s", "visual": "Worked example", "purpose": "Procedural learning"},
            {"num": 4, "time": "6–8s", "visual": "Critical insight", "purpose": "Deepen grasp"},
            {"num": 5, "time": "8–10s", "visual": "Result and summary", "purpose": "Solidify"},
        ]

    frames_json = json.dumps(frames)
    return f"""<!DOCTYPE html><html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title_clean} — Animation Frames</title>
<style>
*{{margin:0;padding:0;box-sizing:border-box}}
body{{background:#0f0f1a;color:#e8e8f0;font-family:Inter,system-ui,sans-serif;min-height:100vh;display:flex;align-items:center;justify-content:center;padding:20px}}
.player{{width:800px;max-width:100%;background:#1a1a2e;border-radius:14px;overflow:hidden;border:1px solid #2a2a4e;box-shadow:0 8px 40px rgba(0,0,0,.5)}}
.top{{padding:16px 20px;background:#16213e;border-bottom:1px solid #2a2a4e;display:flex;align-items:center;gap:12px}}
.top .title{{font-size:15px;font-weight:600}}
.top .meta{{margin-left:auto;font-size:11px;color:#8888aa}}
.top .badge{{font-size:10px;padding:3px 10px;border-radius:10px;background:rgba(13,115,119,.15);color:#0d7377;font-weight:600}}
.display{{padding:48px 32px;min-height:280px;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;position:relative;background:radial-gradient(ellipse at 50% 50%,#1e1e3a,#0f0f1a)}}
.display .frame-label{{position:absolute;top:14px;left:20px;font-size:11px;color:#8888aa;font-family:'JetBrains Mono',monospace}}
.display .frame-time{{position:absolute;top:14px;right:20px;font-size:11px;color:#f5a623;font-family:'JetBrains Mono',monospace}}
.display .visual{{font-size:22px;font-weight:600;margin-bottom:12px;max-width:600px}}
.display .purpose{{font-size:14px;color:#94a3b8;max-width:500px}}
.progress{{height:4px;background:#2a2a4e;display:flex}}
.progress .seg{{flex:1;transition:all .3s;cursor:pointer}}
.progress .seg.active{{background:#e94560;box-shadow:0 0 8px rgba(233,69,96,.5)}}
.progress .seg.done{{background:#0d7377}}
.controls{{display:flex;align-items:center;justify-content:center;gap:12px;padding:14px 20px;border-top:1px solid #2a2a4e;background:#14142a}}
.controls button{{padding:8px 20px;border-radius:8px;border:1px solid #2a2a4e;background:transparent;color:#94a3b8;cursor:pointer;font-size:13px;transition:all .15s;font-family:inherit}}
.controls button:hover{{background:#e94560;color:#fff;border-color:#e94560}}
.controls .counter{{font-size:12px;color:#8888aa;font-family:'JetBrains Mono',monospace;min-width:80px;text-align:center}}
.controls .auto-btn.active{{background:#0d7377;color:#fff;border-color:#0d7377}}
.metaphor{{padding:12px 20px;font-size:11px;color:#8888aa;border-top:1px solid #2a2a4e;text-align:center;background:#14142a}}
</style></head><body>
<div class="player">
<div class="top"><span class="badge">🎬 Animation</span><span class="title">{escape_html(title_clean)}</span><span class="meta">{len(frames)} frames</span></div>
<div class="display" id="display">
<div class="frame-label" id="frameLabel">Frame 1 of {len(frames)}</div>
<div class="frame-time" id="frameTime">{frames[0]['time']}</div>
<div class="visual" id="frameVisual">{escape_html(frames[0]['visual'])}</div>
<div class="purpose" id="framePurpose">{escape_html(frames[0]['purpose'])}</div>
</div>
<div class="progress" id="progress">{"".join(f'<div class="seg" data-i="{i}"></div>' for i in range(len(frames)))}</div>
<div class="controls">
<button onclick="goFrame(current-1)" id="prevBtn">◀ Prev</button>
<span class="counter" id="counter">1 / {len(frames)}</span>
<button onclick="goFrame(current+1)" id="nextBtn">Next ▶</button>
<button class="auto-btn" id="autoBtn" onclick="toggleAuto()">▶ Auto</button>
</div>
<div class="metaphor">{escape_html(metaphor)}</div>
</div>
<script>
const frames={frames_json};
let current=0,autoInterval=null;
function goFrame(i){{
if(i<0||i>=frames.length)return;
current=i;
const f=frames[current];
document.getElementById('frameLabel').textContent='Frame '+(current+1)+' of '+frames.length;
document.getElementById('frameTime').textContent=f.time;
document.getElementById('frameVisual').textContent=f.visual;
document.getElementById('framePurpose').textContent=f.purpose;
document.getElementById('counter').textContent=(current+1)+' / '+frames.length;
document.getElementById('prevBtn').style.opacity=current===0?'.3':'1';
document.getElementById('nextBtn').style.opacity=current===frames.length-1?'.3':'1';
document.querySelectorAll('.seg').forEach((s,i)=>{{
s.classList.toggle('active',i===current);
s.classList.toggle('done',i<current);
}});
}}
function toggleAuto(){{
const btn=document.getElementById('autoBtn');
if(autoInterval){{
clearInterval(autoInterval);autoInterval=null;
btn.textContent='▶ Auto';btn.classList.remove('active');
}}else{{
autoInterval=setInterval(()=>{{if(current<frames.length-1)goFrame(current+1);else{{clearInterval(autoInterval);autoInterval=null;btn.textContent='▶ Auto';btn.classList.remove('active');}}}},2500);
btn.textContent='⏸ Pause';btn.classList.add('active');
}}}}
document.addEventListener('keydown',e=>{{if(e.key==='ArrowRight'&&current<frames.length-1)goFrame(current+1);if(e.key==='ArrowLeft'&&current>0)goFrame(current-1);}});
document.querySelectorAll('.seg').forEach(s=>s.addEventListener('click',()=>goFrame(parseInt(s.dataset.i))));
goFrame(0);
</script>
</body></html>"""


# ─── Helpers & Main ─────────────────────────────────────────────────

def escape_html(t):
    if not isinstance(t, str): return str(t or "")
    return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")

def save_asset(concept_id, filename, content):
    path = os.path.join(CONTENT_DIR, "creative", concept_id, filename)
    with open(path, "w") as f:
        f.write(content)
    return path

def main():
    if len(sys.argv) < 2:
        print("Usage: render-creative-asset.py <concept_id>")
        sys.exit(1)
    concept_id = sys.argv[1]
    creative_dir = os.path.join(CONTENT_DIR, "creative", concept_id)
    if not os.path.isdir(creative_dir):
        print(f"Error: No creative directory for {concept_id}")
        sys.exit(1)

    landscape = read_spec(concept_id, "LANDSCAPE.md")
    social = read_spec(concept_id, "SOCIAL.md")
    anim = read_spec(concept_id, "ANIMATION_BLUEPRINT.md")
    assets = []

    if landscape:
        p = render_infographic(concept_id, landscape)
        fn = f"{concept_id}_infographic.html"
        save_asset(concept_id, fn, p)
        print(f"  ✅ Infographic HTML: {fn}")
        assets.append(fn)

    if social:
        p = render_social_card(concept_id, social)
        fn = f"{concept_id}_social-card.html"
        save_asset(concept_id, fn, p)
        print(f"  ✅ Social card HTML: {fn}")
        assets.append(fn)

    if anim:
        p = render_animation(concept_id, anim)
        fn = f"{concept_id}_animation-frames.html"
        save_asset(concept_id, fn, p)
        print(f"  ✅ Animation frames HTML: {fn}")
        assets.append(fn)

    if assets:
        print(f"\nRendered {len(assets)} assets for {concept_id}")
    else:
        print("No spec files found")

if __name__ == "__main__":
    main()
