---
name: project-governance
description: Manual project governance initializer/upgrader. Use when explicitly invoked to initialize transferable `.project-governance/`, import existing PRD/architecture/product docs into a project SSOT, upgrade existing governance, or re-enable disabled governance. Produces project-owned rules for fixed four-stage project skeleton (requirements / tech stack / active development / acceptance testing), multi-version snapshots with backlog and regression tracking, agent-user glossary, grilling-style clarification with one-question-at-a-time, and a user-private process library at `~/.claude/process-library/`.
---

# Project Governance

Create or maintain a project-owned governance system that works even after the project moves to an environment without this skill.

## Hard Rules

- Only run when explicitly asked to initialize, import, upgrade, or re-enable governance.
- Project-side rules (four-stage skeleton, version + backlog + regression model, grilling protocol, plain-language communication, glossary discipline, no-preset-process policy) live in the generated `.project-governance/` and `~/.claude/process-library/`. Do not duplicate or weaken them here — this `SKILL.md` is the installer's playbook, not a second source of truth.

## Workflow

1. Orient: lightly scan the project root, `AGENTS.md`, `CLAUDE.md`, README files, manifests, and likely product/architecture/API/design docs. If `.project-governance/` exists, read `AGENT_BOOTSTRAP.md`, `ssot/PROJECT_STATE.md`, `ssot/GLOSSARY.md`, and `processes/active.md` if present.
2. Classify: new project, existing docs import, existing governance upgrade, or disabled governance re-enable.
3. Create/update governance files: prefer `scripts/init_governance.py`; if Python or the script fails, manually copy the same structure from `assets/governance-template/`.
4. Preserve existing `AGENTS.md` and `CLAUDE.md`; insert or update only the `project-governance` marker block.
5. Drive the project through the fixed four-stage skeleton; never reorder or rename it. Inside the third stage, discuss the development flow with the user, looking up `~/.claude/process-library/` first.
6. Validate with generated `.project-governance/scripts/check-governance.sh` when possible, and run the skill validator after editing this skill.

## Generated Layout

Generated projects use `AGENTS.md` and `CLAUDE.md` as entry points, with all durable rules under `.project-governance/`:

- `AGENT_BOOTSTRAP.md` — startup checklist + the red lines (points to the rules files below for details)
- `rules/GRILLING_PROTOCOL.md` — when/how to grill, what counts as confirmation, where to write the result
- `rules/DEVELOPMENT_PROCESS.md` — four-stage skeleton model, flow template fields, internal-flow mutation rules, skip rule
- `rules/VERSION_RULES.md` — version snapshots, regression action, backlog, hard-bump handling, sinking triggers
- `rules/DOCUMENTATION_RULES.md` — SSOT list, change-history rules, import rules, language policy
- `rules/UPGRADE_RULES.md` — semver, upgrade safety, 0.x → 1.0.0 migration path, disable/re-enable
- `ssot/PRD.md`, `ssot/ARCHITECTURE.md`, `ssot/API_CONTRACT.md` — product / architecture / API SSOT
- `ssot/PROJECT_STATE.md` — current version + four-stage status + Active Process + Backlog + Stage Regressions + Stage Skips
- `ssot/GLOSSARY.md` — user term ↔ doc term ↔ code identifier dictionary, shared across versions
- `processes/active.md` — the development flow agreed for the current version's third stage
- `processes/tasks/<stage_id>.md` — fine-grained task plan required before any code work for each `acceptance_required` stage of the active development flow; rules in `rules/DEVELOPMENT_PROCESS.md` "Task Plan 前置" section
- `decisions/INDEX.md`, `imports/SOURCE_INDEX.md`, `templates/RECORD_TEMPLATES.md`
- `scripts/check-governance.sh` — structural validator

Existing docs are inputs, not authority: index them, grill and confirm extracted facts, then make SSOT (and the glossary) authoritative.

## Process Library (user-local, private)

Location: `~/.claude/process-library/`. Created on first need by `scripts/init_governance.py`. Not part of the skill repository, not part of any generated project. Ships **empty**; grows as the user finishes projects. Lookup / drafting / sinking rules live in `rules/DEVELOPMENT_PROCESS.md` and `rules/VERSION_RULES.md` — read those, do not restate them here.

## Resources

- `assets/governance-template/`: files copied into the generated project.
- `scripts/init_governance.py`: optional initializer; also seeds `~/.claude/process-library/` on first run unless `--skip-process-library` is set.
