---
name: repo-organizer
description: >-
  Audits, restructures, and cleans messy GitHub repositories into high-conversion landing pages based on target audience and scenario.
  Features an Evidence-Backed Architecture: Explicit Tool Stack Matrix (git, GitHub REST/GraphQL API, OpenAlex/arXiv, AST, Tree-sitter),
  Built-in Executable Deterministic Scripts (`scripts/`), 3-Layer External Novelty Audit (GitHub -> arXiv -> Web), Deterministic Invariant Baseline,
  AST Safe Migration Pipeline with Dry-Run & Rollback, Authentic Demo Asset Capture, and Evidence-Based README Interfaces across 8 Popular GitHub Archetypes.
  Use when the user asks to clean up root directory clutter, structure a repo for competition judges,
  prepare an academic paper release, build an open-source SDK layout, discover repository competitive edge, optimize README conversion, or fix broken links.
---

# 📦 Repository Reorganization & Competitive Edge Skill (`repo-organizer`)

This skill provides an enterprise-grade procedure for auditing, reorganizing, and polishing GitHub codebases into clean, safe, and **high-converting repository landing pages**.

> **Core Philosophy & System Positioning**: `repo-organizer` is NOT just a prompt that writes pretty READMEs; it is an **Evidence-Backed Repository Transformation Agent**. All competitive edge claims must originate from deterministic local parser scans and external API evidence before LLM synthesis.

---

## 🛠️ Concrete Built-in Tool Scripts (`scripts/`)

This skill includes executable Python scripts in `scripts/` to perform deterministic analysis, invariant tracking, dry-runs, and rollback:

| Script Path | CLI Invocation | Purpose & Capabilities |
| :--- | :--- | :--- |
| **[`scripts/invariant_checker.py`](scripts/invariant_checker.py)** | `python3 scripts/invariant_checker.py [snapshot\|verify]` | Captures & verifies 6-domain invariant baseline (links, AST imports, entry points, CI workflows) |
| **[`scripts/ast_import_analyzer.py`](scripts/ast_import_analyzer.py)** | `python3 scripts/ast_import_analyzer.py` | AST tree parsing of Python module import dependencies & broken relative references |
| **[`scripts/safe_migrate.py`](scripts/safe_migrate.py)** | `python3 scripts/safe_migrate.py --plan plan.json [--dry-run]` | Dry-run validation, atomic `git mv` file relocations, and automatic `git reset` rollback on failure |
| **[`scripts/external_novelty_search.py`](scripts/external_novelty_search.py)** | `python3 scripts/external_novelty_search.py` | Queries GitHub Search API & arXiv API to retrieve comparable repos/papers & format proof tuples |

---

## 🏛️ Golden Architectural Hierarchy

To prevent hallucinations and guarantee filesystem safety, the agent MUST enforce this execution hierarchy:

```text
                  LLM (Interpretation / Synthesis / Plan Proposal)
                             ┌─────────┴─────────┐
                             ▼                   ▼
           Web / APIs / Search           Local Analyzers & Parsers
            (External Evidence)             (Code / Filesystem)
                             │                   │
                             └─────────┬─────────┘
                                       ▼
                            Deterministic Verification Checks (Git / AST / Parsers / Tests)
                                       ▼
                                  Final Action
```

---

## 🛠️ Mandatory Tool Stack Matrix

Never rely on LLM internal weights alone. Match every sub-task to its deterministic tool/API:

| Task / Domain | Primary Tool / API | Specific Purpose & Method |
| :--- | :--- | :--- |
| **Repo & Version Info** | `git` / `gh` CLI | `git clone`, `commit`, `diff`, `branch`, `history`, `git ls-files` |
| **GitHub Metadata** | GitHub REST / GraphQL API (`gh api`) | Retrieve repo metadata, languages, topics, stars, forks, contributors |
| **GitHub External Search** | `scripts/external_novelty_search.py` | Query GitHub Search API (`code search`, `repository search`) for top 5–10 real comparable implementations |
| **Code-level Novelty** | `scripts/ast_import_analyzer.py` / `ast` | Extract algorithms, data structures, custom workflows (No LLM guessing!) |
| **Academic Novelty** | OpenAlex API + arXiv API | Search papers, mechanisms, comparable algorithms, publication timestamps |
| **Web / Product Competitors**| `search_web` / HTTP | Search official product sites, blogs, benchmarks, company implementations |
| **Markdown Link Audit** | `scripts/invariant_checker.py` | Parse relative Markdown links and verify file existence and URL HTTP status |
| **Python Import Audit** | `scripts/ast_import_analyzer.py` | AST tree parsing of module dependencies and import statements (No regex guessing!) |
| **JS/TS Import Audit** | `Tree-sitter` / TS Compiler API | Parse module import trees and export dependencies for JavaScript/TypeScript |
| **YAML / CI Audit** | `PyYAML` / YAML Parsers | Inspect `.github/workflows/*.yml` step paths and environment variables |
| **Package Scripts** | JSON / TOML Parsers | Parse `package.json`, `pyproject.toml`, `Cargo.toml` entry points and scripts |
| **Dependency Graph** | Native Package Managers | `npm`/`pnpm`, `uv`/`poetry`/`pip`, `cargo` dependency resolution |
| **Test/Build Verification** | Native Repo Commands | Execute `pytest`, `npm test`, `cargo test`, `make` to verify runtime integrity |
| **Diff Sanity Check** | `git diff --check` + `git diff` | Verify whitespace, path changes, and code diffs before final commit |
| **Migration Execution** | `scripts/safe_migrate.py` (`git mv`) | Perform atomic, trackable, and safe file relocations |
| **Rollback Guard** | `git reset` / Git Worktree | Instantly restore baseline on test or invariant failure |

