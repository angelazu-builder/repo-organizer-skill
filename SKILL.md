---
name: repo-organizer
description: >-
  Audits, restructures, and cleans messy GitHub repositories into high-conversion landing pages based on target audience and scenario.
  Use when the user asks to clean up root directory clutter, structure a repo for competition judges,
  prepare an academic paper release, build an open-source SDK layout, optimize GitHub README conversion, or fix broken markdown links.
---

# 📦 Repository Reorganization & Marketing Conversion Skill (`repo-organizer`)

This skill provides a systematic procedure for analyzing, reorganizing, and polishing GitHub codebases into clean, professional, and **high-converting repository landing pages**.

> **Core Philosophy**: A GitHub repository is fundamentally a **Marketing Tool & Landing Page**. Beyond clean code structure, it must convert casual visitors into stars, users, and contributors within 3 seconds.

---

## 🎯 User Pain Points Solved

1. **Root Directory Clutter**: Prototyping leaves loose `.png` plots, `.csv`/`.json` logs, and temporary lock files in the root.
2. **Audience Mismatch**: A competition project, an academic paper release, and an open-source SDK require completely different repository structures.
3. **Low GitHub Conversion Rate**: Great tech with poor README marketing fails to gain traction or stars.
4. **Broken Relative Links**: Manually moving files breaks Markdown image embeds (`![alt](path)`), doc links, and Python relative imports (`sys.path`).
5. **Git Artifact Leaks**: Missing `.gitignore` entries cause `__pycache__`, `.DS_Store`, and `.~lock*` files to pollute GitHub commits.

---

## 🚀 GitHub Landing Page Conversion Rate Optimization (CRO)

Every reorganized repository MUST implement these 5 high-conversion landing page elements:

1. **The 3-Second Hook Rule**: A bold 1-sentence value proposition right under the title explaining *what pain it solves instantly*.
2. **Above-the-Fold Visual Hero Asset**: A high-impact 10-second Demo GIF, video screenshot, or clean architecture diagram placed immediately before deep technical text.
3. **Zero-Friction Quickstart Command**: Single copy-paste execution command (`pip install ...`, `npx ...`, `docker run ...`) placed before detailed documentation.
4. **Comparison Matrix ("Why Us?")**: A clean table contrasting your solution against existing alternatives.
5. **Social Card Guidelines (Open Graph)**: Recommendations for setting up a `1200x630` PNG image for GitHub Social Preview when shared on Twitter/X or LinkedIn.

---

## 🏛️ Repository Archetype Selector

Identify the **primary target audience and scenario** with the user:

### Archetype 1: Competition & Hackathon (`competition-research`)
- **Target Audience**: Competition Judges (want `.docx`/PPT deliverables), Technical Reviewers (want methodology logbooks), Developers (want CLI script).
- **Structure**:
  ```
  root/
  ├── README.md                  # Quick navigation + embedded visual results
  ├── main.py                    # Unified CLI runner
  ├── src/                       # Core python package
  ├── docs/                      # Multi-audience documentation hub
  │   ├── submission/            # Official deliverables for judges
  │   ├── logbook/               # Research trajectory & iteration logs
  │   └── references/            # Background PDFs, PPTs, templates
  ├── outputs/                   # Figures & data logs
  └── notebooks/                 # Interactive Jupyter demos
  ```

### Archetype 2: Academic Paper Release (`paper-release`)
- **Target Audience**: AI/Physics Researchers & Peer Reviewers.
- **Goal**: **Minimal friction to reproduce** (Zero cognitive overhead).
- **Structure**:
  ```
  root/
  ├── README.md                  # Abstract, Paper Link, Single-line evaluation command
  ├── run_eval.py / main.py      # Flat, 1-command replication script
  ├── requirements.txt
  ├── src/                       # Core algorithm modules
  ├── weights/ / checkpoints/    # Pretrained model weights
  └── scripts/                   # Shell scripts for multi-GPU training/eval
  ```

