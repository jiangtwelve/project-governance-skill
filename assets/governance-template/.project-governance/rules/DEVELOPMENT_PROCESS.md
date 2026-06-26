# Development Process

开发流程不可随意变更。流程可以根据影响范围有条件跳过阶段，但跳过建议必须由 agent 提出、用户明确确认后才能生效。

## 通用强制规则

- 不允许快速开始写代码，文档以后再补。
- PRD 与架构确认前不得初始化业务代码。
- 主文档更新后，必须按影响范围重新走开发流程。
- 不受影响的阶段可以跳过，但必须记录跳过原因和用户确认。
- 第一次完整开发流程包含两次验收：前端阶段验收、当前版本全量验收。
- 后续因需求或交互变更重新走流程时，只保留流程最后一次验收；验收范围可以收窄到受影响需求和交互。

## 阶段字典

| ID | 中文名称 | English Name | 需要用户验收 |
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
| 09_completed | 当前版本完成 | Completed | 否 |

## UI 项目流程

UI 项目必须使用 `rules/processes/ui-project.md`。Web App、SaaS、管理后台、移动端、小程序、带界面的工具都属于 UI 项目。

核心顺序：

1. PRD 与架构确认。
2. 制定 API 接口标准文档，用于前端 Mock 和后端实现。
3. 前端开发第一步必须以静态页面形式实现关键页面，用来确认页面风格。
4. 风格确认后开发全部相关页面并接入 Mock 数据。
5. 前端阶段验收；只有用户明确验收通过后才能进入后端开发。
6. 后端开发。
7. 前后端联调。
8. 当前版本全量验收。

## 非 UI 项目流程

非 UI 项目使用 `rules/processes/default-project.md`，并根据项目类型调整契约文档：

- 后端服务：API 或模块契约。
- Library/package：公共 API、兼容性和测试契约。
- Automation/script：输入、输出、副作用、失败处理契约。
- Data pipeline：数据源、数据模型、调度、质量校验契约。

## 跳过规则

agent 可以建议跳过阶段，但必须用户确认。记录内容包括：

- 被跳过阶段 ID 和中文名称。
- 跳过原因。
- 影响范围。
- 用户确认时间或确认语句。

未确认不得跳过。
