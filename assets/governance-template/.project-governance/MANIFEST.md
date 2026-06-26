# Project Governance Manifest

| Field | Value |
|---|---|
| governance_skill | project-governance |
| governance_version | 0.1.0 |
| initialized_at | TBD |
| project_type | TBD |
| status | enabled |

## 规则

- `.project-governance/` 是本项目治理系统的唯一根目录。
- `AGENTS.md` 是外部入口；`CLAUDE.md` 指向 `AGENTS.md`。
- `.project-governance/ssot/*` 是需求、架构、接口和项目状态的权威来源。
- 原始项目文档被导入并确认后不再作为 SSOT；若与 SSOT 冲突，以 SSOT 为准。