### Archetype 3: Open-Source Python Package / Tool (`open-source-library`)
- **Target Audience**: External Software Developers & Package Maintainers.
- **Structure**:
  ```
  root/
  ├── README.md                  # PyPI badge, 3-sec hook, 1-line install, quickstart
  ├── pyproject.toml / setup.py
  ├── src/pkg_name/              # Package module
  ├── tests/                     # Pytest suite
  ├── docs/                      # Sphinx / MkDocs documentation
  └── examples/                  # Standalone usage scripts
  ```

### Archetype 4: Data Science & ML Pipeline (`data-science-pipeline`)
- **Target Audience**: Data Scientists & ML Engineers.
- **Structure**:
  ```
  root/
  ├── README.md                  # Pipeline overview & data pipeline DAG
  ├── data/                      # raw/, processed/, external/
  ├── models/                    # Serialized model artifacts (.pkl, .onnx)
  ├── notebooks/                 # Exploratory notebooks with sequential prefixes
  ├── src/                       # Data processing, training & feature engineering
  └── reports/figures/           # Publication plots
  ```

---

## 🛠️ Step-by-Step Execution Workflow

### Step 1: Root Audit & Junk Identification
Identify loose files sitting at root level:
- **Image Artifacts**: `*.png`, `*.jpg`, `*.svg` (Move to `outputs/` or `reports/figures/`)
- **Data & Logs**: `*.csv`, `*.json`, `*.log` (Move to `outputs/` or `data/`)
- **Junk/Temp Files**: `__pycache__/`, `.DS_Store`, `.~lock*`, `*.tmp`, `*.zip` (Delete or `.gitignore`)

### Step 2: Directory Hierarchy Creation
Create clean target subdirectories based on chosen archetype (e.g. `docs/submission/`, `docs/logbook/`, `docs/references/`, `outputs/`).

### Step 3: Safe File Migration & Renaming
- Move files to their designated directories.
- Give submission deliverables clean, ordered names (e.g., `01_Problem_Definition.docx`, `02_Final_Report.docx`).

### Step 4: Markdown Link & Python Path Auditing
After moving files, **immediately audit and update**:
1. **Markdown Links**: Scan all `.md` files for relative links (`[text](url)` and `![alt](path)`). Update paths to point to new subfolder locations.
2. **Python Imports**: In scripts and `.ipynb` notebooks, ensure `sys.path.insert(0, os.path.abspath('..'))` or `from src import ...` is correctly configured.

### Step 5: High-Conversion README Generation
- Add **Status Badges** (License, Python Version, PRs Welcome).
- Insert **3-Second Value Proposition**.
- Insert **Visual Hero Asset (GIF/Diagram)**.
- Insert **Single-Line Copy-Paste Quickstart Command**.
- Add a **Quick Navigation Menu** for multi-folder repos.

### Step 6: `.gitignore` Hardening
Ensure `.gitignore` contains:
```gitignore
__pycache__/
*.py[cod]
.DS_Store
.~*
*.tmp
*.zip
.vscode/
.idea/
```

### Step 7: Verification & Git Sync
- Run main execution scripts (`python main.py --mode full`) to verify 0 path errors.
- Run a link checker script to ensure 100% valid relative Markdown links.
- Stage and commit with clean git message: `refactor: reorganize repository structure to [Archetype] standard`.

---

## 📋 Reorganization Checklist

- [ ] Chosen repository archetype matches target audience & scenario.
- [ ] README includes 3-second hook, visual asset (GIF/diagram), and 1-line quickstart.
- [ ] Root directory contains ONLY essential entry files (`README.md`, `main.py`, `requirements.txt`, `LICENSE`, `.gitignore`).
- [ ] No loose PNGs, CSVs, or JSONs sitting in root.
- [ ] `docs/` is partitioned by audience/purpose with a guide `docs/README.md`.
- [ ] `outputs/` contains a figure/data index `outputs/README.md`.
- [ ] All relative Markdown links (`![alt](path)`) resolve to valid existing files.
- [ ] All Python imports in scripts and notebooks run without `ImportError` or `FileNotFoundError`.
- [ ] `.gitignore` excludes temporary lock files and python bytecode.
