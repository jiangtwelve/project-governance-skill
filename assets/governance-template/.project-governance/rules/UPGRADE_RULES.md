# Upgrade Rules

治理版本记录在 `AGENT_BOOTSTRAP.md` 的 Metadata 中，使用语义化版本。

| Version | Meaning | Default stage handling |
|---|---|---|
| `patch` | 不改变流程语义 | 不中断当前阶段 |
| `minor` | 新增能力或规则强化 | 继续当前阶段，补齐必要文档 |
| `major` | 可能改变阶段、验收、SSOT 或追问规则 | 必须做影响评估 |

## 升级

- 可以检测版本、生成 diff 和升级建议；不得静默修改治理规则。
- 修改 `.project-governance/rules/*` 前必须获得用户确认。
- 不得覆盖项目事实文档：`ssot/PRD.md`、`ssot/ARCHITECTURE.md`、`ssot/API_CONTRACT.md`、`ssot/PROJECT_STATE.md`。
- 升级必须写入 `changelog/GOVERNANCE_CHANGELOG.md`；文件不存在时按需创建。

开发中升级不得默认重置开发流程。必须评估当前阶段、新规则影响、已完成阶段、当前需求/交互/架构/API/验收、是否补齐产物、是否回退或重新验收；结论写入 `PROJECT_STATE.md` 和 `GOVERNANCE_CHANGELOG.md`。

## 停用与重启

- 用户可通过关闭 `AGENTS.md` 的 project-governance 入口停用；停用后不再强制执行 `.project-governance/`。
- 建议保留 `.project-governance/` 作历史资料；是否删除由用户决定。
- 重新启用前必须扫描停用期间的需求、架构、API、代码变化，更新 `PROJECT_STATE.md`，必要时更新 PRD/架构/API/决策记录，再恢复入口状态。
