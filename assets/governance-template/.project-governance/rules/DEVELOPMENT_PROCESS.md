# Development Process

开发流程不可随意变更。跨流程的硬规则在 `AGENT_BOOTSTRAP.md`，本文件只列流程专属规则。

## 流程规则

- 不受影响的阶段可由 agent 建议、用户明确确认后跳过。
- 首次完整 UI 流程包含两次验收：前端阶段验收、当前版本全量验收。
- 后续因需求或交互变更重走流程时，只保留最后一次验收，范围可收窄到受影响内容。

## 阶段字典

| ID | 中文名称 | English Name | 验收 |
|---|---|---|---|
| 00_governance_initialization | 治理体系初始化 | Governance Initialization | 否 |
| 01_prd_architecture_confirmation | PRD 与架构确认 | PRD and Architecture Confirmation | 是 |
| 02_api_contract | API 接口标准制定 | API Contract Definition | 否 |
| 03_frontend_static_style_confirmation | 关键静态页面风格确认 | Frontend Static Style Confirmation | 是 |
| 04_frontend_mock_implementation | 前端 Mock 开发 | Frontend Mock Implementation | 否 |
| 05_frontend_acceptance | 前端阶段验收 | Frontend Acceptance | 是 |
| 06_backend_implementation | 后端开发 | Backend Implementation | 否 |
| 07_integration | 前后端联调 | Integration | 否 |
| 08_release_acceptance | 当前版本全量验收 | Release Acceptance | 是 |

## 流程选择

- UI 项目使用 `rules/processes/ui-project.md`。
- 非 UI 项目使用默认流程：PRD 与架构确认 -> 契约确认 -> 核心实现 -> 测试验证 -> 当前版本全量验收。
- Web App、SaaS、管理后台、移动端、小程序、带界面的工具都属于 UI 项目。

默认流程同样要求：有歧义必须追问；需求变化更新 PRD；架构、契约、数据模型变化更新对应 SSOT；完成前必须获得用户明确验收；跳过阶段必须由用户确认。

## 跳过记录

跳过阶段时，在 `ssot/PROJECT_STATE.md` 记录：阶段 ID、中文名称、跳过原因、影响范围、用户确认。
