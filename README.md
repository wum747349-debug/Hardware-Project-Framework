# Hardware Practice Projects

> 仓库状态：Repository Architecture Transition — Framework v1 RC1
> 当前仓库：`wum747349-debug/Hardware-Practice-Projects`
> 目标仓库名称：`Hardware-Project-Framework`（尚未切换）
> Framework 发布状态：RC1 已发布；Final 尚未发布

本仓库正在从 Legacy Monorepo 收敛为 Hardware Project Framework。Framework 定义方法和契约，不作为真实 Project 的活动事实源。当前 `projects/` 仍保留三个 Legacy Migration Source。Project 2 与 Project 3 的 Authority Cutover 均已完成；各自 Standalone Repository 是 Only Active Project Authority，Legacy Project 2 与 Legacy Project 3 仅作为 Frozen Migration Source 保留。Project 1 仍待 formal migration / cutover。

Framework v0.9 已建立 Standalone Project Template、初始化 Guide/Skill/Checklist、Project Validator、Framework Validator 与轻量 CI；Framework v1 RC1 现已发布。RC1 不是 Framework v1 Final，也不表示最终 Closeout 已完成。

## 普通用户入口

请从 [Framework User Guide](docs/Framework_User_Guide.md) 开始：`README → Framework User Guide → 按当前任务进入对应 Contract / Guide`。

## 架构边界

```text
Framework Repository
  Contract → Template → Validator → Reference/Test Fixture

Standalone Project Repository
  Binding + Runtime Rules + Project Facts + EDA/Evidence + Own Git History
```

一个正式 Project 只能有一个活动权威仓库。独立仓库完成验证和 Authority Cutover 前，Legacy 项目目录仍是当前权威；Cutover 后原目录只能作为 Frozen Migration Source，禁止长期双写。

## 八阶段项目流程

Project Bootstrap 位于八阶段之前，不是 Stage 0 或 Stage 1。Stage 1 建立第一版 Requirements Baseline，Gate 1.5 通过后才可进入 Stage 2。八个主阶段保持不变：

1. 需求确认阶段
2. 关键器件选型阶段
3. 原理图模块设计和绘制阶段
4. 原理图审查阶段
5. PCB 布局阶段
6. 布线和铺铜阶段
7. PCB 审查阶段
8. 焊接和硬件调试阶段

## Framework 工作入口

- [Framework 通用规则](PROJECT_RULES.md)
- [Project 结构与绑定契约](docs/Project_Structure_Standard.md)
- [Bootstrap、Gate 1.5 与八阶段 Workflow](docs/08_Project_Workflow.md)
- [AI 最小上下文指南](docs/AI_Context_Guide.md)
- [Template 使用与同步规则](docs/Project_Template_Guide.md)
- [Standalone Project 初始化指南](docs/Project_Initialization_Guide.md)
- [Framework Migration Guide](docs/Framework_Migration_Guide.md)
- [Framework Changelog](CHANGELOG.md)
- [Migration Baseline 历史记录](docs/Repository_Architecture_Migration_Baseline.md)
- [Standalone Project Template](templates/hardware_project_template/README.md)
- [Project Initialization Skill](skills/hardware-project-initialization/SKILL.md)
- [Gate 1.5 Checklist](checklists/project_initialization_checklist.md)

## Repository Architecture Transition

- Human roadmap：[Repository Architecture Migration Master Plan](docs/Repository_Architecture_Migration_Master_Plan.md)
- AI migration execution：[Repository Architecture Migration AI Runbook](docs/Repository_Architecture_Migration_AI_Runbook.md)
- Runtime Contract：[PROJECT_RULES.md](PROJECT_RULES.md)、[Project Structure Standard](docs/Project_Structure_Standard.md)、[Project Workflow](docs/08_Project_Workflow.md)、[AI Context Guide](docs/AI_Context_Guide.md)

Master Plan 是 human-facing 一次性迁移路线；AI Runbook 是 migration-only AI operational guide。两者都不属于 Standalone Project Runtime Contract，不复制到 Project Template 或真实 Project，也不改变八阶段 Workflow。

## Validation

```bash
python scripts/validate_framework_repository.py
python scripts/validate_project_repository.py templates/hardware_project_template --template
```

复制到 Standalone Project 后可在项目根运行：

```bash
python scripts/validate_project_repository.py
python scripts/validate_project_repository.py --gate-1-5
```

## 当前事实

- Baseline Tag：`framework-pre-v1-migration`
- Baseline Commit：`3e9d4801bdd5768f8edc0e14e8f01bf278721e54`
- 当前 GitHub Repository 尚未重命名。
- Legacy monorepo projects 仍存在；Legacy Project 2 与 Legacy Project 3 已冻结为 Migration Source，Project 1 仍待 formal migration / cutover。
- Framework v1 RC1 已发布；Final 和最终 Reference Project 尚未发布或建立。
- `development-v0.9` 只用于 Framework 自测或明确预发布评估，不是正式 Release。
