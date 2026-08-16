# 🤖 AI Agent Skill & MCP Server Archetype (`agent-skill-mcp`)

## Target Audience
- **AI Agent Developers & Users** (Antigravity, Cursor, Claude MCP, GitHub Copilot).
- **Core Goal**: **Instant 1-click integration** into local or workspace skill configs.

## Recommended Structure
```
my-agent-skill/
├── README.md                  # 1-line installation curl script + tool spec
├── LICENSE
├── SKILL.md                   # Core skill metadata & instructions
├── plugin.json                # Plugin manifest
├── .agents/skills/my-skill/   # Workspace auto-discovery folder
│   └── SKILL.md
└── examples/                  # Usage prompts & agent trajectory logs
```
