---
name: repo-organizer
description: >-
  Audits, restructures, and cleans messy GitHub repositories into high-conversion landing pages based on target audience and scenario.
  Includes Dual-Scope (Internal + External) Innovation Audits, Before/After Invariant Verification, Safe AST-Based Migration with Dry-Run & Rollback,
  Authentic Demo Asset Capture, and Evidence-Based README Interfaces across 8 Popular GitHub Archetypes.
  Use when the user asks to clean up root directory clutter, structure a repo for competition judges,
  prepare an academic paper release, build an open-source SDK layout, discover repository competitive edge, optimize README conversion, or fix broken links.
---

# 📦 Repository Reorganization & Competitive Edge Skill (`repo-organizer`)

This skill provides an enterprise-grade procedure for auditing, reorganizing, and polishing GitHub codebases into clean, safe, and **high-converting repository landing pages**.

> **Core Philosophy**: A GitHub repository is fundamentally a **Marketing Tool & Technical Landing Page**. Restructuring must guarantee **same semantics, better structure** while grounding all competitive edge claims in verifiable internal code evidence and external market comparisons.

---

## 🔬 1. External & Internal Innovation Audit System

Developers often lack objective awareness of their codebase's true technical differentiators. `repo-organizer` executes a dual-scope audit (Internal AST/Code Inspection + External Web/GitHub/arXiv Search) to discover true technical novelty.

> ⚠️ **STRICT RULE: PROHIBIT LLM-ONLY NOVELTY JUDGMENTS**  
> An agent MUST NOT declare a feature "novel" based solely on LLM training weights. Every claimed innovation MUST be validated against real SOTA repos/papers via external search.

```
[1. AST Code Audit] ──▶ [2. External Search (GitHub/arXiv)] ──▶ [3. Evidence Tuple Verification] ──▶ [4. Developer Audit Report]
```

### Structured Evidence Tuple Format
For EVERY identified competitive edge or novelty claim, the agent MUST format and output the following 5-part proof tuple:

```text
Claim        : <Target feature / architectural implementation claim>
Comparable   : <Existing SOTA repository, paper, or library found via search>
Difference   : <Exact technical delta / speedup / dependency advantage>
Evidence     : <Code snippet file:line, benchmark result CSV, or commit link>
Confidence   : <High | Medium | Low with explicit rationale>
```

### Audit Pipeline Steps:
1. **Internal Codebase Audit**: Parses AST, algorithms, custom data structures, JIT accelerations, zero-dependency modules, and memory patterns.
2. **External Market Search**: Executes searches (`search_web` / GitHub API) against comparable open-source repos and arXiv papers.
3. **Commodity Claim Filtering**: Filters out generic statements (*"Built with React"*, *"Uses AsyncIO"*).
4. **Developer Audit Report**: Outputs a private audit log (`.agents/reports/innovation_audit.md`) detailing confirmed edges, filtered commodity claims, and competitive gaps.

---

## 🛡️ 2. Before/After Invariant Verification System

Restructuring must NEVER break execution paths, import paths, or build pipelines. The primary objective is:

> **SAME SEMANTICS, BETTER STRUCTURE.**

### Pre-Migration Invariant Baseline
Before modifying any files or directories, automatically record a snapshot of the repository's **Invariant Baseline**:

| Invariant Category | Target Artifacts / Paths Captured |
| :--- | :--- |
| **README Links** | All relative markdown links (`[text](path)`), image tags, and anchor targets |
| **Python Imports** | Complete module dependency graph, internal package imports (`from .pkg import x`), `sys.path` references |
| **Entry Points** | `pyproject.toml`, `setup.py`, `package.json` scripts, `main.py`, CLI binaries |
| **CI Workflows** | `.github/workflows/*.yml` step execution paths, action scripts, path triggers |
| **Docker & Configs** | `Dockerfile`, `docker-compose.yml`, `.env.example`, JSON/YAML configuration file paths |
| **Build & Tests** | Test suites (`pytest`, `npm test`), build scripts (`make`, `python setup.py sdist`) |

### Post-Migration Verification
After restructuring, re-execute verification on all 6 invariant categories. If ANY invariant fails or returns a non-zero exit code, trigger the **Safe Migration Rollback Protocol**.

---

## 🛟 3. Safe AST-Based Migration Protocol (Dry-Run & Rollback)

All file movements, path updates, and directory reorganizations MUST follow a strict multi-phase safety pipeline.

```
[Phase 1: AST Path Analysis] ──▶ [Phase 2: Dry-Run Plan] ──▶ [Phase 3: Migration Execution] ──▶ [Phase 4: Invariant Audit & Rollback Guard]
```

### Phase 1: AST Dependency & Path Analysis
- **AST Import Audit**: Use Python AST parsing (`ast.parse()`) rather than superficial regex string replace to track all module import paths and symbol definitions.
- **Config & Resource Mapping**: Trace relative file IO paths (`open("config/settings.json")`) across the codebase.

### Phase 2: Migration Plan & Dry-Run
- Generate a explicit **Migration Plan** mapping `Source Path ──► Destination Path`.
- Perform a simulated dry-run to identify potential path collisions, circular imports, or broken relative references prior to disk modification.

### Phase 3: Execution & Link/Import Healing
- Execute file movements.
- Programmatically update AST import paths, relative Markdown links, CI workflow YAML steps, and configuration paths.

