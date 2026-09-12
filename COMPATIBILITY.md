# Agent compatibility

Checked against the linked official documentation on 2026-09-12.

## Packaging decision

README Skills uses one canonical [Agent Skills](https://agentskills.io/specification) package:

- `SKILL.md` contains the portable instructions and the commonly accepted `name`, `description`, and `license` frontmatter fields.
- `references/`, `scripts/`, and `assets/` use the standard progressive-disclosure layout.
- `agents/openai.yaml` is optional OpenAI/Codex interface metadata. Other agents can ignore it.
- Vendor-only frontmatter is intentionally absent. The open specification's optional `compatibility` field is documented here instead because the current bundled Codex validator rejects it. Add a thin vendor overlay only if a real client requirement cannot be expressed by the shared core.

No Claude-, Gemini-, Cursor-, Copilot-, or OpenCode-specific copy of the Skill is required today. Duplicating the instructions would make multilingual and behavioral updates drift.

## Install locations

Clone or copy the complete `readme-skills` directory into one location recognized by the client:

| Agent | User scope | Project scope | Notes |
| --- | --- | --- | --- |
| Codex | `$HOME/.agents/skills/readme-skills` | `.agents/skills/readme-skills` | Current shared Agent Skills path; an existing Codex catalog may also use `~/.codex/skills/readme-skills` |
| Claude Code | `~/.claude/skills/readme-skills` | `.claude/skills/readme-skills` | Invoke explicitly with `/readme-skills` or let Claude match the description |
| GitHub Copilot | `~/.agents/skills/readme-skills` or `~/.copilot/skills/readme-skills` | `.agents/skills/readme-skills` or `.github/skills/readme-skills` | Availability varies by Copilot surface |
| Gemini CLI | `~/.agents/skills/readme-skills` or `~/.gemini/skills/readme-skills` | `.agents/skills/readme-skills` or `.gemini/skills/readme-skills` | Can also install directly from the Git repository |
| Cursor | `~/.agents/skills/readme-skills` or `~/.cursor/skills/readme-skills` | `.agents/skills/readme-skills` or `.cursor/skills/readme-skills` | Cursor also discovers compatible Claude and Codex skill directories |
| OpenCode | `~/.agents/skills/readme-skills` or `~/.config/opencode/skills/readme-skills` | `.agents/skills/readme-skills` or `.opencode/skills/readme-skills` | Claude-compatible directories are also supported |

Example:

```bash
git clone https://github.com/Shiaoming123/readme-skills.git "$HOME/.agents/skills/readme-skills"
```

Gemini CLI also supports:

```bash
gemini skills install https://github.com/Shiaoming123/readme-skills.git
```

After installation, start a new agent session or refresh its Skill catalog. Use the client-native explicit form when available (`$readme-skills` in Codex, `/readme-skills` in Claude Code), or ask naturally for a repository README audit, generation, optimization, restructure, translation, or release sync.

## Verified boundary

The shared package structure and selected frontmatter fields conform to the open specification and pass the current bundled Codex validator. The install locations above are taken from current official client documentation. Runtime behavior has not been end-to-end tested on every client, editor surface, or future version; a client that does not expose Agent Skills may require its own instruction mechanism.

## Official sources

- [Agent Skills specification](https://agentskills.io/specification)
- [Codex Skills](https://developers.openai.com/codex/skills/)
- [Claude Code Skills](https://code.claude.com/docs/en/skills)
- [GitHub Copilot Agent Skills](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/add-skills)
- [Gemini CLI Agent Skills](https://geminicli.com/docs/cli/skills/)
- [Cursor Skills](https://cursor.com/docs/skills)
- [OpenCode Skills](https://opencode.ai/docs/skills/)