---

## 🔬 1. 3-Layer External Novelty Audit Protocol

> ⚠️ **STRICT EXECUTION ORDER: EVIDENCE ──► MODEL JUDGMENT**  
> The agent MUST collect hard search evidence first via `scripts/external_novelty_search.py`, then synthesize. Never let the LLM guess novelty from memory and find evidence backwards.

```
[Layer A: GitHub Search API] ──► [Layer B: OpenAlex & arXiv API] ──► [Layer C: Web Product Search] ──► [LLM Synthesis & Proof Tuple]
```

### Layer A: GitHub Search API (`gh api /search/repositories` & `gh api /search/code`)
- Query GitHub API for exact keywords, topic tags, and code AST patterns.
- Retrieve the top 5–10 real comparable implementations.

### Layer B: Academic Papers (OpenAlex API + arXiv API)
- Query OpenAlex and arXiv APIs for core technical keywords and algorithms.
- **LLM Restriction**: The LLM MUST NOT state *"This is novel."* It MUST state: *"Based on OpenAlex/arXiv API search, I found / did not find comparable work."*

### Layer C: Web & Product Search (`search_web`)
- Search official product documentations, tech blogs, and benchmark reports.

### Structured Evidence Proof Tuple
For EVERY identified feature or innovation, output the 6-part proof tuple:

```text
Claim        : <Target feature / implementation claim>
Comparable   : <SOTA repository, paper, or library reference retrieved via API>
Similarity   : <Matched mechanism or algorithmic structure>
Difference   : <Exact technical delta / memory / zero-dependency advantage>
Evidence     : <File path:line number or raw benchmark CSV output>
Confidence   : <verified | supported | plausible | unsupported>
```

---

## 🛡️ 2. Before/After Invariant Verification System

Restructuring must NEVER alter execution semantics. The strict core objective is:

> **SAME SEMANTICS, BETTER STRUCTURE.**

### Deterministic Baseline Tracking (`scripts/invariant_checker.py`)
Before moving files, automatically construct a baseline using `python3 scripts/invariant_checker.py snapshot`:

| Invariant Category | Local Parser / Script Used | Target Baseline Elements |
| :--- | :--- | :--- |
| **README Links** | `scripts/invariant_checker.py` | All relative links (`[text](path)`), image tags, anchor targets |
| **Python Imports** | `scripts/ast_import_analyzer.py` | Full AST module import tree (`from .pkg import x`), `sys.path` references |
| **JS/TS Imports** | `Tree-sitter` / TS Compiler API | Module import/export graph for `.js`, `.ts`, `.jsx`, `.tsx` |
| **Entry Points** | `scripts/invariant_checker.py` | `package.json` scripts, `pyproject.toml`, `main.py`, CLI binaries |
| **CI Workflows** | `scripts/invariant_checker.py` | `.github/workflows/*.yml` step paths and environment references |
| **Docker & Configs**| `scripts/invariant_checker.py` | `Dockerfile`, `docker-compose.yml`, configuration file paths |
| **Tests & Builds** | `subprocess` + Native Commands | Test suites (`pytest`, `npm test`) & build scripts (`make`) |

Post-migration, re-run `python3 scripts/invariant_checker.py verify`. If ANY invariant fails, trigger the **Safe Migration Rollback Protocol**.

---

## 🛟 3. Safe Migration Pipeline (`scripts/safe_migrate.py`)

The LLM is responsible for proposing migration plans, but **DOES NOT have unguided filesystem authority**.

