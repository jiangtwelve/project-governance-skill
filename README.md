# Project Governance — AI 驱动的项目治理系统

> 让 AI 写代码从黑盒走向可见可控。

`project-governance` 是一个 Claude Code skill，在项目根目录下生成一套完整的治理系统（`.project-governance/`）。

初始化之后，这套系统就不再依赖 skill 本身——治理规则、开发进度、决策日志全部留在项目目录中，切换 agent 也不会丢进度，整个流程对用户透明。

---

## 目录

- [为什么要做这个](#为什么要做这个)
- [三个设计原则](#三个设计原则)
- [功能一览](#功能一览)
- [快速开始](#快速开始)
- [使用流程](#使用流程)
- [文件结构](#文件结构)
- [规则速览](#规则速览)
- [注意事项](#注意事项)
- [常见问题](#常见问题)

---

## 为什么要做这个

AI 辅助开发越来越普遍，但大多数项目缺乏基本的治理：

1. **没有流程**——agent 上来就写代码，没有需求确认，没有架构设计，没有任务规划。
2. **文档混乱**——需求、架构、API 散落在各处，版本对不上，agent 不知道该信哪个。
3. **换环境就丢**——文档和流程绑在某个 agent 的上下文里，换了工具、换了人，全部重来。
4. **版本靠记忆**——没有版本管理，回溯和回归全靠人脑，项目状态说不清楚。
5. **术语各说各的**——用户说"用户"，文档写"Account"，代码叫 `member`，沟通成本很高。
6. **代码没人审**——AI 写完就过，逻辑漏洞和安全问题只有上线了才知道。

**典型场景：**

- 你在用 Claude Code 开发产品，希望每次写代码前有个明确的任务计划，写完后有人审查。
- 项目需要在 Claude Code、OpenCode、Codex 之间切换，希望治理文档能跟着项目走。
- 你手上有多个项目，希望把做过的开发流程沉淀下来，下一个项目能复用。
- 你希望"需求→架构→开发→验收"这条线被严格执行，而不是 AI 跳过步骤直接写。

---

## 三个设计原则

### ① 项目自有，不依赖 skill

在项目根目录下生成治理文件，由项目自身持有，和 AI 工具解耦。

- 治理规则写在项目文件里，不是 skill 的记忆，不是 agent 的上下文。skill 可以卸载，治理系统不动。
- 新 agent 读 `AGENT_BOOTSTRAP.md` 就能接盘——不需要重装 skill，不需要翻历史。
- 项目换到任何环境（Claude Code、OpenCode、Codex），治理直接可用。

### ② 上下文完整，不依赖会话

开发进度、决策记录、版本状态全部持久化在项目目录中，agent 换来换去也不丢。

- 当前版本、阶段、状态——记在 `PROJECT_STATE.md`。
- 需求、架构、API 决策——记在 `decisions/`。
- 术语对齐——记在 `GLOSSARY.md`。
- 任务计划、审查记录——记在 `processes/tasks/`。

会话断了？切 agent？换台电脑？治理文件一直在。

### ③ 流程透明，用户看得见

agent 按固定流程推进，每一步都有据可查。

- 四阶段骨架（需求确认 → 技术栈确认 → 实际开发 → 验收测试），不能跳过，不能合并。
- 写代码前先出 Task Plan，用户批准了才能动手。
- 代码改完先 Code Review，有问题修完了再继续。
- 有歧义的地方追问清楚，一次一问，确认了才算数。

用户随时知道"现在在做什么""做了什么决定""下一步是什么"。

---

## 功能一览

### 项目自有——治理资产沉淀在项目目录

- **完整目录结构**：初始化时生成 `.project-governance/`，含规则、SSOT、流程、决策、模板五类文件。
- **入口持久化**：在 `AGENTS.md` 和 `CLAUDE.md` 插入标记块，agent 启动时自动加载。
- **自校验脚本**：`check-governance.sh` 可以验证结构完整性，防止误操作破坏治理。
- **可卸载可迁移**：skill 卸载了治理照跑，项目换环境也能带走。

### 上下文独立——开发进度持久化

- **多版本 + Backlog + 回归**：每个版本独立追踪四阶段状态，历史版本锁定不变。Backlog 记下推迟的功能，开新版本时自动扫一遍。阶段可以回退，上下文不丢。
- **PROJECT_STATE 实时同步**：版本、阶段、回归、跳过记录都在文件里，任何 agent 接入就能读。
- **术语表**：用户口语 ↔ 文档术语 ↔ 代码标识 对照表，跨版本共享，换 agent 不用重新对齐。
- **决策日志**：需求、架构、流程决策写在 `decisions/INDEX.md` 里，切 agent 后不用重新讨论。
- **完整性检测**：每次调用 `/project-governance` 自动跑 `check-governance.sh`，发现缺失或不合规的文件会提示补全。

### 流程透明——开发过程可见可控

- **固定四阶段骨架**：需求确认 → 技术栈确认 → 实际开发 → 验收测试，不能改名、合并或跳过，用户始终知道项目在第几步。
- **Task Plan 前置**：写代码前先出颗粒级任务计划，用户明确批准了才能动手。每条任务产出不超过一个文件、预估不超过一小时，附带风险清单和"明确不做的事"。
- **Code Review 后置**：代码改完必须先过 Code Review，优先用独立审查能力（`/code-review`、`/security-review`），结果记入 `Review Log`。
- **追问协议**：有歧义的地方一次问一个问题，附推荐答案和理由。沉默和模糊赞同不算确认，防止 agent 跳过关键决策。
- **流程库沉淀**：首版验收通过时问你要不要沉淀流程到 `~/.claude/process-library/`。后续版本改过流程并走完一轮也会问，慢慢积累你自己的开发方法库。

---

## 快速开始

### 前提

- Claude Code（或其他兼容环境，如 OpenCode、Codex）
- 已安装 `project-governance` skill

### 用 /project-governance 一键搞定

在对话里直接调 skill 就行。支持四种场景：

| 场景 | 对话示例 | 干什么 |
|------|---------|--------|
| **初始化** | `/project-governance` | 新项目里生成完整的治理系统 |
| **文档导入** | `/project-governance 把现有的 PRD 和架构文档导入` | 扫项目已有文档，追问确认后整合进 SSOT |
| **升级版本** | `/project-governance 升级治理到最新版本` | 检测当前版本，做影响评估后升级 |
| **重新启用** | `/project-governance 重新启用治理` | 恢复停用的治理，扫停用期间的变更并更新状态 |

#### 初始化做了啥（以新项目为例）

1. **扫描**——读项目根目录、`AGENTS.md`、`CLAUDE.md`、README、清单文件、产品/架构/API 文档。
2. **分类**——判断是新项目、已有文档导入、已有治理升级还是重新启用。
3. **生成**——建 `.project-governance/`，往 `AGENTS.md` 和 `CLAUDE.md` 里插标记块。
4. **启动**——读 `AGENT_BOOTSTRAP.md`，开始走四阶段骨架。

#### 完整性检测

每次调 `/project-governance`，agent 会自动跑 `check-governance.sh`，检查：

- 所有必需文件有没有
- `AGENTS.md` 和 `CLAUDE.md` 的标记块在不在
- `PROJECT_STATE.md` 的必需章节全不全
- `acceptance_required` 阶段有没有对应的 Task Plan
- Task Plan 里 `Review Log` 建了没有、表头对不对

缺了什么东西，agent 会追问你要不要补。

### 备用方案：Python 脚本（agent 不可用时）

如果 skill 调不了，可以用脚本手动创建：

```bash
python scripts/init_governance.py \
  --project-root /path/to/your/project \
  --project-type saas-web-app \
  --scan
```

参数：

| 参数 | 说明 | 默认 |
|------|------|------|
| `--project-root` | 项目根目录 | `.` |
| `--project-type` | 项目类型（如 `saas-web-app`、`mobile-app`） | `TBD` |
| `--scan` | 扫描已有文档并建立导入索引 | 不扫 |
| `--skip-process-library` | 跳过创建 `~/.claude/process-library/` | 创建 |

Python 也没有？手动从 `assets/governance-template/` 把 `.project-governance/` 复制到项目根目录，填好 `AGENT_BOOTSTRAP.md` 的 metadata，把 `root/AGENTS.block.md` 和 `root/CLAUDE.block.md` 插到对应文件。

---

## 使用流程

### 一个版本的完整周期

```
第一阶段：需求确认
  ├── agent 和你讨论需求
  ├── 新概念先记到 Glossary
  ├── 有歧义就追问（一次一问）
  └── PRD 确认 → 阶段状态改为 Confirmed

第二阶段：技术栈确认
  ├── 查 ~/.claude/process-library/ 找可复用的流程
  ├── 和你商定开发流程 → 写入 processes/active.md
  ├── 完善架构文档
  ├── 补齐 Glossary 的代码标识符
  └── 架构和流程确认 → 阶段状态改为 Confirmed

第三阶段：实际开发
  ├── 每个 acceptance_required 阶段：
  │   ├── 起草 Task Plan → 你明确批准
  │   ├── 逐条执行任务
  │   ├── 每次改代码 → Code Review → 记入 Review Log
  │   └── 阶段完成 → 你确认
  └── 全部完成 → 阶段状态改为 Confirmed

第四阶段：验收测试
  ├── 你测试全部功能
  ├── 验收通过 → 阶段状态改为 Confirmed
  ├── agent 问：要不要把流程沉淀到流程库？
  ├── agent 问：要不要开新版本？
  └── 进入下个版本或收工
```

### 版本迭代

```
v1.0 ─► 走完四段
  │
  ├─ 你确认开 v2.0
  └─ Backlog 里哪些该进 v2.0？
       │
       v2.0 ─► 走完四段
```

---

## 文件结构

```
AGENTS.md                          ← project-governance 标记块（入口）
CLAUDE.md                          ← project-governance 标记块（入口）
.project-governance/
├── AGENT_BOOTSTRAP.md             agent 启东检查清单 + 红线摘要（新 agent 最先读这个）
│
├── rules/                         规则文件
│   ├── GRILLING_PROTOCOL.md       追问协议
│   ├── DEVELOPMENT_PROCESS.md     开发流程（四段骨架、Task Plan、Code Review）
│   ├── VERSION_RULES.md           版本规则
│   ├── DOCUMENTATION_RULES.md     文档规则
│   └── UPGRADE_RULES.md           治理升级规则
│
├── ssot/                          单一事实来源
│   ├── PRD.md                     产品需求文档
│   ├── ARCHITECTURE.md            技术架构文档
│   ├── API_CONTRACT.md            API 契约（无外部接口可标 n/a）
│   ├── PROJECT_STATE.md           项目状态
│   └── GLOSSARY.md                术语对照表
│
├── processes/                     开发流程
│   ├── active.md                  当前版本商定的流程
│   └── tasks/                     Task Plan（运行时创建）
│
├── decisions/                     决策日志
│   └── INDEX.md
│
├── imports/
│   └── SOURCE_INDEX.md            从项目扫到的现有文档索引
│
├── templates/
│   └── RECORD_TEMPLATES.md        所有记录的模板
│
└── scripts/
    └── check-governance.sh        治理完整性校验脚本
```

用户本地（不在项目内）：

```
~/.claude/process-library/         用户私有的可复用流程库
```

---

## 规则速览

| 规则 | 内容 | 出处 |
|------|------|------|
| **骨架红线** | 四段不可改名/合并/跳过；前两段未确认不能进开发 | `DEVELOPMENT_PROCESS.md` |
| **版本红线** | 当前版本没完不能开新版 | `VERSION_RULES.md` |
| **Task Plan 红线** | 编码前先出颗粒级 task plan，你批准了才能动手 | `DEVELOPMENT_PROCESS.md` |
| **Code Review 红线** | 代码改完先审查，CRITICAL/HIGH 问题修完才能继续 | `DEVELOPMENT_PROCESS.md` |
| **追问红线** | 有歧义就追问，一次一问，附建议和理由 | `GRILLING_PROTOCOL.md` |
| **术语红线** | 新概念进来先登记 Glossary | `GLOSSARY.md` |
| **文档红线** | 不能先写代码再补文档 | `DOCUMENTATION_RULES.md` |
| **流程库红线** | 第二段先进流程库看一眼 | `DEVELOPMENT_PROCESS.md` |

---

## 注意事项

### 使用注意

1. **手动调用**——skill 不会自动触发。需要你明确说"初始化治理""导入文档""升级治理""重新启用治理"。
2. **中文为主**——说明、规则、确认文本用中文；文件名、目录名、字段名、阶段 ID 用英文。
3. **确认 ≠ 模糊赞同**——"确认""同意""验收通过"才算。沉默、模糊赞同、agent 自己推断不算。
4. **Task Plan 批准是硬门槛**——你说"开始吧"不算，必须针对 task plan 文件说"过""确认""approve"。
5. **SSOT 优先**——现有文档只做输入索引，内容经过追问确认后才能进 SSOT。SSOT 永远是权威。
6. **流程库是私有的**——`~/.claude/process-library/` 不在项目里，不随 skill 分发，靠你的项目实践积累。

### 边界

- 面向**标准软件开发项目**（Web 应用、移动端、CLI 等）。纯研究型、一次性脚本可能需要裁剪。
- 第四段验收完了**才算版本结束**，之前 agent 会拒绝开新版本。
- 第三段里的流程动了，**没完成的 task plan 立刻失效**，得重新起草。
- Task Mutation Threshold 和 Process Mutation Threshold 默认都是 3，跑过一轮后你可以自己放宽到 5–7。

### 禁用治理

把 `AGENTS.md` 里 project-governance 标记块的 `Status: enabled` 改成 `disabled` 就行。`.project-governance/` 建议保留做历史资料。重新启用时，agent 会先扫停用期间的变更、更新状态，再恢复治理。

---

## 常见问题

<details>
<summary><strong>Q: 这个 skill 和 Claude Code 内置的规则有什么区别？</strong></summary>

`CLAUDE.md` 是行为指南，没有强制结构。`project-governance` 在此基础上加了完整的治理骨架：固定四阶段、版本管理、颗粒级 Task Plan、强制 Code Review、追问协议。而且可迁移——项目换到其他环境照样用。
</details>

<details>
<summary><strong>Q: 初始化后还能卸掉 skill 吗？</strong></summary>

能。治理文件是项目自己的，不依赖 skill。卸了之后系统照跑，新 agent 读 `AGENT_BOOTSTRAP.md` 就能接盘。需要升级治理时才需要装回来。
</details>

<details>
<summary><strong>Q: 骨架阶段能跳过吗？</strong></summary>

不能。四段是硬红线，不能改名、合并、跳过。但第三段内部的流程阶段可以通过 `optional: true` 标记为可跳过。
</details>

<details>
<summary><strong>Q: 阶段回归是什么？</strong></summary>

把已经 `Confirmed` 的阶段重新打开。比如开发到一半需求变了，就回到第一段改 PRD，改完再重新走。这不是失败，是正常路径。
</details>

<details>
<summary><strong>Q: 流程库怎么积累的？</strong></summary>

在 `~/.claude/process-library/`。首版验收通过时 agent 会问你要不要沉淀流程，后续版本改过流程并走完一轮也会问。沉淀的内容包含适用场景、阶段定义、经验教训等字段，你口述、agent 整理。
</details>

<details>
<summary><strong>Q: 项目没有外部 API，API_CONTRACT.md 还要吗？</strong></summary>

标成 `n/a` 就行，不占骨架阶段。
</details>

<details>
<summary><strong>Q: 版本号必须连续吗？</strong></summary>

不用。你说了算，1.0 → 1.8 → 2.4 都可以。版本号明显不合理时 agent 会提醒，但不会拒绝。你坚持就记入决策记录。
</details>

---

MIT License © 2026 江十二
