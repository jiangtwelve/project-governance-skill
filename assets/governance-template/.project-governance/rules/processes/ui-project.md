# UI Project Process

适用于 Web App、SaaS、管理后台、移动端、小程序、带界面的工具。

| Stage ID | 中文阶段 | 完成条件 |
|---|---|---|
| 01_prd_architecture_confirmation | PRD 与架构确认 | `ssot/PRD.md`、`ssot/ARCHITECTURE.md`、`ssot/PROJECT_STATE.md` 已确认 |
| 02_api_contract | API 接口标准制定 | `ssot/API_CONTRACT.md` 可指导前端 Mock 和后端实现 |
| 03_frontend_static_style_confirmation | 关键静态页面风格确认 | 已实现关键页面静态版本，用户明确确认风格 |
| 04_frontend_mock_implementation | 前端 Mock 开发 | 当前范围页面完成，按 API Contract 接入 Mock，主要路径可演示 |
| 05_frontend_acceptance | 前端阶段验收 | 用户明确验收通过，并在 `acceptance/` 下记录 |
| 06_backend_implementation | 后端开发 | 按 API Contract 实现后端逻辑；本阶段不单独验收 |
| 07_integration | 前后端联调 | 前端接真实后端，关键流程联调通过；本阶段不单独验收 |
| 08_release_acceptance | 当前版本全量验收 | 用户明确验收通过，并在 `acceptance/` 下记录 |

## 强制规则

- 前端开发第一步必须做关键页面静态版本；用户确认前不得批量开发后续页面。
- 前端阶段验收不通过时，先更新 SSOT，再按影响范围回退流程。
- 当前版本全量验收中出现需求或交互变化时，更新 SSOT 并按影响范围重走流程。
- 验收记录按 `templates/ACCEPTANCE_REPORT.template.md` 创建或更新。
