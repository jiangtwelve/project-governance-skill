# Grilling Protocol

本协议内置 `grill-me` 的核心行为，不依赖外部 skill。

## 何时追问

必须追问：新项目/功能/版本/需求；需求、交互、架构、技术栈、数据模型、API、部署变化；验收不通过后的修改方向；多路线反馈；文档、代码、用户口述冲突；任何影响阶段、SSOT 或验收标准的决定。

通常可豁免：明确 bug 修复、测试补充、格式/拼写、无行为变化重命名、不改变行为的依赖升级、用户已完整说明的小任务。豁免时说明“不影响 PRD、架构、API 和流程”。

## 怎么追问

- 一次只问一个关键问题，并给出推荐答案。
- 先解决上游决策，再问下游细节。
- 能通过读项目文件回答的，先读文件，不问用户。
- 用户明确确认前，不得把争议假设写入 PRD、架构、API 或代码。

## 什么算确认

只有用户明确表达“确认”“同意”“按这个方案做”“验收通过”“进入下一阶段”或等价授权，才算确认。沉默、模糊赞同、agent 自行判断都不算确认。

## 追问后写哪里

- 需求/交互：`ssot/PRD.md`
- 架构/数据模型/部署：`ssot/ARCHITECTURE.md`
- 接口：`ssot/API_CONTRACT.md`
- 阶段/下一步：`ssot/PROJECT_STATE.md`
- 长期原因和权衡：`.project-governance/decisions/NNNN-title.md` + `.project-governance/decisions/INDEX.md`
