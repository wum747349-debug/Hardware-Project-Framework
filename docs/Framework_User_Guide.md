# Framework 用户指南（Framework User Guide）

> 面向对象（Audience）：Human User
>
> Runtime Contract：No
>
> 用途（Purpose）：解释与导航，不定义新的 Framework Contract

Framework 与 Standalone Project 的 human-facing documentation 默认采用 Chinese-first：以中文作为主要解释语言，同时保留必要英文正式术语、工程缩写、文件名和固定字段。完整 Documentation Language / Readability convention 以 [AI Context Guide](AI_Context_Guide.md) 为权威；本指南只负责解释和导航，不创建第二规则源，也不创建 Framework Contract、Project Runtime Rule、Stage Rule 或 Human Approval Rule。

## 1. Framework 是什么

Hardware Project Framework 为硬件项目提供可复用的工程方法、仓库结构规则、Template、Validator 和 AI 上下文指引。

Framework Repository 定义：

- 项目方法和 Contract；
- Template 和验证工具；
- Workflow、Stage 与 Guide。

Standalone Project Repository 保存真实 Project 事实：

- requirements 和设计决策；
- EDA 源文件；
- Evidence、测试记录和 Project history。

Framework 不是任何真实 Project 的活动事实源。

## 2. Framework Repository 与 Standalone Project Repository

```text
Framework Repository
Contract → Template → Validator → Guide

Standalone Project Repository
Binding → Runtime Rules → Project Facts → EDA / Evidence → Project History
```

Project 使用 `FRAMEWORK.md` 记录的固定 Framework Release 和 immutable Commit，不会自动跟随 Framework `main`。

## 3. 如何创建一个新 Project

推荐阅读路径：

```text
README
→ Framework User Guide
→ 当前任务需要的 Contract / Guide
```

典型流程：

1. 创建 Standalone Project Repository。
2. 从固定 Framework Release 的 Template 初始化。
3. 完成 Bootstrap 和 Stage 1 requirements。
4. 通过 Gate 1.5 后才能进入 Stage 2。

未知事实应保留为 `TBD` 或待确认，不得为了通过结构检查而伪造工程事实。

操作顺序见 [Project Initialization Guide](Project_Initialization_Guide.md)，Template 边界见 [Project Template Guide](Project_Template_Guide.md)，结构与 Binding 见 [Project Structure Standard](Project_Structure_Standard.md)，Lifecycle 与 Gate 见 [Project Workflow](08_Project_Workflow.md)。本指南不复制这些文档的完整规则。

## 4. 如何继续已有 Project

继续一个已有 Project 时：

1. 从 Project `README.md` 查看 current stage 和 Project Facts 导航。
2. 从 `FRAMEWORK.md` 查看当前 Framework Binding。
3. 读取 Project `PROJECT_RULES.md` 了解 project runtime rules。
4. 从已绑定的 Framework snapshot 取得当前任务需要的 Stage Method、Guide、Skill 和 Checklist。

当前 Project Repository 始终是项目特定事实的权威源。按已绑定 snapshot 中的 [AI Context Guide](AI_Context_Guide.md) 只加载当前任务所需 Project Facts、Stage Method 和 Evidence；不默认读取 Framework `main` 或其他 Project。

以上是用户了解进度的阅读路径；AI 的启动顺序仍由 Project `AGENTS.md` 指向 `FRAMEWORK.md`、`PROJECT_RULES.md` 和绑定快照中的 AI Context Guide。用户阅读与 AI 执行共用同一批事实，不需要另一份 AI 状态记录。

Project README 用简短说明呈现项目身份、当前阶段、状态摘要、事实导航与下一步。需要理解设计依据时进入 requirements / design 文档，需要核对完成情况时进入对应 Review、Bring-up 或 Test 记录与实际证据。README 的进度摘要帮助理解这些记录，不代替它们，也不把待验证工作写成已完成；具体文件职责见 [Structure Standard](Project_Structure_Standard.md)。

## 5. AI 可以做什么，哪些动作需要 Human Approval

在已授权的任务范围内，AI 可以直接协助：

- documentation 准备；
- read-only review、diff inspection、Evidence 整理和工程分析；
- 结构、链接、Validator 和 CI 检查；
- 已授权范围内的文档、Validator 和工具维护；
- 明确暂存、普通 commit 与 push。

这些常规动作不授权 AI 虚构 Project Facts、声称未执行的 EDA 或物理工作，也不授权高影响状态变更。

