# Agent Bootstrap

本项目启用了 `project-governance` 治理体系。除非 `AGENTS.md` 中的 project-governance block 已被明确设置为 `Status: disabled`，否则所有 agent 必须遵守本文件。

## 启动顺序

每次开始项目工作前，按顺序读取：

1. `.project-governance/ssot/PROJECT_STATE.md`
2. `.project-governance/rules/GRILLING_PROTOCOL.md`
3. `.project-governance/rules/DEVELOPMENT_PROCESS.md`
4. `.project-governance/rules/DOCUMENTATION_RULES.md`
5. `.project-governance/rules/LOGGING_RULES.md`
6. 与任务相关的 SSOT、流程、验收、决策文件

默认只读取 `.project-governance/decisions/INDEX.md`。只有当当前任务需要追溯某个决策原因时，才读取对应的单个决策文件。

## 强制规则

- 不允许“快速开始写代码，文档以后再补”。
- 在 PRD、架构、阶段状态确认前，不得进入代码实现。
- 任何需求、交互、架构、接口、数据模型、流程阶段存在歧义时，必须执行追问协议。
- 需求或交互变化必须更新 `.project-governance/ssot/PRD.md` 并留痕。
- 架构、接口、数据模型、部署方式变化必须更新对应 SSOT 并留痕。
- 主文档更新后，必须按影响范围重新走开发流程；不受影响的阶段只能在用户明确确认后跳过。
- 验收和关键确认只能来自用户明确表达，agent 不得自行推断。
- 开始工作前读取 `PROJECT_STATE.md`，结束后若状态发生实质变化则更新它。

## 文件索引

| 文件 | 作用 |
|---|---|
| `.project-governance/ssot/PRD.md` | 需求 SSOT 与需求变更摘要 |
| `.project-governance/ssot/ARCHITECTURE.md` | 架构 SSOT 与架构变更摘要 |
| `.project-governance/ssot/API_CONTRACT.md` | 前端 Mock 与后端实现的接口契约 |
| `.project-governance/ssot/PROJECT_STATE.md` | 当前状态快照，不做历史日志 |
| `.project-governance/rules/GRILLING_PROTOCOL.md` | 内置追问协议 |
| `.project-governance/rules/DEVELOPMENT_PROCESS.md` | 阶段状态机与流程规则 |
| `.project-governance/rules/UPGRADE_RULES.md` | 治理系统升级、停用、重新启用规则 |
| `.project-governance/decisions/INDEX.md` | 决策日志索引 |
| `.project-governance/imports/SOURCE_INDEX.md` | 已有文档导入索引 |
