# Repository Architecture Migration Baseline

> Document Status: Historical Baseline / Provenance Record
> Current-state authority: No

## 1. Purpose

本文记录 `Hardware-Practice-Projects` 从 Legacy Monorepo 向 Hardware Project Framework + Standalone Project Repositories 架构整改前的 Git Baseline。

本文件仅保存 Phase 0 冻结时的恢复点、结构摘要和项目阶段事实，不是 Framework v1 契约，也不提前定义 Phase 1 的最终实施细节。

### Historical Terminology Note

本文保留原始 Baseline Freeze 当时使用的 migration terminology。文中的 `Phase 0` 与旧 Phase 1～8 migration model 仅是历史术语；Repository Architecture Migration 已关闭，本文件与 [Repository Architecture Migration Master Plan](Repository_Architecture_Migration_Master_Plan.md) 都不是 current-state authority。

## 2. Repository Baseline

| Item | Baseline value |
| --- | --- |
| Repository | `wum747349-debug/Hardware-Practice-Projects` |
| Remote | `origin` |
| Branch | `main` |
| Baseline Tag | `framework-pre-v1-migration` |
| Baseline Commit SHA | `3e9d4801bdd5768f8edc0e14e8f01bf278721e54` |
| Baseline Commit Message | `chore: ignore local workspace materials` |
| Baseline Commit Timestamp | `2026-08-03T19:43:44+08:00` |
| Baseline Freeze Date | `2026-08-03` |

该 SHA 是任何 Phase 0 基线记录文档提交之前，当前可靠且已与 `origin/main` 同步的原始 `main` HEAD。后续记录 Phase 0 的文档 commit 不属于 pre-migration Baseline，且不会移动 Baseline Tag。

## 3. Repository Model at Baseline

Baseline 时仓库仍属于 Legacy Monorepo 模型：

```text
Legacy Monorepo
├─ Repository-level rules / templates / skills / checklists
├─ Project 1
├─ Project 2
└─ Project 3
```

仓库级方法、模板、工具和三个硬件 Project 仍保存在同一个 Git repository 中；尚未实施 Framework 与 Standalone Project Repositories 的目标架构。

## 4. Structural Snapshot

Baseline commit 的主要顶层入口如下。此处只提供便于人工理解的摘要；完整、精确的 tracked 文件快照由 Baseline Tag 保存。

```text
.gitattributes
.github/
.gitignore
AGENTS.md
PROJECT_RULES.md
README.md
checklists/
common/
docs/
images/
projects/
prompts/
references/
scripts/
skills/
templates/
```

三个现有 Project 路径为：

```text
projects/01_STM32_DAQ_Control_Board
projects/02_LiIon_Charger_Protection_Board
projects/03_STM32_OpAmp_ADC_Acquisition_Board
```

## 5. Project State Snapshot

项目当前阶段只取自各项目根 `README.md`，不根据目录内容、文件数量、设计成熟度或其他记录推断。

| Project | Path | Authoritative stage source | Current stage at Baseline | Notes |
| --- | --- | --- | --- | --- |
| Project 1 — STM32 DAQ Control Board | `projects/01_STM32_DAQ_Control_Board` | `projects/01_STM32_DAQ_Control_Board/README.md` | Stage 7 — PCB 审查阶段 | 根 README 明确声明“当前项目阶段：阶段 7：PCB 审查阶段”；Phase 0 未修改或推进该阶段。 |
| Project 2 — Li-Ion Charger Protection Board | `projects/02_LiIon_Charger_Protection_Board` | `projects/02_LiIon_Charger_Protection_Board/README.md` | 未在权威项目根 README 中明确声明 | Existing Baseline gap；不得推断为 Stage 1。 |
| Project 3 — STM32 OpAmp ADC Acquisition Board | `projects/03_STM32_OpAmp_ADC_Acquisition_Board` | `projects/03_STM32_OpAmp_ADC_Acquisition_Board/README.md` | 未在权威项目根 README 中明确声明 | Existing Baseline gap；不得自行推断阶段。 |

## 6. Baseline Gaps

- Project 2 的项目根 `README.md` 在 Baseline 时未声明权威的当前项目阶段。
- Project 3 的项目根 `README.md` 在 Baseline 时未声明权威的当前项目阶段。

以上是 Baseline 已存在的事实缺口，Phase 0 只记录、不修复。

## 7. Phase 0 Non-Goals

Phase 0 没有执行以下工作：

- 拆分 Project repositories；
- 删除 `projects/`；
- 重命名 GitHub repository；
- Standalone Template 改造；
- 引入 `FRAMEWORK.md`；
- 实现 Gate 1.5；
- 重构 Validator；
- 创建 Reference Project；
- 迁移 EDA 文件；
- 推进或重写任何 Project 阶段；
- 修改任何 Project 的硬件设计；
- 实施其他 Phase 1～8 架构整改内容。

## 8. Recovery Point

`framework-pre-v1-migration` 是 Framework v1 架构整改前 Legacy Monorepo 的不可变恢复点。可使用以下非破坏性命令检查该恢复点：

```bash
git show framework-pre-v1-migration
git switch --detach framework-pre-v1-migration
```

如需长期恢复或开展对照工作，应从该 Tag 新建 recovery branch，而不是覆盖、移动该 Tag，也不要破坏当前 `main`：

```bash
git switch -c recovery/framework-pre-v1-migration framework-pre-v1-migration
```