以下动作仍需要 Human Approval：

- Project Hardware Stage advancement；
- Gate 1.5 Human PASS；
- Framework Contract Migration；
- Authority Cutover；
- RC / Final publication；
- Repository Rename；
- Legacy deletion / destructive cleanup。

常规 documentation、review、Validator、CI、diff inspection、Evidence 整理以及授权任务内的普通 commit / push 不制造重复 Human Gate。Framework maintenance / Release publication 见 [Framework Maintenance and Release Guide](Framework_Maintenance_and_Release_Guide.md)；Project adoption 与 Authority Cutover 见 [Framework Migration Guide](Framework_Migration_Guide.md)。权威职责与审批边界仍以 [Framework Rules](../PROJECT_RULES.md) 和 [Project Workflow](08_Project_Workflow.md) 为准。

## 6. Framework 更新：Compatible Framework Sync 与 Framework Contract Migration

### 兼容 Framework 同步（Compatible Framework Sync）

用于目标 Framework Release + immutable Commit 固定，且 Runtime / Structural Contract 语义保持不变的兼容更新。它仍需要明确用户任务与验证，但不另行制造重复 Human Approval Gate。

### Framework Contract Migration

用于 schema、structure、lifecycle、authority、Project fact responsibility、validator required structure 等 Contract 语义发生实质变化的情况。它需按权威 Guide 完成影响审查、Project adaptation、验证、rollback plan 和 Human Approval。

完整分类与执行流程见 [Framework Migration Guide](Framework_Migration_Guide.md)；本节只做易懂解释，不替代该 Guide。

## 7. 应该去哪里查看真实状态和事实

| 问题 | 查阅入口（操作说明仍回源到对应 Contract） |
| --- | --- |
| 当前 Framework Binding | Project `FRAMEWORK.md` |
| 当前 Project Stage | Project `README.md` |
| 当前 Requirements | Project `requirements.md` |
| Project Facts / Evidence | 当前 Project 自身的事实文件和证据，从其 `README.md` 导航 |
| Repository Structure / Binding 职责 | [Project Structure Standard](Project_Structure_Standard.md) |
| Bootstrap / Gate 1.5 操作 | [Project Initialization Guide](Project_Initialization_Guide.md) |
| Stage lifecycle | [Project Workflow](08_Project_Workflow.md) |
| AI context routing | [AI Context Guide](AI_Context_Guide.md) |
| Framework maintenance / Release | [Framework Maintenance and Release Guide](Framework_Maintenance_and_Release_Guide.md) |
| Project Framework adoption | [Framework Migration Guide](Framework_Migration_Guide.md) |

## 8. 不同角色应该阅读哪些文档

Human User：

- 仓库 `README.md` 和本 Framework User Guide；
- 继续已有 Project 时，读取当前 Project 的 `README.md`、`FRAMEWORK.md`、requirements 和任务相关事实；
- 创建 Project 时，读取 [Project Initialization Guide](Project_Initialization_Guide.md)。

Project Creator：

- 本指南；
- [Project Initialization Guide](Project_Initialization_Guide.md)；
- [Project Structure Standard](Project_Structure_Standard.md)；
- [Project Workflow](08_Project_Workflow.md)；
- [Project Template Guide](Project_Template_Guide.md)。

Framework Maintainer：

- [Framework Rules](../PROJECT_RULES.md)；
- [Project Structure Standard](Project_Structure_Standard.md)、[Project Workflow](08_Project_Workflow.md) 和 [AI Context Guide](AI_Context_Guide.md)；
- [Framework Maintenance and Release Guide](Framework_Maintenance_and_Release_Guide.md) 与 [Framework Migration Guide](Framework_Migration_Guide.md)；
- [Project Template Guide](Project_Template_Guide.md) 与 [Project Initialization Guide](Project_Initialization_Guide.md)；
- 只按当前任务需要读取受影响的 Validator、Skill、Checklist 和 CI 文档。

## 9. Repository Architecture Migration 历史记录

Repository Architecture Migration 已关闭。[Repository Architecture Migration Master Plan](Repository_Architecture_Migration_Master_Plan.md) 是 closed historical engineering record，[Repository Architecture Migration AI Runbook](Repository_Architecture_Migration_AI_Runbook.md) 已 retired。

两者只在显式历史 architecture / provenance review 时按需读取，不是 Standalone Project Runtime Contract，也不是 normal Framework maintenance 或普通 Project 工作的默认阅读路径。
