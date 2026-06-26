---
name: project-governance
description: Manual project governance initializer and upgrader. Use when explicitly invoked to initialize a transferable project governance system, import existing PRD/architecture/product docs into a project SSOT, upgrade an existing `.project-governance/` system, or re-enable governance after it was disabled. Creates project-owned rules for PRD, architecture, API contracts, staged development, grilling-style clarification, acceptance, decisions, and cross-agent continuity.
---

# Project Governance

Use this skill to create or maintain a project-owned governance system that remains usable after the project is moved to an environment without this skill.

## Non-negotiable Behavior

- Treat this skill as primarily manual-triggered. Do not inject it into ordinary coding work unless the user explicitly asks to initialize, import, upgrade, or re-enable project governance.
- Do not let users fast-start coding and backfill docs later. Application code starts only after the necessary grilling, PRD confirmation, architecture confirmation, and stage state are complete.
- When anything is ambiguous or meaningfully debatable, use the bundled grilling protocol: ask one question at a time, give a recommended answer, and continue until the decision tree is resolved.
- If a question can be answered by inspecting the project, inspect the project instead of asking.
- Any demand, interaction, architecture, API, data model, or workflow change must update the project SSOT and leave a concise trace.
- The generated project governance files must not require this skill, `grill-me`, Python, or any external tool to remain understandable.

## Core Workflow

1. Orient first.
   - Lightly scan the project root, existing `AGENTS.md`, `CLAUDE.md`, README files, manifest files, and likely product/architecture/API/design docs.
   - Do not deep-read the whole codebase unless needed for a specific decision.
   - If `.project-governance/` exists, read its `MANIFEST.md`, `GOVERNANCE_VERSION`, `AGENT_BOOTSTRAP.md`, and `ssot/PROJECT_STATE.md`.

2. Classify the operation.
   - New empty project: initialize governance, then grill the user until PRD and architecture can be confirmed.
   - Existing project with docs: import and analyze existing docs, identify conflicts and gaps, then grill the user before writing confirmed SSOT.
   - Existing project with governance: compare versions and propose an upgrade plan.
   - Disabled governance: synchronize changes made while disabled before re-enabling the `AGENTS.md` marker block.

3. Create or update the project-owned governance files.
   - Prefer `scripts/init_governance.py` when Python is available.
   - If Python is unavailable or the script fails, manually create the same structure from `assets/governance-template/`.
   - Script failure is not a reason to skip governance initialization.

4. Confirm project facts before application code.
   - Governance scaffolding can be created early so decisions have a home.
   - Do not initialize or modify application code until PRD, architecture, and the relevant development stage are confirmed.
   - For UI projects, the first frontend implementation step must be static key pages for visual style confirmation.

5. Validate.
   - Run the generated `.project-governance/scripts/check-governance.sh` when possible.
   - Run the skill validator after modifying this skill itself.
   - Report any validation that could not be run.

## Generated Project Structure

The generated project uses `AGENTS.md` and `CLAUDE.md` as external entry points. All governance rules and SSOT files live under `.project-governance/` to avoid conflicts with a project's own `docs/` folder.

```text
AGENTS.md
CLAUDE.md
.project-governance/
  AGENT_BOOTSTRAP.md
  GOVERNANCE_VERSION
  MANIFEST.md
  rules/
    GRILLING_PROTOCOL.md
    DEVELOPMENT_PROCESS.md
    DOCUMENTATION_RULES.md
    LOGGING_RULES.md
    UPGRADE_RULES.md
    processes/
      ui-project.md
      default-project.md
  ssot/
    PRD.md
    ARCHITECTURE.md
    API_CONTRACT.md
    PROJECT_STATE.md
  decisions/
    INDEX.md
  acceptance/
    FRONTEND_ACCEPTANCE.md
    RELEASE_ACCEPTANCE.md
  imports/
    SOURCE_INDEX.md
    analysis/
  changelog/
    GOVERNANCE_CHANGELOG.md
  templates/
  scripts/
    check-governance.sh
```

`AGENTS.md` must contain a marker block bounded by:

```text
<!-- project-governance:start -->
...
<!-- project-governance:end -->
```

If `AGENTS.md` or `CLAUDE.md` already exists, preserve existing content and insert or update only the marker block.

## Initialization Modes

Support two modes and choose based on context:

- Governance-only: create the governance system and SSOT placeholders. Use for existing projects, uncertain tech stacks, or early product discussions.
- Full-init: after PRD, architecture, API contract, and process stage are confirmed, initialize the actual code project according to the confirmed architecture.

For existing documents:

- Do not move or delete original documents.
- Index candidate sources in `.project-governance/imports/SOURCE_INDEX.md`.
- Extract facts into SSOT only after grilling and user confirmation.
- Once imported and confirmed, original docs are no longer authoritative. If they conflict with SSOT, SSOT wins.
- User's latest explicit confirmation wins over original docs, but must update SSOT and decision records.

## Development Process Requirements

For UI projects, write and enforce the full UI process in `.project-governance/rules/processes/ui-project.md`:

1. PRD and architecture confirmation.
2. API contract definition for frontend Mock and backend implementation.
3. Static key-page implementation for visual style confirmation.
4. Frontend implementation with Mock data.
5. Frontend acceptance. User must explicitly pass this stage before backend development.
6. Backend implementation.
7. Frontend/backend integration.
8. Current-version full acceptance.

Only the first complete run requires both frontend acceptance and release acceptance. Later reruns caused by requirement or interaction changes keep only final acceptance, scoped to affected behavior when appropriate.

For non-UI projects, use the default process and tailor the contract document to the project type.

Stage skipping rule: the agent may recommend skipping unaffected stages, but the user must explicitly confirm the skip. Record the skipped stage IDs, Chinese names, reason, impact, and confirmation in `PROJECT_STATE.md`.

## Upgrade Rules

Each generated governance system has a semantic version in `.project-governance/GOVERNANCE_VERSION`.

- Patch upgrades should not interrupt the current stage.
- Minor upgrades can continue the current stage but may require missing documents to be backfilled.
- Major upgrades require an impact assessment before continuing.

Never silently overwrite `.project-governance/rules/*`. Generate an upgrade plan, ask for user confirmation, then modify rules. Do not overwrite project facts in `ssot/*`.

After any upgrade, write the result to `changelog/GOVERNANCE_CHANGELOG.md` and update `PROJECT_STATE.md` if the current plan changed.

## Disable and Re-enable

To disable governance, the user can change the marker block in `AGENTS.md` from `Status: enabled` to `Status: disabled`. No heavy governance-change process is required.

To re-enable governance, first synchronize changes made while disabled:

- Scan project changes and relevant docs.
- Update `PROJECT_STATE.md`.
- Update PRD, architecture, API contract, and decisions if needed.
- Restore the `AGENTS.md` marker block to `Status: enabled`.

## Resource Use

- `assets/governance-template/`: source of all generated governance files and marker blocks.
- `scripts/init_governance.py`: optional initializer. Use `--scan` for existing projects when you want a first-pass source index.

Example:

```bash
python3 project-governance/scripts/init_governance.py --project-root /path/to/project --project-type ui-project --scan
```
