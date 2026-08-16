# 📦 repo-organizer-skill

> **AI Agent Skill for auditing, restructuring, and optimizing GitHub repositories based on target audience & use-case — with automated competitive edge discovery.**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.8%2B-green.svg)](https://www.python.org/)
[![Antigravity](https://img.shields.io/badge/Antigravity-Agent%20Skill-blue.svg)](https://github.com/angelazu-builder/repo-organizer-skill)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

---

## 🎯 Core Philosophy: Audience Alignment & Friction Reduction

A great GitHub repository is not defined by rigid boilerplate, but by **how effortlessly it communicates with its target audience**:
- **Competition Judges** want a structured deliverables hub (`docs/submission/`).
- **Academic Peer Reviewers** want zero-friction single-command reproduction (`python run_eval.py`).
- **Developers** want quickstart installation and clean modular code (`src/pkg/`, `tests/`).

`repo-organizer-skill` gives AI Agents (Antigravity, Cursor, Claude MCP, Gemini) the exact intelligence to **audit your code, identify your true competitive edge, and align your repository structure with your specific scenario.**

```
┌────────────────────────┐      ┌──────────────────────────────┐      ┌─────────────────────────────┐
│   Messy Root Clutter   │ ───► │  Agent Innovation Audit &    │ ───► │  Audience-Aligned Repo      │
│ (PNGs, CSVs, Pycache)  │      │  Competitive Edge Discovery  │      │  Structure (8 Archetypes)   │
└────────────────────────┘      └──────────────────────────────┘      └─────────────────────────────┘
```

---

## 💎 Killer Feature: Agent Innovation Audit & Developer Feedback Loop

Developers often lack objective self-awareness of their code's true strengths. They highlight commodity features (*"Built with React"*) while missing their **genuine unfair technical advantage**.

`repo-organizer-skill` equips your Agent to perform a 4-step audit:

1. 🟢 **Discover Genuine Technical Novelty**: Identifies algorithms, JIT accelerations, and zero-dependency designs unique across GitHub.
2. 🟡 **Filter Saturated Commodity Claims**: Down-weights commonplace claims (*"Uses AsyncIO"*) so they don't waste prime README real estate.
3. ✨ **Inject `✨ Key Edge` Section**: Automatically formats and places your true competitive edge right below the title hook.
4. 🔴 **Output Developer Feedback Report**: Delivers a private audit report identifying competitive gaps against SOTA projects.

---

## 🏛️ 8 Popular Repository Archetypes

Click any archetype to view its recommended structure and before/after example:

| Archetype | Target Audience | Example Structure |
| :--- | :--- | :--- |
| **`competition-research`** | Hackathons, Datawhale AI4R, Competitions | [View Example](examples/competition-research.md) |
| **`paper-release`** | arXiv Paper Appendix, Conference Repos | [View Example](examples/paper-release.md) |
| **`open-source-library`** | PyPI Packages, Developer Tools | [View Example](examples/open-source-library.md) |
| **`data-science-pipeline`** | ML Pipelines, Data Science Projects | [View Example](examples/data-science-pipeline.md) |
| **`agent-skill-mcp`** | AI Agent Developers (Antigravity, MCP) | [View Example](examples/agent-skill-mcp.md) |
| **`curated-awesome-list`** | Community Curators & Topic Lists | [View Example](examples/curated-awesome-list.md) |
| **`fullstack-web-app`** | SaaS Founders & Web Developers | [View Example](examples/fullstack-web-app.md) |
| **`cli-binary-tool`** | DevOps & System Administrators | [View Example](examples/cli-binary-tool.md) |

---

## ⚖️ Capability Comparison Matrix

| Capability | Manual Cleanup | General AI (Codex / Claude) | `repo-organizer-skill` |
| :--- | :---: | :---: | :---: |
| **Root Junk Identification (`.png`, `.csv`)** | ⚠️ Manual | ✅ Capable | ✅ Automated Workflow |
| **Basic README Formatting & Badges** | ⚠️ Manual | ✅ Capable | ✅ Automated Workflow |
| **Multi-Audience Alignment (8 Archetypes)** | ❌ No | ⚠️ Needs Complex Prompting | ✅ Built-in Workflows |
| **Directory-Wide Link & Import Healing** | ⚠️ Error-Prone | ⚠️ Single-file Scope | ✅ Full Tree Verification |
| **Competitive Edge Audit & Feedback Report** | ❌ Subjective | ❌ No | ✅ Automated 4-Step Loop |

---

## 🚀 1-Line Quickstart Installation

### Option 1: Workspace Installation (Recommended)
```bash
mkdir -p .agents/skills/repo-organizer
curl -sSL https://raw.githubusercontent.com/angelazu-builder/repo-organizer-skill/main/SKILL.md -o .agents/skills/repo-organizer/SKILL.md
```

### Option 2: Global Machine Installation
```bash
mkdir -p ~/.gemini/config/skills/repo-organizer
curl -sSL https://raw.githubusercontent.com/angelazu-bullet/repo-organizer-skill/main/SKILL.md -o ~/.gemini/config/skills/repo-organizer/SKILL.md
```

---

## 📖 How to Prompt Your Agent

Once installed, simply ask your agent:

```text
"Audit my repository and structure it for competition judges."
"Discover the true competitive edge of my codebase and update the README."
"Restructure this codebase for an academic paper release."
```

---

## 📄 License

Distributed under the MIT License. See [`LICENSE`](LICENSE) for more information.

*Maintained with ❤️ by [Angela Zu (angelazu-builder)](https://github.com/angelazu-builder)*
