---
name: project-governance
description: Manual project governance initializer/upgrader. Use when explicitly invoked to initialize transferable `.project-governance/`, import existing PRD/architecture/product docs into a project SSOT, upgrade existing governance, or re-enable disabled governance. Produces project-owned rules for fixed four-stage project skeleton (requirements / tech stack / active development / acceptance testing), multi-version snapshots with backlog and regression tracking, agent-user glossary, grilling-style clarification with one-question-at-a-time, and a user-private process library at `~/.claude/process-library/`.
---

# Project Governance

Create or maintain a project-owned governance system that works even after the project moves to an environment without this skill.

## Hard Rules

- Only run when explicitly asked to initialize, import, upgrade, or re-enable governance.
- Project-side hard rules (no fast-start, grilling before code, SSOT updates, generator self-containment, fixed four-stage skeleton, one-question-at-a-time grilling, plain-language communication, glossary discipline) live in the generated `.project-governance/`; do not duplicate or weaken them here.
- The skill ships **no preset development processes**. The project skeleton (four stages) is fixed; the development flow inside the third stage is discussed and decided with the user.

## Workflow

1. Orient: lightly scan the project root, `AGENTS.md`, `CLAUDE.md`, README files, manifests, and likely product/architecture/API/design docs. If `.project-governance/` exists, read `AGENT_BOOTSTRAP.md`, `ssot/PROJECT_STATE.md`, `ssot/GLOSSARY.md`, and `processes/active.md` if present.
2. Classify: new project, existing docs import, existing governance upgrade, or disabled governance re-enable.
3. Create/update governance files: prefer `scripts/init_governance.py`; if Python or the script fails, manually copy the same structure from `assets/governance-template/`.
4. Preserve existing `AGENTS.md` and `CLAUDE.md`; insert or update only the `project-governance` marker block.
5. Drive the project through the fixed four-stage skeleton; never reorder or rename it. Inside the third stage, discuss the development flow with the user, looking up `~/.claude/process-library/` first.
6. Validate with generated `.project-governance/scripts/check-governance.sh` when possible, and run the skill validator after editing this skill.

## Generated System

Generated projects use `AGENTS.md` and `CLAUDE.md` as entry points, with all durable rules under `.project-governance/`:

- `AGENT_BOOTSTRAP.md`
- `rules/GRILLING_PROTOCOL.md`, `rules/DEVELOPMENT_PROCESS.md`, `rules/VERSION_RULES.md`, `rules/DOCUMENTATION_RULES.md`, `rules/UPGRADE_RULES.md`
- `ssot/PRD.md`, `ssot/ARCHITECTURE.md`, `ssot/API_CONTRACT.md`, `ssot/PROJECT_STATE.md`, `ssot/GLOSSARY.md`
- `processes/active.md` (the development flow agreed for the current version's third stage)
- `decisions/INDEX.md`, `imports/SOURCE_INDEX.md`, `templates/RECORD_TEMPLATES.md`
- `scripts/check-governance.sh`

Existing docs are inputs, not authority: index them, grill and confirm extracted facts, then make SSOT (and the glossary) authoritative.

## Project Skeleton (固定四段，不可变)

| Stage | 中文名称 | English Name |
|---|---|---|
| 01 | 需求确认 | Requirements Confirmation |
| 02 | 技术栈确认 | Tech Stack Confirmation |
| 03 | 实际开发 | Active Development |
| 04 | 验收测试 | Acceptance Testing |

The skeleton is locked: cannot be renamed, merged, or skipped. Stages 1, 2, 4 are determined by user explicit confirmation; stage 3 carries the version-specific development flow agreed in stage 2.

## Versioning, Regression, Backlog

- Each version owns an independent four-stage snapshot under `Versions`. Old versions are marked `Released` and never overwritten; new versions are appended.
- Stage state can regress within a version (e.g. requirement change during stage 3 triggers regression to stage 1); regression is explicit and logged in `Stage Regressions`.
- Functions deferred without a target version go into `Backlog`; agent prompts to consume backlog when starting new versions, and prompts to open a new version when backlog is non-empty after planned versions complete.
- Version bumps are user-driven; agent refuses to bump while current version is incomplete and guides the user to merge or backlog instead.

## Process Library (用户本机私有)

- Location: `~/.claude/process-library/` (created on first need; not part of the skill repository, not part of generated project).
- Ships **empty**. The library grows as the user finishes projects.
- Lookup happens at the start of stage 2; agent matches by project type + tech stack keywords and surfaces candidates with `applicable_to` + `lessons_learned`.
- When no candidate fits, agent drafts the flow in-project, confirms it with the user, and stores it in `processes/active.md` for the current version (not yet in the library).
- Sinking into the library is triggered only when (a) the first version's stage 4 is `Confirmed`, or (b) a later version finishes after the flow was modified. The agent asks; the user decides whether to add, replace, or skip.

## Internal-Flow Mutation Boundary

- Changes inside `processes/active.md` are allowed (add / remove / reorder / edit stages), but each change goes through one-question-at-a-time grilling with the agent's recommendation and rationale.
- When a single proposal exceeds `Process Mutation Threshold` (default 3) changes, the agent must first ask whether to switch flows instead of editing this one.
- Any confirmed change forces stage 3 to restart from the new flow's first step; overlapping artifacts from the previous flow are adjudicated per stage (reuse / patch / redo) and the decisions are logged.

## Glossary (双语对照表)

`ssot/GLOSSARY.md` is the single source of truth for translating between user spoken vocabulary, document terminology, and code identifiers. Maintained across versions (not reset per version). New concepts must be entered before being used in PRD, architecture, API, or code.

## Resources

- `assets/governance-template/`: generated governance files and marker blocks.
- `scripts/init_governance.py`: optional initializer.
