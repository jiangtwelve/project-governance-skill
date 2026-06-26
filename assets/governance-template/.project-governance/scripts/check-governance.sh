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

need_file "AGENTS.md"
need_file "CLAUDE.md"
need_dir ".project-governance"
need_file ".project-governance/AGENT_BOOTSTRAP.md"
need_file ".project-governance/GOVERNANCE_VERSION"
need_file ".project-governance/MANIFEST.md"
need_file ".project-governance/ssot/PROJECT_STATE.md"
need_file ".project-governance/ssot/PRD.md"
need_file ".project-governance/ssot/ARCHITECTURE.md"
need_file ".project-governance/ssot/API_CONTRACT.md"
need_file ".project-governance/decisions/INDEX.md"
need_file ".project-governance/imports/SOURCE_INDEX.md"

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