```text
LLM ↓ 
Propose Migration Plan ↓ 
scripts/safe_migrate.py --plan plan.json --dry-run ↓ 
Human/Agent Approval ↓ 
scripts/safe_migrate.py --plan plan.json ↓ 
Tests & Invariant Verification ↓ 
[Pass: Final Commit] OR [Fail: Automatic Git Reset Rollback]
```

### Safety Rules:
1. **AST & Path Validation**: Verify that file relocations map cleanly to updated import paths without circular dependencies.
2. **Dry-Run**: Output a simulation of file movements (`Source ──► Destination`) before disk modification (`--dry-run`).
3. **Execution**: File relocations MUST be performed via `scripts/safe_migrate.py` (`git mv`) for atomic git history tracking.
4. **Strict Halt & Rollback**: If tests fail post-migration, execute immediate rollback (`git reset --hard HEAD`).

---

## 📊 4. Evidence-Based README Interface

Construct README landing pages using an **Evidence-Based Information Architecture**:

$$\text{What} \longrightarrow \text{Why} \longrightarrow \text{Evidence} \longrightarrow \text{How} \longrightarrow \text{Differentiator}$$

| Section | Content Origin | Generation Rule |
| :--- | :--- | :--- |
| **What** | LLM Synthesis | Crisp 1-sentence product definition |
| **Why** | LLM Synthesis | Clear problem statement & target scenario alignment |
| **Evidence** | **Machine Scan / Tests / Benchmarks** | Benchmark metrics, test outputs, AST stats (No LLM fluff!) |
| **How** | System / Code Inspection | Zero-friction 1-line reproduction / quickstart script |
| **Differentiator** | **API Search + AST Proof Tuples** | Technical distinction hyperlinked to code lines (`src/core/solver.py#L45`) |
| **Confidence** | **Deterministic Auditor** | Categorized as `verified`, `supported`, `plausible`, or `unsupported` |

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

### Step 1: Deterministic Baseline Capture
Run `python3 scripts/invariant_checker.py snapshot` to record the 6-domain Invariant Baseline.

### Step 2: 3-Layer Novelty Audit (GitHub API ──► OpenAlex/arXiv ──► Web Search)
Run `python3 scripts/external_novelty_search.py` and query GitHub Search API, OpenAlex/arXiv API, and `search_web`. Output structured proof tuples (`Claim → Comparable → Similarity → Difference → Evidence → Confidence`).

### Step 3: Migration Plan & AST Dry-Run Validation
LLM proposes migration plan. Run `python3 scripts/ast_import_analyzer.py` and `python3 scripts/safe_migrate.py --plan plan.json --dry-run`.

### Step 4: Root Audit & Junk Cleanup
Identify loose files at root level (`.png`, `.csv`, `.log`, `__pycache__`) and organize or gitignore them safely.

### Step 5: Safe Migration Execution (`scripts/safe_migrate.py`)
Execute file movements via `python3 scripts/safe_migrate.py --plan plan.json`. Programmatically update AST imports, relative Markdown links, CI steps, and config paths.

### Step 6: Invariant Re-Verification & Rollback Guard
Run `python3 scripts/invariant_checker.py verify` and `git diff --check`. **If any test or invariant fails, trigger immediate `git reset` rollback.**

### Step 7: Evidence-Based README Interface & Asset Protocol
Construct README following **What → Why → Evidence → How → Differentiator**. Ensure all visual assets are authentic browser screenshots or real data plots (NO AI visuals).

### Step 8: `.gitignore` Hardening & Git Sync
Ensure `.gitignore` excludes temporary lock files and cache. Commit with message: `refactor: reorganize repository structure to [Archetype] standard`.

---

## 📋 Reorganization & Edge Checklist

- [ ] Executed built-in scripts (`scripts/invariant_checker.py`, `scripts/ast_import_analyzer.py`, `scripts/safe_migrate.py`, `scripts/external_novelty_search.py`).
- [ ] Invariant Baseline captured prior to migration using `python3 scripts/invariant_checker.py snapshot`.
- [ ] 3-Layer Novelty Audit completed with external search (`python3 scripts/external_novelty_search.py`).
- [ ] All competitive edge claims formatted as proof tuples with confidence (`verified | supported | plausible | unsupported`).
- [ ] Migration plan validated by AST analyzer and executed via `scripts/safe_migrate.py`.
- [ ] Invariant re-verification passed (`python3 scripts/invariant_checker.py verify`).
- [ ] Automatic rollback guard verified in case of test failure (same semantics, better structure).
- [ ] README structured via Evidence Interface (**What → Why → Evidence → How → Differentiator**).
- [ ] Authentic demo screenshot captured from running app OR real data plot generated (NO AI visuals).
- [ ] Root directory contains ONLY essential entry files (`README.md`, `main.py`, `requirements.txt`, `LICENSE`, `.gitignore`).
