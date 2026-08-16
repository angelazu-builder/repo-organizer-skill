---
name: repo-organizer
description: >-
  Audits, restructures, and cleans messy GitHub repositories based on target audience and scenario.
  Use when the user asks to clean up root directory clutter, structure a repo for competition judges,
  prepare an academic paper release, build an open-source SDK layout, or fix broken markdown links after file moves.
---

# 📦 Repository Reorganization & Audience Alignment Skill (`repo-organizer`)

This skill provides a systematic procedure for analyzing, reorganizing, and polishing messy GitHub codebases into clean, professional, and audience-aligned repository architectures.

---

## 🎯 User Pain Points Solved

1. **Root Directory Clutter**: Prototyping leaves loose `.png` plots, `.csv`/`.json` logs, and temporary lock files in the root.
2. **Audience Mismatch**: A competition project, an academic paper release, and an open-source SDK require completely different repository structures.
3. **Broken Relative Links**: Manually moving files breaks Markdown image embeds (`![alt](path)`), doc links, and Python relative imports (`sys.path`).
4. **Git Artifact Leaks**: Missing `.gitignore` entries cause `__pycache__`, `.DS_Store`, and `.~lock*` files to pollute GitHub commits.

---

## 🏛️ Repository Archetype Selector

Before moving any files, identify the **primary target audience and scenario** with the user:

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

### Archetype 3: Open-Source Python Package (`open-source-library`)
- **Target Audience**: External Software Developers & Package Maintainers.
- **Structure**:
  ```
  root/
  ├── README.md                  # PyPI badge, installation, quickstart code
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

### Step 5: Navigation & Index Guide Generation
- Add a **Quick Navigation Menu** at the top of `README.md`.
- Add a mini `docs/README.md` guiding different audience types to their target folders.
- Add an `outputs/README.md` listing figure schemas and data logs.

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
- [ ] Root directory contains ONLY essential entry files (`README.md`, `main.py`, `requirements.txt`, `LICENSE`, `.gitignore`).
- [ ] No loose PNGs, CSVs, or JSONs sitting in root.
- [ ] `docs/` is partitioned by audience/purpose with a guide `docs/README.md`.
- [ ] `outputs/` contains a figure/data index `outputs/README.md`.
- [ ] All relative Markdown links (`![alt](path)`) resolve to valid existing files.
- [ ] All Python imports in scripts and notebooks run without `ImportError` or `FileNotFoundError`.
- [ ] `.gitignore` excludes temporary lock files and python bytecode.
