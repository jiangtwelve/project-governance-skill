# Documentation Rules

## SSOT

`.project-governance/ssot/*` 是项目开发的权威来源：

- `PRD.md`：产品需求、用户流程、交互要求、需求变更摘要。
- `ARCHITECTURE.md`：技术架构、模块边界、数据模型、部署约束、架构变更摘要。
- `API_CONTRACT.md`：接口契约，是前端 Mock 和后端实现的共同标准。
- `PROJECT_STATE.md`：当前阶段、完成项、下一步、阻塞和关键事实。

## 变更留痕

- 需求或交互变化必须更新 `PRD.md` 的 `Change History`。
- 架构变化必须更新 `ARCHITECTURE.md` 的 `Change History`。
- API 契约变化必须更新 `API_CONTRACT.md` 的 `Change History`。
- 详细讨论和权衡不要塞进 SSOT 主文档，写入 `decisions/` 单独文件。

## 现有文档导入

- 原始文档不移动、不删除。
- 导入过程记录在 `imports/SOURCE_INDEX.md`。
- 从原始文档提炼出的内容必须经过追问和用户确认后，才能进入 SSOT。
- 原始文档被确认导入后不再作为权威来源；若与 SSOT 冲突，以 SSOT 为准。
- 用户最新明确确认的结论优先于原始文档，但必须写入 SSOT 和决策记录。

## 语言策略

- 说明、规则、确认文本、流程解释用中文为主。
- 文件名、目录名、字段名、阶段 ID 使用英文稳定索引。
- 阶段名必须同时保留中文名称和英文名称。
