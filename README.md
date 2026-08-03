# Hardware Practice Projects

> 仓库状态：Repository Architecture Transition — Framework v1 Contract
> 当前仓库：`wum747349-debug/Hardware-Practice-Projects`
> 目标仓库名称：`Hardware-Project-Framework`（尚未切换）
> Framework 发布状态：尚未发布 RC 或 Final

本仓库正在从 Legacy Monorepo 收敛为 Hardware Project Framework。Framework 定义方法和契约，不作为真实 Project 的活动事实源。当前 `projects/` 仍保留三个 Legacy Migration Source；本阶段没有拆分、迁移或删除任何真实 Project。

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
- [Phase 0 Baseline 记录](docs/Repository_Architecture_Migration_Baseline.md)
- [Standalone Project Template](templates/hardware_project_template/README.md)

## 当前事实

- Baseline Tag：`framework-pre-v1-migration`
- Baseline Commit：`3e9d4801bdd5768f8edc0e14e8f01bf278721e54`
- 当前 GitHub Repository 尚未重命名。
- Legacy monorepo projects 仍存在，尚未执行 Project 2 / 3 Authority Cutover。
- Framework v1 RC、Final 和最终 Reference Project 均尚未发布或建立。

## Repository Architecture Migration 语义

- Phase 3：Project 2 Pilot + Initial Authority Cutover。
- Phase 4：Project 3 Clean Bootstrap + Initial Authority Cutover。
- Phase 6：Formal Migration Closeout；只做 Project 2 / 3 最终迁移验证和 Project 1 正式独立迁移，不第二次拆分 Project 2 / 3。

详细权威规则见 `PROJECT_RULES.md` 与 `docs/Project_Structure_Standard.md`。
