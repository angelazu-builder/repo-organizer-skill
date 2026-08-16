---
name: repo-organizer
description: >-
  Audits, restructures, and cleans messy GitHub repositories into high-conversion landing pages based on target audience and scenario.
  Includes automated Competitive Edge & Novelty Identification, Developer Feedback Loop, and 8 Popular GitHub Archetypes.
  Use when the user asks to clean up root directory clutter, structure a repo for competition judges,
  prepare an academic paper release, build an open-source SDK layout, discover repository competitive edge, optimize README conversion, or fix broken links.
---

# 📦 Repository Reorganization & Competitive Edge Skill (`repo-organizer`)

This skill provides a systematic procedure for analyzing, reorganizing, and polishing GitHub codebases into clean, professional, and **high-converting repository landing pages**.

> **Core Philosophy**: A GitHub repository is fundamentally a **Marketing Tool & Landing Page**. Beyond clean code structure, it must highlight the project's **true competitive edge over existing GitHub projects** and convert casual visitors into stars, users, and contributors within 3 seconds.

---

## 💎 Killer Feature: Agent Innovation Audit & Competitive Edge Identifier

Developers often lack objective self-awareness of their repository's true strengths. They frequently highlight commodity features ("Built with React", "Uses AsyncIO") while missing their **genuine unfair technical advantage**.

This skill performs a 4-step **Competitive Edge & Developer Feedback Loop**:

```
[1. Deep Codebase Audit] ──▶ [2. Market Novelty Mapping] ──▶ [3. README "✨ Key Edge" Injection] ──▶ [4. Developer Feedback Report]
```

### 1. Codebase Novelty Audit
Scans algorithms, data structures, JIT accelerations, dependency footprints, and workflow combinations.

### 2. Market Novelty Mapping (Commodity vs. Edge)
- **Commodity Features** (Commonplace, low-value to highlight): Using standard frameworks, basic REST APIs, standard logging.
- **Unfair Competitive Edge** (True innovation): First zero-dependency implementation, unconfounded 1D phase transition scanner with finite-size scaling, local-first isolated IPC security.

### 3. README "✨ Key Innovations & Competitive Edge" Injection
Injects a crisp, high-impact highlight box right below the 3-second hook in `README.md`.

### 4. Developer Feedback Report
Outputs a private **"Agent Innovation Audit Report"** for the creator:
- 🟢 **Genuinely Novel Innovations**: Features unique across GitHub.
- 🟡 **Over-Estimated Commodity Features**: Commonplace functions that shouldn't waste prime README real estate.
- 🔴 **Competitive Gaps vs. SOTA Repos**: Suggestions for future roadmap iterations.

---

## 🏛️ 8 Popular GitHub Repository Archetypes

Identify the **primary target audience and scenario** with the user:

### Archetype 1: Competition & Hackathon (`competition-research`)
- **Target Audience**: Competition Judges (want `.docx`/PPT deliverables), Technical Reviewers (want methodology logbooks), Developers (want CLI script).
- **Structure**: `docs/submission/`, `docs/logbook/`, `docs/references/`, `outputs/`, `notebooks/`, `main.py`.

### Archetype 2: Academic Paper Release (`paper-release`)
- **Target Audience**: AI/Physics Researchers & Peer Reviewers.
- **Goal**: **Minimal friction to reproduce** (Zero cognitive overhead).
- **Structure**: `README.md` (Abstract + Paper link), `run_eval.py` (Flat 1-line script), `src/`, `weights/`, `scripts/`.

### Archetype 3: Open-Source Package / Tool (`open-source-library`)
- **Target Audience**: External Software Developers & Package Maintainers.
- **Structure**: `pyproject.toml`, `src/pkg_name/`, `tests/`, `docs/`, `examples/`.

### Archetype 4: Data Science & ML Pipeline (`data-science-pipeline`)
- **Target Audience**: Data Scientists & ML Engineers.
- **Structure**: `data/` (raw/processed), `models/`, `notebooks/`, `src/`, `reports/figures/`.

### Archetype 5: AI Agent Skill / MCP Server (`agent-skill-mcp`)
- **Target Audience**: AI Agent Developers (Antigravity, Cursor, Claude MCP, Copilot).
- **Structure**: `SKILL.md` / `mcp_config.json`, `.agents/skills/`, `plugin.json`, `examples/`.

### Archetype 6: Curated Awesome List (`curated-awesome-list`)
- **Target Audience**: Community Developers seeking organized topic resources.
- **Structure**: Categorized `README.md` TOC, Badge matrix, strict `CONTRIBUTING.md`.

### Archetype 7: Full-Stack Web App / Starter (`fullstack-web-app`)
- **Target Audience**: Web Developers & SaaS Founders.
- **Structure**: `frontend/`, `backend/`, `docker-compose.yml`, `.env.example`, `npm run dev`.

### Archetype 8: CLI Utility Binary (`cli-binary-tool`)
- **Target Audience**: System Administrators & DevOps Engineers.
- **Structure**: Terminal UI GIF, package manager install (`brew install`), Flag cheat-sheet table.

---

## 🛠️ Step-by-Step Execution Workflow

### Step 1: Innovation Audit & Edge Identification
Scan the codebase to generate the **Developer Feedback Report** (distinguishing true novelty vs. commodity features).

### Step 2: Root Audit & Junk Cleanup
Identify loose files sitting at root level:
- **Image Artifacts**: `*.png`, `*.jpg`, `*.svg` (Move to `outputs/` or `reports/figures/`)
- **Data & Logs**: `*.csv`, `*.json`, `*.log` (Move to `outputs/` or `data/`)
- **Junk/Temp Files**: `__pycache__/`, `.DS_Store`, `.~lock*`, `*.tmp`, `*.zip` (Delete or `.gitignore`)

### Step 3: Directory Hierarchy Creation
Create clean target subdirectories based on chosen archetype from the 8 options.

### Step 4: Safe File Migration & Renaming
Move files and rename deliverables cleanly (`01_Problem_Definition.docx`, `02_Final_Report.docx`).

### Step 5: Markdown Link & Python Path Auditing
Audit and update all relative Markdown links (`![alt](path)`) and Python relative imports (`sys.path`).

### Step 6: High-Conversion README & Edge Injection
- Insert **3-Second Hook Rule**.
- Insert **✨ Key Innovations & Competitive Edge Section**.
- Insert **Above-the-Fold Visual Hero Asset (GIF/Diagram)**.
- Insert **Single-Line Copy-Paste Quickstart Command**.

### Step 7: `.gitignore` Hardening & Git Sync
- Ensure `.gitignore` excludes `__pycache__`, `.DS_Store`, and temporary lock files.
- Commit with git message: `refactor: reorganize repository structure to [Archetype] standard`.

---

## 📋 Reorganization & Edge Checklist

- [ ] Agent Innovation Audit executed & Feedback Report delivered to creator.
- [ ] README contains 3-second hook, ✨ Key Edge Section, visual asset, and 1-line quickstart.
- [ ] Selected archetype matches 1 of the 8 GitHub popular scenarios.
- [ ] Root directory contains ONLY essential entry files (`README.md`, `main.py`, `requirements.txt`, `LICENSE`, `.gitignore`).
- [ ] All relative Markdown links (`![alt](path)`) resolve to valid existing files.
- [ ] Python imports run cleanly without `ImportError`.
