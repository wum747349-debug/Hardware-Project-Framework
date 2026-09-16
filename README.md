# Hardware Project Framework

> 仓库状态：Normal Framework Maintenance
> 当前仓库：`wum747349-debug/Hardware-Project-Framework`
> Framework target release line：v1.2.1；正式 publication 状态以 GitHub tag / Release 为准

本仓库是处于 normal maintenance lifecycle 的 Hardware Project Framework。Framework 定义方法和契约，不作为真实 Project 的活动事实源。Repository Architecture Migration 已关闭；Project 1 / 2 / 3 均已完成 Authority Cutover，各自 Standalone Repository 是 Only Active Project Authority。Framework current Git tree 只保留轻量 [history marker](projects/README.md)，迁移细节作为历史工程记录保存。

Framework v1.2.1 的 release-level changes、compatibility 与 SemVer 信息记录在 [Framework Changelog](CHANGELOG.md)；准确 publication 状态由 GitHub tag / Release 证明。今后的 Framework Repository maintenance、Semantic Versioning、optional risk-driven RC 与 Release publication 由 [Framework Maintenance and Release Guide](docs/Framework_Maintenance_and_Release_Guide.md) 管理；Existing Project 是否以及如何采用 immutable Framework Release 由 [Framework Migration Guide](docs/Framework_Migration_Guide.md) 管理。Framework `main` 或新 Release 均不自动 rebind Standalone Project。

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

- [Framework 用户指南](docs/Framework_User_Guide.md)
- [Framework Maintenance and Release Guide](docs/Framework_Maintenance_and_Release_Guide.md)
- [Framework Migration Guide](docs/Framework_Migration_Guide.md)
- [Framework 通用规则](PROJECT_RULES.md)
- [Project 结构与绑定契约](docs/Project_Structure_Standard.md)
- [Bootstrap、Gate 1.5 与八阶段 Workflow](docs/08_Project_Workflow.md)
- [AI 最小上下文指南](docs/AI_Context_Guide.md)
- [Template 使用与同步规则](docs/Project_Template_Guide.md)
- [Standalone Project 初始化指南](docs/Project_Initialization_Guide.md)
- [Framework Changelog](CHANGELOG.md)
- [Standalone Project Template](templates/hardware_project_template/README.md)
- [Synthetic Reference Project](examples/reference_project_v1/README.md)
- [Project Initialization Skill](skills/hardware-project-initialization/SKILL.md)
- [Gate 1.5 Checklist](checklists/project_initialization_checklist.md)
- [Bring-up 与硬件测试 Checklist](checklists/bringup_test_checklist.md)

## Repository Architecture Migration 历史记录

- [Migration Master Plan — CLOSED / Historical](docs/Repository_Architecture_Migration_Master_Plan.md)
- [Migration AI Runbook — RETIRED](docs/Repository_Architecture_Migration_AI_Runbook.md)
- [Migration Baseline — Historical provenance](docs/Repository_Architecture_Migration_Baseline.md)

这些文件只用于历史工程追溯，不是普通用户或 AI 的主要工作入口，不维护 Current Phase、Next transaction、current Project status 或 current release roadmap。它们都不属于 Standalone Project Runtime Contract，不复制到 Project Template 或真实 Project，也不改变八阶段 Workflow。

## Validation

Framework maintenance 使用一个 canonical full validation entry point；该命令已聚合 Template、Reference Project、smoke 与 regression coverage：

```bash
python scripts/validate_framework_repository.py
```

Standalone Project 继续使用独立 Project Validator，在项目根运行：

```bash
python scripts/validate_project_repository.py
python scripts/validate_project_repository.py --gate-1-5
```

## 当前事实

- Baseline Tag：`framework-pre-v1-migration`
- Baseline Commit：`3e9d4801bdd5768f8edc0e14e8f01bf278721e54`
- 当前 GitHub Repository 已重命名为 `wum747349-debug/Hardware-Project-Framework`。
- Repository Architecture Migration：`CLOSED — historical only`。
- Framework operating mode：`NORMAL MAINTENANCE`。
- Framework v1.2.1：当前 target release line；release-level summary 见 `CHANGELOG.md`，正式 publication 状态以 GitHub tag / Release 为准。
- Project 1 / 2 / 3 Standalone Repository 均为各自 Only Active Project Authority。
- Framework current Git tree 不再保存三个真实 Legacy Project copy；历史可通过 Git history、baseline tag 与 migration records 追溯。
- `examples/reference_project_v1/` 已建立为 synthetic、lightweight、validator-valid fixture，不是第四个真实 Project。
- Framework v0.9 是 v1.0.0-rc1 之前的 historical Executable Candidate，不是当前 Release。
- Framework `main` 的普通 commit 不自动要求 Release，也不自动修改任何 Project binding。
