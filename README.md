# 📦 repo-organizer-skill

> **AI Agent Skill for automatically auditing, restructuring, and cleaning messy GitHub repositories based on audience and scenario.**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.8%2B-green.svg)](https://www.python.org/)
[![Antigravity](https://img.shields.io/badge/Antigravity-Agent%20Skill-blue.svg)](https://github.com/angelazu-builder/repo-organizer-skill)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

---

## 💡 Why `repo-organizer`?

When prototyping code, writing papers, or entering hackathons, root directories inevitably accumulate loose `.png` plots, `.csv`/`.json` logs, and temporary lock files.

However, **there is no one-size-fits-all repository structure**:
- **Competition Judges** want structured Word/PPT deliverables in a clear submission folder.
- **Academic Researchers** want flat, minimal-friction scripts (`python run_eval.py`).
- **Software Engineers** want modular Python packages (`src/pkg/`, `tests/`).

`repo-organizer-skill` solves this by empowering AI coding agents (Antigravity, Gemini, Claude, Cursor) to **audit, restructure, and fix links** in your GitHub repository based on your target audience.

---

## ✨ Features

- 🏛️ **4 Targeted Archetypes**:
  - `competition-research`: Partitioned docs hub (`submission/`, `logbook/`, `references/`) + `outputs/`.
  - `paper-release`: Flat 1-command reproduction layout with zero cognitive friction.
  - `open-source-library`: Standard PyPA layout (`src/pkg/`, `tests/`, `examples/`).
  - `data-science-pipeline`: Cookiecutter ML pipeline (`data/`, `models/`, `reports/figures/`).
- 🔗 **Automatic Path & Link Healing**: Automatically updates Markdown image links (`![alt](path)`) and Python relative imports (`sys.path`) after moving files.
- 📑 **Audience Guide Generator**: Auto-generates `docs/README.md` and `outputs/README.md` indices.
- 🛡️ **Git Hardening**: Automatically detects temporary lock files (`.~lock*`), `__pycache__`, and `.DS_Store` to update `.gitignore`.

---

## 🚀 Quick Installation

### Option 1: Antigravity / Gemini Workspace (Recommended)
Copy the skill folder into your project's `.agents/skills/` directory:

```bash
mkdir -p .agents/skills/repo-organizer
curl -sSL https://raw.githubusercontent.com/angelazu-builder/repo-organizer-skill/main/SKILL.md -o .agents/skills/repo-organizer/SKILL.md
```

### Option 2: Global Machine Installation
Install globally across all local projects:

```bash
mkdir -p ~/.gemini/config/skills/repo-organizer
curl -sSL https://raw.githubusercontent.com/angelazu-builder/repo-organizer-skill/main/SKILL.md -o ~/.gemini/config/skills/repo-organizer/SKILL.md
```

---

## 📖 How to Use

Prompt your AI coding assistant with any of the following natural language commands:

```text
"Audit my repository and clean up the root directory clutter."
"Organize this repository for competition judges and research reviewers."
"Restructure this codebase for an academic paper release."
"Format this project as a standard open-source Python package."
```

---

## 🏛️ Archetype Examples

| Archetype | Best For | Example Layout |
| :--- | :--- | :--- |
| **`competition-research`** | Hackathons, Datawhale AI4R, Competitions | [View Example](examples/competition-research.md) |
| **`paper-release`** | arXiv Paper Appendix, Conference Repos | [View Example](examples/paper-release.md) |
| **`open-source-library`** | PyPI Packages, Developer Tools | [View Example](examples/open-source-library.md) |
| **`data-science-pipeline`** | ML Pipelines, Data Analysis Projects | [View Example](examples/data-science-pipeline.md) |

---

## 📄 License

Distributed under the MIT License. See [`LICENSE`](LICENSE) for more information.

---

*Maintained with ❤️ by [Angela Zu (angelazu-builder)](https://github.com/angelazu-builder)*
