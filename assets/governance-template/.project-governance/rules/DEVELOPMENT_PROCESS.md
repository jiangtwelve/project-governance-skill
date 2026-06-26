# Development Process

开发流程的可变性受当前阶段约束。跨流程的硬规则在 `AGENT_BOOTSTRAP.md`，本文件只列流程专属规则。

## 流程可变性

流程只有两种状态：可变（Mutable）与冻结（Frozen），状态写在 `ssot/PROJECT_STATE.md` 的 `Process State` 字段。

- **可变**：当且仅当当前阶段为 `01_prd_architecture_confirmation`（首次 PRD 与架构确认）或显式标记的需求改动阶段（PRD/架构出现变化、流程回退到 01 的状态）。
- **冻结**：一旦用户明确确认进入下一阶段（`02_api_contract` 或之后任意阶段），流程立刻冻结。后续阶段必须严格按当时冻结的流程定义执行。

### 何时允许动态修改流程

只有在"可变"状态下，agent 才可以基于当前需求评估流程是否适用，并提出修改建议（增删阶段、调整顺序、替换默认流程为自定义流程）。修改必须满足：

1. 由 agent 按追问协议给出建议与理由，用户明确确认。
2. 修改结果落到 `rules/processes/<project-slug>.md`（自定义流程文件），不要直接改默认的 `rules/processes/ui-project.md`。
3. 在 `.project-governance/decisions/` 写入一条决策记录，说明为什么改、改了什么。
4. 同步更新 `ssot/PROJECT_STATE.md` 的 `Active Process` 字段，指向新的流程文件。

### 进入开发阶段之后

- 流程冻结后，agent **不允许**修改流程定义、跳过流程要求的阶段或私自变更阶段顺序。
- 如果开发中发现当前流程与实际需求不匹配，必须先：
  1. 在 `ssot/PROJECT_STATE.md` 标注需要回退，列出原因和影响范围；
  2. 由用户明确确认"回到需求讨论阶段"；
  3. 把 `Current Stage` 改回 `01_prd_architecture_confirmation`，`Process State` 改回 `Mutable`；
  4. 才能开始讨论流程调整。
- 未经上述流程，任何流程改动都视为违规，agent 必须停下来向用户报告。

## 流程规则

- 不受影响的阶段可由 agent 建议、用户明确确认后跳过；跳过仍是冻结流程内的一次性豁免，不算修改流程。
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

- UI 项目默认使用 `rules/processes/ui-project.md`；项目可在可变阶段派生自定义流程。
- 非 UI 项目使用默认流程：PRD 与架构确认 -> 契约确认 -> 核心实现 -> 测试验证 -> 当前版本全量验收。
- Web App、SaaS、管理后台、移动端、小程序、带界面的工具都属于 UI 项目。

默认流程同样要求：有歧义必须追问；需求变化更新 PRD；架构、契约、数据模型变化更新对应 SSOT；完成前必须获得用户明确验收；跳过阶段必须由用户确认。

## 跳过记录

跳过阶段时，在 `ssot/PROJECT_STATE.md` 记录：阶段 ID、中文名称、跳过原因、影响范围、用户确认。
