# Upgrade Rules

## 版本规则

治理系统版本记录在 `MANIFEST.md`，使用语义化版本：

- `patch`：不改变流程语义，默认不中断当前阶段。
- `minor`：新增能力或规则强化，默认继续当前阶段，但需要补齐必要文档。
- `major`：可能改变阶段、验收、SSOT 或追问规则，必须做影响评估。

## 升级原则

- 新版 skill 可以自动检测版本、生成 diff 和升级建议。
- 不允许静默修改治理规则。
- 用户确认后才能修改 `.project-governance/rules/*`。
- 升级不得覆盖项目事实文档：`ssot/PRD.md`、`ssot/ARCHITECTURE.md`、`ssot/API_CONTRACT.md`、`ssot/PROJECT_STATE.md`。
- 所有升级必须写入 `changelog/GOVERNANCE_CHANGELOG.md`；文件不存在时按需创建。

## 开发中升级

治理升级不得默认重置开发流程。升级后必须评估：

- 当前阶段。
- 新规则影响哪些已完成阶段。
- 是否影响当前需求、交互、架构、API 或验收。
- 是否需要补齐阶段产物。
- 是否需要回退或重新验收。

评估结论写入 `PROJECT_STATE.md` 和 `GOVERNANCE_CHANGELOG.md`。

## 停用

用户可以通过关闭 `AGENTS.md` 中的 project-governance 入口直接停用本治理体系。停用后，agent 不再强制执行 `.project-governance/` 内的流程。

建议保留 `.project-governance/` 作为历史资料；是否删除由用户决定。

## 重新启用

重新启用前必须同步停用期间的变化：

- 扫描停用期间的需求、架构、API、代码变化。
- 更新 `PROJECT_STATE.md`。
- 必要时更新 PRD、架构、API 契约和决策记录。
- 同步完成后再恢复 `AGENTS.md` 入口状态。
