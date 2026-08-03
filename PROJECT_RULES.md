# PROJECT_RULES

## 1. 仓库身份与当前状态

本仓库当前仍是 `wum747349-debug/Hardware-Practice-Projects`，处于 Legacy Monorepo 向 Framework Repository 过渡期间。目标名称是 `Hardware-Project-Framework`，但在后续仓库身份切换完成前，文档、脚本和绑定不得假装 GitHub Repository 已经改名。

Framework 定义硬件项目的方法和契约，不作为真实 Project 的活动事实源。当前 `projects/` 中的内容属于 Legacy Migration Source；在各项目完成独立仓库验证和 Authority Cutover 前不得删除，也不得被提取为 Framework 默认器件、网络、规则值、板框或制造参数。

## 2. Framework / Project 权威边界

Framework Repository 保存：通用运行规则、项目结构标准、八阶段 Workflow、AI Context Routing、Bootstrap 与 Gate 1.5、Template、Skill、Checklist、Validator、Changelog、Migration Guide，以及后续阶段建立的轻量 Reference Project。

正式 Standalone Project Repository 保存：项目身份、当前阶段、需求、设计事实、器件决策、项目资料、EDA 权威源、BOM、Review、Manufacturing、Bring-up、Test、Revision，以及自己的 Git history、issue 和 release。

必须遵守：

- 一个正式 Project 只能有一个活动权威仓库；
- Framework 只定义方法与契约，不维护真实 Project 的活动副本；
- 其他 Project、Template 和 Reference Project 都不能作为当前 Project 的事实源；
- 项目当前阶段只在该 Project 根 `README.md` 维护；
- `.SchDoc` 与 `.PcbDoc` 分别是原理图和 PCB 的权威 EDA 实现源。

结构、文件职责与绑定契约以 `docs/Project_Structure_Standard.md` 为准；阶段顺序与门禁以 `docs/08_Project_Workflow.md` 为准；读取范围以 `docs/AI_Context_Guide.md` 为准。

## 3. Legacy Monorepo / Framework Era

仓库历史分为：

```text
Legacy Monorepo Era
        ↓
Repository Architecture Transition
        ↓
Framework Era
```

- 不重写原仓库历史；Legacy commits 中存在真实 Project 是允许的。
- `framework-pre-v1-migration` 是不可移动的 Legacy Monorepo 恢复点。
- Framework Era 的当前工作树最终不维护真实 Project 活动副本；历史可继续由 Git 追溯。
- 默认禁止为追求“历史绝对干净”执行 `git filter-repo`、force push 或移动 Baseline Tag。

## 4. 渐进式硬件设计与资料依据

- 先确认需求和模块边界，再围绕当前决策分批选择关键器件、读取资料、反推外围并完善 BOM。
- 不要求项目一开始收集全部 datasheet；普通阻容、LED、排针和测试点等不影响架构的器件可以后置。
- 官方 datasheet、reference manual 和 application note 是关键参数的主要依据。
- 商品页只可用于库存、价格、封装、料号和资料入口，不能替代官方资料。
- 开源项目只可学习结构、方法和文档组织；不得直接复制其原理图、PCB、BOM、Gerber、生产文件或源工程作为项目成果。
- 电源、电池、MOSFET、ADC 输入保护、运放供电、参考电压及其他安全风险必须回到官方资料核对。

## 5. EDA、制造与实测证据边界

- 无可靠解析器、脚本或自动化接口时，AI/Codex 不得声称读取、解析或核对 `.SchDoc` / `.PcbDoc` 内部电路、对象、规则、Scope、Priority、铺铜或 DRC 状态。
- AI/Codex 不得声称自行运行 Altium、ERC、Repour、Batch DRC、制造输出、焊接或实测；只分析用户提供的实际结果并说明证据限制。
- 文档中的需求与设计意图不能单独证明 EDA 实现已同步，PCB 图片也不能证明网络、精确规则命中、铺铜或 DRC 通过。
- 完整 Batch DRC 只在阶段 7 的 PCB Release Review 与制造放行前由用户运行；阶段 5 的 Layout Preflight 不要求初始 DRC，阶段 6 不要求归档中间 DRC。
- 制造极限不能直接作为项目默认设计值；设计值必须结合可靠性、装配、成本和工艺波动保留合理裕量。

## 6. Framework Release、绑定与升级

- 正式 Project 必须通过 `FRAMEWORK.md` 锁定一个 Framework Release 和对应不可歧义的完整 Commit SHA。
- Project 不默认跟随或读取 Framework `main`。
- 正式 Bootstrap 必须从固定 Framework Release 获取 Template；开发绑定只允许用于 Framework 自测和明确的预发布评估。
- Framework 升级必须显式执行 migration；只有完成差异审查、结构/内容迁移和验证后，才更新 `Framework Release`、`Framework Commit`，并在需要时更新 `Project Structure Version`。
- 发布顺序为 Baseline → Release Candidate → Final。RC 后若 Required files、`FRAMEWORK.md` schema、Project `AGENTS.md`、Gate 1.5、Runtime Rules、目录职责、Structure Version 或 Validator required structure 实质变化，必须发布新的 RC，不得继续声称旧 RC 已验证。

版本语义不得混淆：Framework Release 表示方法发布；Project Structure Version 表示项目仓库结构契约；Hardware Revision 表示硬件设计版本；Git tag/commit 表示源码身份。

## 7. Authority Cutover 与迁移阶段语义

迁移前，Legacy Monorepo Project Directory 是 Current Authority。独立仓库完成验证并执行 Cutover 后，Standalone Project Repository 成为 Only Active Project Authority，原目录降级为 Frozen Migration Source：不继续开发、不再修改项目事实、只用于迁移核对，且在新仓库确认完整前不删除。禁止长期双写。

仓库架构整改阶段语义固定为：

- Phase 3：Project 2 Pilot + Initial Authority Cutover；
- Phase 4：Project 3 Clean Bootstrap + Initial Authority Cutover；
- Phase 6：Formal Migration Closeout，包括 Project 2 final migration verification、Project 3 final migration verification，以及 Project 1 formal standalone migration。

Phase 6 不得第二次创建或拆分 Project 2 / Project 3。

## 8. Git 安全

- 修改前和交付前检查工作树、分支、远端、上游和 diff。
- 保留用户已有修改与未跟踪资料；无法安全分离时停止。
- 只显式暂存本次文件，禁止 `git add .` 和 `git add -A`。
- 不 force push，不移动 Baseline Tag，不用破坏性方式处理冲突或非 fast-forward。
- 不将日志、缓存、临时项目、数据库、敏感信息或 `.git/config` 混入提交。