### Phase 4: Strict Halt & Rollback Protocol
- **Post-Migration Verification**: Run `git diff` sanity checks, AST import verification, link verification, and test execution.
- 🔴 **STRICT HALT RULE**: If any test, build, or invariant check fails post-migration:
  1. **STOP IMMEDIATELY**. Do NOT attempt hacky inline patches or force commits.
  2. Execute automatic rollback (`git reset --hard HEAD` / restore migration snapshot).
  3. Generate a diagnostic report explaining the exact failed invariant to the developer.

---

## 📊 4. Evidence-Based README Interface

Do not rely on superficial marketing fluff or generic hooks. `repo-organizer` structures README landing pages using an **Evidence-Based Information Architecture**:

> **What ──► Why ──► Evidence ──► How ──► Differentiator**

### Information Architecture Blueprint
1. **What**: Crisp 1-sentence definition of the repository and its core capability.
2. **Why**: Clear problem statement and target audience scenario alignment.
3. **Evidence**: Reproducible benchmark metrics, AST performance comparison tables, or verified external proof tuples (`Claim → Comparable → Difference → Evidence → Confidence`).
4. **How**: Zero-friction 1-line copy-paste quickstart command / reproduction script.
5. **Differentiator**: Concrete technical distinction vs. existing open-source solutions (backed by code line references).

Every claim in the **"✨ Key Innovations & Competitive Edge"** section MUST hyperlink directly to the authoritative source code file (`file:///src/core/solver.py#L45`), benchmark log, or external comparison reference.

---

## 📸 Visual Assets & Live Demo Capture Protocol

> ⚠️ **STRICT DIRECTIVE: NEVER USE AI-GENERATED VISUALS!**  
> All images, plots, and media in the repository MUST be authentic product artifacts:
> - **Product Screenshots**: Taken directly from running web apps / UI instances via browser subagent/tools.
> - **Data Plots**: Rendered directly from raw benchmark data, evaluation logs, or metrics using Python (`matplotlib`/`seaborn`/`plotly`).
> - **Terminal Demonstrations**: Recorded or transcribed from actual CLI command execution.
> - **Diagrams**: Native GitHub Mermaid diagrams (````mermaid ... ````) or standard vector SVGs.

### Demo Capture Procedure: When a Repo Lacks Visuals
1. **Web Apps & UI Services** (React, Streamlit, Gradio, Flask, FastAPI):
   - Launch or inspect active web server (`http://localhost:8501` or deployed URL).
   - Use browser automation to open app URL and capture clean product screenshot(s) to `docs/assets/demo-screenshot.png`.
2. **Data Science & ML Projects**:
   - Run evaluation scripts to produce real performance metrics.
   - Plot confusion matrices, loss curves, or accuracy comparisons using `matplotlib`/`seaborn` directly from output CSVs/logs.
3. **CLI Tools & Open-Source Libraries**:
   - Run sample commands in terminal and record authentic ANSI execution blocks.
   - Render architecture diagrams using native Markdown Mermaid blocks.

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

### Step 1: Pre-Migration Invariant Baseline Capture
Automatically discover and record all 6 invariant categories (README links, AST imports, entry points, CI workflows, docker/configs, test commands).

### Step 2: Dual-Scope Innovation Audit (Internal AST + External Search)
Execute AST code analysis and web/GitHub search. Generate structured proof tuples (`Claim → Comparable → Difference → Evidence → Confidence`) for confirmed technical edges.

### Step 3: Migration Plan & AST Dry-Run
Build source-to-destination map, perform AST import analysis, and dry-run migration to detect path collisions.

### Step 4: Root Audit & Junk Cleanup
Identify loose files at root level (`.png`, `.csv`, `.log`, `__pycache__`) and organize or gitignore them safely.

### Step 5: Directory Restructuring & Safe File Migration
Move files according to selected archetype. Programmatically update AST imports, relative Markdown links, CI steps, and config paths.

### Step 6: Invariant Re-Verification & Rollback Guard
Run link audit, AST import verification, test suites, and `git diff` sanity check. **If any test or invariant fails, halt immediately and trigger rollback.**

### Step 7: Evidence-Based README Interface & Asset Protocol
Construct README following **What → Why → Evidence → How → Differentiator**. Ensure all visual assets are authentic browser screenshots or real data plots (NO AI visuals).

### Step 8: `.gitignore` Hardening & Git Sync
Ensure `.gitignore` excludes temporary lock files and cache. Commit with message: `refactor: reorganize repository structure to [Archetype] standard`.

---

## 📋 Reorganization & Edge Checklist

- [ ] Invariant Baseline captured across all 6 categories prior to migration.
- [ ] Dual-Scope Innovation Audit completed with external search (NO LLM-only novelty claims).
- [ ] All competitive edge claims formatted as structured proof tuples (`Claim → Comparable → Difference → Evidence → Confidence`).
- [ ] AST-based dependency analysis and migration dry-run executed.
- [ ] Invariant re-verification passed (links, AST imports, entry points, CI workflows, tests).
- [ ] Rollback protocol verified in case of verification failure (same semantics, better structure).
- [ ] README structured via Evidence Interface (**What → Why → Evidence → How → Differentiator**).
- [ ] Authentic demo screenshot captured from running app OR real data plot generated (NO AI visuals).
- [ ] Root directory contains ONLY essential entry files (`README.md`, `main.py`, `requirements.txt`, `LICENSE`, `.gitignore`).
