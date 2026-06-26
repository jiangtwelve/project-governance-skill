---
name: project-governance
description: Manual project governance initializer/upgrader. Use when explicitly invoked to initialize transferable `.project-governance/`, import existing PRD/architecture/product docs into a project SSOT, upgrade existing governance, or re-enable disabled governance. Produces project-owned rules for PRD, architecture, API contracts, staged development, grilling-style clarification, acceptance, decisions, and cross-agent continuity.
---

# Project Governance

Create or maintain a project-owned governance system that works even after the project moves to an environment without this skill.

## Hard Rules

- Use only when explicitly asked to initialize, import, upgrade, or re-enable governance.
- Never fast-start code and backfill docs later; application code starts only after grilling, PRD confirmation, architecture confirmation, and stage state are complete.
- Resolve ambiguity with the bundled grilling protocol: inspect files first when possible; otherwise ask one question at a time with a recommended answer until decisions are confirmed.
- Update the project SSOT for any requirement, interaction, architecture, API, data model, or workflow change.
- Generated project files must remain understandable without this skill, external `grill-me`, Python, or other tooling.

## Workflow

1. Orient: lightly scan the project root, `AGENTS.md`, `CLAUDE.md`, README files, manifests, and likely product/architecture/API/design docs. If `.project-governance/` exists, read `MANIFEST.md`, `AGENT_BOOTSTRAP.md`, and `ssot/PROJECT_STATE.md`.
2. Classify: new project, existing docs import, existing governance upgrade, or disabled governance re-enable.
3. Create/update governance files: prefer `scripts/init_governance.py`; if Python or the script fails, manually copy the same structure from `assets/governance-template/`.
4. Preserve existing `AGENTS.md` and `CLAUDE.md`; insert or update only the `project-governance` marker block.
5. Confirm before code. For UI projects, the first frontend step must be static key pages for visual style confirmation.
6. Validate with generated `.project-governance/scripts/check-governance.sh` when possible, and run the skill validator after editing this skill.

## Generated System

Generated projects use `AGENTS.md` and `CLAUDE.md` as entry points. All governance lives under `.project-governance/`:

- `AGENT_BOOTSTRAP.md`, `MANIFEST.md`
- `rules/`: grilling, development process, documentation, logging, upgrades, process variants
- `ssot/`: `PRD.md`, `ARCHITECTURE.md`, `API_CONTRACT.md`, `PROJECT_STATE.md`
- `decisions/INDEX.md`, `imports/SOURCE_INDEX.md`
- `templates/`: decision and acceptance records
- `scripts/check-governance.sh`

`AGENTS.md` must contain the `<!-- project-governance:start --> ... <!-- project-governance:end -->` marker block.

## Modes and Imports

- Governance-only: create governance and SSOT placeholders for existing projects, uncertain stacks, or early product discussion.
- Full-init: initialize application code only after PRD, architecture, API contract, and stage state are confirmed.
- Existing documents are inputs, not authority. Index them in `imports/SOURCE_INDEX.md`; extract facts into SSOT only after grilling and user confirmation. Confirmed SSOT wins over originals.

## Process and Lifecycle

- UI projects follow `rules/processes/ui-project.md`: PRD/architecture, API contract, static key-page style confirmation, frontend Mock, frontend acceptance, backend, integration, release acceptance.
- Non-UI projects follow `rules/processes/default-project.md`.
- Skipping unaffected stages requires explicit user confirmation and must be recorded in `PROJECT_STATE.md`.
- Version governance with `MANIFEST.md`. Patch/minor/major upgrades follow `rules/UPGRADE_RULES.md`.
- Never silently overwrite `rules/*` or project facts in `ssot/*`; ask for confirmation.
- Disable by changing the `AGENTS.md` marker block to `Status: disabled`; re-enable only after synchronizing changes made while disabled.

## Resources

- `assets/governance-template/`: generated governance files and marker blocks.
- `scripts/init_governance.py`: optional initializer.

```bash
python3 project-governance/scripts/init_governance.py --project-root /path/to/project --project-type ui-project --scan
```
