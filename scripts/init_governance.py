#!/usr/bin/env python3
"""Initialize the project-governance file structure.

This script is an optional accelerator. If Python is unavailable, agents should
manually create the same structure from assets/governance-template.
"""

from __future__ import annotations

import argparse
import datetime as dt
import os
import re
import shutil
from pathlib import Path


START = "<!-- project-governance:start -->"
END = "<!-- project-governance:end -->"


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def upsert_marker_block(target: Path, block: str) -> str:
    if target.exists():
        content = read_text(target)
    else:
        content = ""

    pattern = re.compile(
        rf"{re.escape(START)}.*?{re.escape(END)}",
        flags=re.DOTALL,
    )
    if pattern.search(content):
        new_content = pattern.sub(block.strip(), content)
        action = "updated"
    else:
        sep = "\n\n" if content.strip() else ""
        new_content = content.rstrip() + sep + block.strip() + "\n"
        action = "inserted"

    write_text(target, new_content)
    return action


def copy_template_tree(src: Path, dst: Path) -> int:
    created = 0
    for item in sorted(src.rglob("*")):
        rel = item.relative_to(src)
        out = dst / rel
        if item.is_dir():
            out.mkdir(parents=True, exist_ok=True)
            continue

        out.parent.mkdir(parents=True, exist_ok=True)
        if out.exists():
            continue
        shutil.copy2(item, out)
        created += 1
    return created


def update_bootstrap_metadata(project_root: Path, project_type: str) -> None:
    bootstrap = project_root / ".project-governance" / "AGENT_BOOTSTRAP.md"
    if not bootstrap.exists():
        return
    today = dt.date.today().isoformat()
    content = read_text(bootstrap)
    content = content.replace("initialized_at=TBD", f"initialized_at={today}")
    content = content.replace("project_type=TBD", f"project_type={project_type}")
    write_text(bootstrap, content)


def scan_candidates(project_root: Path) -> list[Path]:
    names = {
        "readme",
        "prd",
        "product",
        "requirements",
        "architecture",
        "api",
        "design",
        "spec",
    }
    skip_dirs = {".git", "node_modules", ".project-governance", ".venv", "dist", "build"}
    candidates: list[Path] = []
    for current, dirs, files in os.walk(project_root):
        current_path = Path(current)
        rel_dir = current_path.relative_to(project_root)
        depth = 0 if rel_dir == Path(".") else len(rel_dir.parts)
        dirs[:] = [name for name in dirs if name not in skip_dirs and depth < 3]

        for filename in files:
            path = current_path / filename
            rel = path.relative_to(project_root)
            if len(rel.parts) > 4:
                continue
            lowered = filename.lower()
            if any(key in lowered for key in names):
                candidates.append(rel)
    return sorted(candidates)


def write_scan(project_root: Path) -> int:
    candidates = scan_candidates(project_root)
    index = project_root / ".project-governance" / "imports" / "SOURCE_INDEX.md"
    lines = [
        "# Source Index",
        "",
        "本文件记录已有项目文档的导入过程。原始文档不移动、不删除；被提炼并确认后，SSOT 优先于原始文档。",
        "",
        "| Source Path | Type | Trust Level | Import Status | Imported Into | Notes |",
        "|---|---|---|---|---|---|",
    ]
    for rel in candidates:
        lines.append(f"| `{rel.as_posix()}` | candidate | TBD | candidate | TBD | auto-scanned |")
    lines.extend(
        [
            "",
            "Import status: `candidate`, `partial-import`, `imported-confirmed`, `reference-only`, `superseded-by-ssot`, `conflicting`.",
        ]
    )
    write_text(index, "\n".join(lines) + "\n")
    return len(candidates)


def main() -> int:
    parser = argparse.ArgumentParser(description="Initialize project-governance in a project")
    parser.add_argument("--project-root", default=".", help="Project root to initialize")
    parser.add_argument("--project-type", default="TBD", help="Project type, e.g. ui-project")
    parser.add_argument("--scan", action="store_true", help="Scan existing docs into imports/SOURCE_INDEX.md")
    args = parser.parse_args()

    script_dir = Path(__file__).resolve().parent
    template_root = script_dir.parent / "assets" / "governance-template"
    project_root = Path(args.project_root).resolve()

    if not template_root.exists():
        raise SystemExit(f"template root not found: {template_root}")

    created = copy_template_tree(template_root / ".project-governance", project_root / ".project-governance")

    agents_action = upsert_marker_block(
        project_root / "AGENTS.md",
        read_text(template_root / "root" / "AGENTS.block.md"),
    )
    claude_action = upsert_marker_block(
        project_root / "CLAUDE.md",
        read_text(template_root / "root" / "CLAUDE.block.md"),
    )

    update_bootstrap_metadata(project_root, args.project_type)
    scan_count = 0
    if args.scan:
        scan_count = write_scan(project_root)

    print(f"Initialized project-governance in {project_root}")
    print(f"AGENTS.md: {agents_action} marker block")
    print(f"CLAUDE.md: {claude_action} marker block")
    print(f"Files created: {created}")
    if args.scan:
        print(f"Existing document candidates indexed: {scan_count}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
