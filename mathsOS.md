# mathsOS — MathsLMS Dashboard on Hermes (Hostinger VPS)

Adapting the [Hermes AgentOS Mission Control Dashboard](https://komputermechanic.com/tutorials/hermes-dashboard)
to monitor and command the MathsLMS multi-agent Claude pipeline on your Hostinger VPS.

---

## What This Is

The Hermes dashboard tutorial builds a glassmorphism ops console for a 4-agent content team. MathsLMS needs
the same thing, but for a 10-agent mathematics content pipeline. This guide maps your Blueprint's agent roster
to the Hermes structure, adapts every dashboard tab, and covers Hostinger-specific remote access.

You get one unified screen showing: which agents are running, what content is being generated, past paper
tagging progress, GIF render status, and a personal task board — all live from your VPS.

---

## 1. Agent Roster Mapping

The Hermes tutorial builds 4 specialist agents (Scout, Scribe, Reach, Dev) plus an Orchestrator. Replace these
with the MathsLMS agent roster from your Blueprint. Use the same Discord channel wiring pattern.

| Hermes Original | MathsLMS Equivalent | Discord Channel | Model |
|---|---|---|---|
| Orchestrator (Telegram) | **Orchestrator** — decomposes goals, delegates, validates | Telegram | Claude Opus |
| Scout | **Curriculum** — writes concept scripts, IGCSE/IMO alignment | #curriculum | Claude Sonnet |
| Scribe | **Content** — formats scripts to structured JSON, LaTeX | #content | Claude Sonnet |
| Reach | **Animation** — writes Manim scripts, Canvas JS animations | #animation | Claude Sonnet |
| Dev | **Problems** — generates practice problems at 4 difficulty levels | #problems | Claude Sonnet |
| *(add)* | **Tagger** — bulk-tags past paper PDFs using vision | #tagger | Claude Haiku |
| *(add)* | **Walkthrough** — generates step-by-step past paper solutions | #walkthrough | Claude Sonnet |
| *(add)* | **QA** — reviews all content for mathematical accuracy | #qa | Claude Sonnet |
| *(add)* | **Hints** — live Socratic tutor, tiered hint ladder | #hints | Claude Opus |
| *(add)* | **Deploy** — runs builds, CI/CD, monitors Sentry | #deploy | Claude Haiku |

The Hermes logging script, SQLite schema, and dashboard backend handle N agents gracefully — just add rows.

---

## 2. Database Schema Adaptations

The tutorial creates three databases at `~/.hermes/`. Keep that structure and add one MathsLMS-specific file.

### Keep as-is
- `~/.hermes/agent-logs.db` — activity log (agent name, task, status, model, timestamp)
- `~/.hermes/state.db` — sessions and token usage (Hermes internal)
- `~/.hermes/gateway_state.json` — live gateway status

### Adapt: `~/.hermes/kanban.db`
The tutorial's kanban tracks operator tasks. Extend it for MathsLMS content pipeline tasks:

```sql
-- Run this in the Hermes kanban.db setup prompt (Part 06, Prompt 1)
-- Add to the existing board.db board table or create alongside it:

CREATE TABLE IF NOT EXISTS content_tasks (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  track TEXT,           -- 'igcse_o' | 'a_level' | 'imo'
  unit TEXT,            -- 'A1_Number', 'P1_Quadratics', etc.
  topic_id TEXT,        -- e.g. 'A2_Q3'
  stage TEXT,           -- 'concept_script' | 'manim_script' | 'gif_rendered' | 'problems' | 'qa_pass'
  status TEXT DEFAULT 'pending',  -- 'pending' | 'in_progress' | 'done' | 'flagged'
  agent TEXT,           -- which agent owns this task
  notes TEXT,
  created_at TEXT DEFAULT (datetime('now')),
  updated_at TEXT DEFAULT (datetime('now'))
);

CREATE TABLE IF NOT EXISTS gif_renders (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  topic_id TEXT,
  manim_script_path TEXT,
  gif_path TEXT,
  r2_url TEXT,
  render_status TEXT DEFAULT 'queued',  -- 'queued' | 'rendering' | 'done' | 'error'
  file_size_kb INTEGER,
  duration_sec REAL,
  created_at TEXT DEFAULT (datetime('now'))
);

CREATE TABLE IF NOT EXISTS past_paper_progress (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  collection TEXT,      -- 'O_Level_4024' | 'IGCSE_0580' | 'A_Level_9709' | 'AMC' | 'AIME'
  year INTEGER,
  paper TEXT,
  total_questions INTEGER,
  tagged INTEGER DEFAULT 0,
  walkthrough_done INTEGER DEFAULT 0,
  updated_at TEXT DEFAULT (datetime('now'))
);
```

### Add: `~/.hermes/mathlms.db`
One consolidated file for dashboard-facing stats. The Python server reads this, not the app database.

```sql
CREATE TABLE IF NOT EXISTS pipeline_stats (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  metric TEXT,          -- 'topics_complete', 'gifs_rendered', 'questions_tagged', 'qa_pass_rate'
  value REAL,
  updated_at TEXT DEFAULT (datetime('now'))
);
```

---

## 3. Dashboard Tab Customisations

Follow the tutorial's 8-prompt UI build (Parts 07–14). At each prompt, swap the placeholder copy with
MathsLMS-specific content. Here is what to adapt per tab.

### Tab 1 — Overview (Part 09)
The tutorial shows a radar chart of agent activity distribution. For MathsLMS, the radar arms should be:

```
Curriculum · Animation · Problems · Tagger · QA · Deploy
```

Replace the "current directive" cycling text with your pipeline phases:
```
Phase 0 — Foundation · Phase 1 — IGCSE Content · Phase 2 — A Level · Phase 3 — Competition
```

VPS health metrics (CPU / RAM / disk bars) stay identical — Hostinger VPS exposes the same `/proc` endpoints.

Add one extra metric card: **Content Pipeline Progress** showing:
- Topics with concept scripts: X / 200
- GIFs rendered: X / 200
- Past papers tagged: X / 3000

### Tab 2 — Agents (Part 10 / 11)
Each agent card needs updated roles. In the dashboard prompt, provide this mapping:

```json
{
  "agents": [
    { "name": "Orchestrator", "role": "Pipeline coordinator", "model": "claude-opus-4-8", "channel": "telegram" },
    { "name": "Curriculum",   "role": "Concept scripts & IGCSE alignment", "model": "claude-sonnet-4-6", "channel": "#curriculum" },
    { "name": "Content",      "role": "JSON formatting & LaTeX", "model": "claude-sonnet-4-6", "channel": "#content" },
    { "name": "Animation",    "role": "Manim scripts & Canvas JS", "model": "claude-sonnet-4-6", "channel": "#animation" },
    { "name": "Problems",     "role": "Practice problem generation", "model": "claude-sonnet-4-6", "channel": "#problems" },
    { "name": "Tagger",       "role": "Past paper vision tagging", "model": "claude-haiku-4-5", "channel": "#tagger" },
    { "name": "Walkthrough",  "role": "Step-by-step solutions", "model": "claude-sonnet-4-6", "channel": "#walkthrough" },
    { "name": "QA",           "role": "Mathematical accuracy review", "model": "claude-sonnet-4-6", "channel": "#qa" },
    { "name": "Hints",        "role": "Socratic tutor (live)", "model": "claude-opus-4-8", "channel": "#hints" },
    { "name": "Deploy",       "role": "CI/CD & monitoring", "model": "claude-haiku-4-5", "channel": "#deploy" }
  ]
}
```

Paste this JSON into the Part 10 agent card prompt so the dashboard auto-generates all 10 cards.

### Tab 3 — Tasks (Kanban) (Part 12)
The tutorial's Kanban is for operator personal tasks. Keep that layer, but add a second board: **Content Pipeline Board**.

Columns:
```
Backlog → Scripting → Animating → QA Review → Live
```

Each card shows: topic ID, track (IGCSE / A Level / IMO), assigned agent, and blocker notes.

Tell the dashboard-building Claude agent:
> "Add a second Kanban board below the operator board titled 'Content Pipeline'. Pull cards from the `content_tasks` table in `~/.hermes/mathlms.db`. Columns: Backlog / Scripting / Animating / QA Review / Live. Card colour: violet for IGCSE, cyan for A Level, mint for IMO."

### Tab 4 — Schedule (Part 13)
Replace the generic cron descriptions with MathsLMS pipeline schedules:

```
Daily 02:00   — Manim render queue (render overnight, GIFs ready by morning)
Daily 03:00   — Past paper tagger batch (Haiku vision, 50 questions/run)
Daily 06:00   — QA Agent sweep (review yesterday's content)
Weekly Sun    — Content pipeline stats snapshot (topics_complete, gifs_rendered)
Monthly 1st   — agent-logs.db retention cleanup (delete > 90 days)
```

### Tab 5 — Content Library (Part 14)
This is the most important tab for MathsLMS. Adapt the content library to show:

**Folder structure** (mirrors `~/.hermes/content/`):
```
content/
  curriculum/      ← concept script JSONs from Curriculum agent
  animations/      ← Manim .py scripts from Animation agent
  problems/        ← problem set JSONs from Problems agent
  walkthroughs/    ← solution markdown from Walkthrough agent
  qa-reports/      ← flagged issues from QA agent
```

Tell the dashboard agent:
> "Organise the Content Library tab by agent folder. Show file count per folder. For files in `curriculum/`, render a preview of the `hook` field from the JSON. For `qa-reports/`, highlight files with `status: flagged` in red."

---

## 4. Hostinger VPS Setup

The tutorial is written for Contabo/RackNerd. Hostinger VPS uses the same Ubuntu base — all commands are
identical. The only differences are networking and the control panel.

### 4.1 Connect to Your VPS
```bash
ssh root@<your-hostinger-vps-ip>
```
Find your IP in Hostinger hPanel → VPS → Manage → Overview.

### 4.2 Install Hermes (same as tutorial)
Follow the tutorial's prerequisite: Hermes must be installed and running before the dashboard build.
If not installed yet, Hermes runs on Python stdlib with no pip packages needed.

```bash
# Verify Hermes is running
ls ~/.hermes/
# Should show: agent-logs.db  state.db  gateway_state.json
```

### 4.3 Dashboard Server Port
The tutorial runs the dashboard on `127.0.0.1:51763`. Keep that port — it is only accessible via SSH tunnel,
which is the secure approach.

If Hostinger's firewall blocks the port from external access (it should), that is correct behaviour.
Do not open port 51763 in the Hostinger firewall. Use the SSH tunnel instead (Section 4.5 below).

### 4.4 Verify Python is available
```bash
python3 --version
sqlite3 --version
```
Both ship with Hostinger Ubuntu VPS. No pip installs needed.

### 4.5 Remote Access from Your Windows Machine

**Option A — One-command SSH tunnel (recommended)**

Follow the tutorial's Part 15 steps for SSH key setup and desktop launchers. On Windows, create a PowerShell
script `mathsOS-connect.ps1` on your Desktop:

```powershell
# mathsOS-connect.ps1
# Opens SSH tunnel to Hostinger VPS and launches dashboard in browser

$VPS_IP = "YOUR_HOSTINGER_VPS_IP"
$VPS_USER = "root"
$LOCAL_PORT = "51763"
$REMOTE_PORT = "51763"

Write-Host "Connecting to MathsLMS dashboard..." -ForegroundColor Cyan

# Start SSH tunnel in background
Start-Process -NoNewWindow -FilePath "ssh" -ArgumentList "-N -L ${LOCAL_PORT}:127.0.0.1:${REMOTE_PORT} ${VPS_USER}@${VPS_IP}"

# Wait 2 seconds for tunnel to establish
Start-Sleep -Seconds 2

# Open browser
Start-Process "http://127.0.0.1:51763"

Write-Host "Dashboard open at http://127.0.0.1:51763" -ForegroundColor Green
Write-Host "Press Ctrl+C to close tunnel" -ForegroundColor Yellow

# Keep script alive
while ($true) { Start-Sleep -Seconds 60 }
```

Run it: right-click → Run with PowerShell.

**Option B — Tailscale mesh (tutorial Part 15, Step 3)**

If you want to access the dashboard from multiple devices without always running an SSH tunnel, install
Tailscale on the Hostinger VPS and your Windows machine. The tutorial walks through this in detail.

```bash
# On VPS
curl -fsSL https://tailscale.com/install.sh | sh
tailscale up

# Get your VPS Tailscale IP (e.g. 100.x.x.x)
tailscale ip -4
```

Then open `http://100.x.x.x:51763` directly from any device on your Tailscale network.

---

## 5. Backend Modifications (server.py)

The tutorial builds `server.py` in Part 06. When the agent writes your data functions, add these
MathsLMS-specific endpoints alongside the five standard Hermes ones.

Tell the Claude agent building your backend:
> "Add four additional data endpoints to server.py:
> 1. `GET /api/content-progress` — reads `content_tasks` table, returns counts grouped by stage and track
> 2. `GET /api/gif-queue` — reads `gif_renders` table, returns pending/rendering/done counts
> 3. `GET /api/past-paper-progress` — reads `past_paper_progress`, returns per-collection completion %
> 4. `GET /api/pipeline-stats` — reads `pipeline_stats`, returns all metric rows as key-value pairs
>
> All four use the same SQLite read-only pattern as the existing endpoints. Return JSON."

---

## 6. Logging Policy for MathsLMS Agents

The tutorial installs a silent logging script in Part 05. The log line format is:
```
agent_name | task_summary | status | model | timestamp
```

When you set up each MathsLMS agent (Parts 01–02 equivalent), include this additional logging rule in
every agent's operating instructions:

```
LOGGING RULE (MathsLMS extension):
After completing any content generation task, log to mathlms.db:
  INSERT INTO content_tasks (track, unit, topic_id, stage, status, agent)
  VALUES ('[track]', '[unit]', '[topic_id]', '[stage]', 'done', '[your_name]');
Run silently via the mathlms_log bash script. Never report this step to the user.
```

Create the logging helper at `~/.hermes/mathlms_log`:
```bash
#!/bin/bash
# Usage: mathlms_log TRACK UNIT TOPIC_ID STAGE STATUS AGENT
sqlite3 ~/.hermes/mathlms.db \
  "INSERT INTO content_tasks (track,unit,topic_id,stage,status,agent,updated_at) \
   VALUES ('$1','$2','$3','$4','$5','$6',datetime('now'));"
```

```bash
chmod +x ~/.hermes/mathlms_log
```

---

## 7. Content Library File Paths

MathsLMS content lives under `~/.hermes/content/` following the same convention as the tutorial, but
structured by agent and track:

```
~/.hermes/content/
  curriculum/
    igcse_o/          ← Track A concept JSONs
      A1_Number/
        2026-06-04_number-types.json
    a_level/          ← Track B
    imo/              ← Track C
  animations/
    igcse_o/          ← Manim .py files
    a_level/
    imo/
  gifs/
    igcse_o/          ← Rendered GIFs (before R2 upload)
  problems/
    igcse_o/
    a_level/
    imo/
  walkthroughs/
    o_level_4024/     ← Past paper walkthroughs
    igcse_0580/
    a_level_9709/
  qa-reports/
    2026-06-04_A2-algebra-review.md
```

File naming convention (same as tutorial): `YYYY-MM-DD_kebab-case-title.extension`

---

## 8. Phased Rollout Plan

Work through the Hermes tutorial in order, applying MathsLMS adaptations at each part.

| Tutorial Part | What to do |
|---|---|
| **Part 01 — Foundation** | Define Orchestrator with MathsLMS system prompt from Blueprint §4.4. Reference the 10-agent roster. |
| **Part 02 — Building Crew** | Create 9 specialist agents (not 4). Use agent prompts from Blueprint §4.4. |
| **Part 03 — Routing** | Natural-language routing: `@curriculum`, `@animation`, `@tagger`, etc. Add pipeline commands: `/generate-unit A2`, `/render-gifs A2`, `/qa-unit A2`. |
| **Part 04 — Discord** | Create 9 agent channels. Bind each agent. |
| **Part 05 — Activity Logging** | Install standard Hermes log + `mathlms_log` script (Section 6 above). |
| **Part 06 — Backend** | Build server.py with 5 Hermes endpoints + 4 MathsLMS endpoints (Section 5 above). |
| **Parts 07–14 — Dashboard UI** | Follow exactly; apply tab adaptations from Section 3 above. |
| **Part 15 — Remote Access** | Use Hostinger SSH tunnel script from Section 4.5 above. |
| **After Part 15** | Run a test unit: `/generate-unit A1` and watch the dashboard update in real time. |

---

## 9. First Content Run

Once the dashboard is live, trigger your first pipeline run and watch it on-screen:

```
# In Telegram to Orchestrator:
Generate all concept scripts for Unit A1: Number (IGCSE O Level).
Use the Curriculum agent prompt. Save outputs to ~/.hermes/content/curriculum/igcse_o/A1_Number/.
Log each completed topic to mathlms.db.
```

You should see:
- **Agents tab**: Curriculum agent activity count incrementing
- **Content Library tab**: new JSON files appearing under `curriculum/igcse_o/A1_Number/`
- **Tasks Kanban**: topic cards moving from Backlog → Scripting → done
- **Overview radar**: Curriculum arm lighting up

Then chain the next step:
```
For each JSON in ~/.hermes/content/curriculum/igcse_o/A1_Number/,
run the Animation agent. Produce Manim scripts in ~/.hermes/content/animations/igcse_o/A1_Number/.
Queue GIF renders. Log to mathlms.db.
```

---

## 10. Token Cost Reference (from Blueprint)

| Operation | Agent | Estimated cost |
|---|---|---|
| Full content generation (200 topics) | Sonnet | ~$80–120 |
| Past paper tagging (3000 questions, vision) | Haiku | ~$25 |
| Monthly live tutoring (200 students) | Sonnet + Opus | ~$150–300/month |
| GIF rendering | Manim (self-hosted) | Free |

The dashboard's Agents tab 7-day bar chart doubles as a cost tracker — each Sonnet call logged gives you
a proxy for token spend without needing to query the Anthropic billing API.

---

*mathsOS v1.0 · June 2026 · Built on Hermes AgentOS by komputermechanic.com*
