#!/usr/bin/env sh
set -eu

root="${1:-.}"
status=0

need_file() {
  if [ ! -f "$root/$1" ]; then
    printf 'missing file: %s\n' "$1"
    status=1
  fi
}

need_dir() {
  if [ ! -d "$root/$1" ]; then
    printf 'missing directory: %s\n' "$1"
    status=1
  fi
}

required_dirs=".project-governance .project-governance/acceptance .project-governance/changelog .project-governance/imports/analysis"
required_files="AGENTS.md CLAUDE.md .project-governance/AGENT_BOOTSTRAP.md .project-governance/MANIFEST.md .project-governance/rules/GRILLING_PROTOCOL.md .project-governance/rules/DEVELOPMENT_PROCESS.md .project-governance/rules/DOCUMENTATION_RULES.md .project-governance/rules/LOGGING_RULES.md .project-governance/rules/UPGRADE_RULES.md .project-governance/rules/processes/ui-project.md .project-governance/rules/processes/default-project.md .project-governance/ssot/PROJECT_STATE.md .project-governance/ssot/PRD.md .project-governance/ssot/ARCHITECTURE.md .project-governance/ssot/API_CONTRACT.md .project-governance/decisions/INDEX.md .project-governance/imports/SOURCE_INDEX.md .project-governance/templates/ACCEPTANCE_REPORT.template.md .project-governance/templates/DECISION_RECORD.template.md"

for dir in $required_dirs; do
  need_dir "$dir"
done

for file in $required_files; do
  need_file "$file"
done

if [ -f "$root/AGENTS.md" ] && ! grep -q 'project-governance:start' "$root/AGENTS.md"; then
  printf 'AGENTS.md missing project-governance marker block\n'
  status=1
fi

if [ -f "$root/CLAUDE.md" ] && ! grep -q 'project-governance:start' "$root/CLAUDE.md"; then
  printf 'CLAUDE.md missing project-governance marker block\n'
  status=1
fi

if [ "$status" -eq 0 ]; then
  printf 'project-governance structure OK\n'
fi

exit "$status"
