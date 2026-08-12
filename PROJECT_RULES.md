# PROJECT_RULES

## 1. 仓库身份与当前状态

本仓库当前身份是 `wum747349-debug/Hardware-Project-Framework`；Repository Architecture Migration 已关闭，Framework v1.0.0 已发布，仓库进入 Normal Framework Maintenance。旧 Repository identity 仍可作为历史 provenance 或既有 Project 的 immutable binding 保留，不因 Rename 或新 Release 自动改写。

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
- Framework binding update 必须由用户明确要求并锁定目标 identity + immutable Commit。Prerelease dogfooding 使用 Pinned Framework Evaluation；上述 Contract 语义均未改变的 backward-compatible adoption 使用 Compatible Framework Sync；发生任何 Runtime / Structural Contract 实质变化时，才使用 Framework Contract Migration 并执行完整差异审查、Project adaptation、验证与一次 Human Approval。所有路径都执行适用 validation，不得自动跟随 Framework `main`；仅在结构契约变化时更新 `Project Structure Version`。
- Framework Repository 的 normal maintenance、Semantic Versioning、risk-driven optional RC、candidate validation 与 Release publication 由 `docs/Framework_Maintenance_and_Release_Guide.md` 管理。RC 不是所有 Release 的 mandatory gate；每个新目标版本从 `rc1` 重新编号，Final 发布后不得继续该版本的 RC。Framework `main` 的普通 commit 不自动要求 Release。

版本语义不得混淆：Framework Release 表示方法发布；Project Structure Version 表示项目仓库结构契约；Hardware Revision 表示硬件设计版本；Git tag/commit 表示源码身份。

后续 Stage 反馈必须按影响范围处理，不自动重新打开旧 RC、Framework Migration 或 Authority Cutover：

- Project-specific issue 留在对应 Project 处理；
- Documentation、Skill 或 Checklist usability issue 进入 normal Framework maintenance；
- 不改变 Contract 的 Validator bug 作为 compatible Framework fix；
- Runtime / Structural Contract 的实质变化进入新的 Framework Contract Migration 和适当的后续版本；
- Final v1 发布后发现问题不回到旧的 `v1.0.0-rc2` 路线，而按正常版本演进处理：`v1.0.x` 用于 compatible fixes，`v1.x.0` 用于 backward-compatible improvements，`v2.0.0` 用于 breaking Runtime / Structural Contract change。

Final v1 只表示发布候选已满足既定 Contract 与验证要求，不表示未来所有 Stage 2–8 engineering scenario 已被穷尽验证；真实 Project 在 Final publication 后继续提供反馈。

## 7. Authority Cutover

迁移前，Legacy Monorepo Project Directory 是 Current Authority。独立仓库完成验证并执行 Cutover 后，Standalone Project Repository 成为 Only Active Project Authority，原目录降级为 Frozen Migration Source：不继续开发、不再修改项目事实、只用于迁移核对，且在新仓库确认完整前不删除。禁止长期双写。

Repository Architecture Migration 的一次性路线已关闭，不属于 Project Runtime Contract。Migration Master Plan 是 Historical Engineering Record，Migration AI Runbook 已 retired；两者不再维护当前计划或执行路由。未来若显式发生新的 Legacy / previous authority → Standalone Project Repository 切换，仍按 `docs/Framework_Migration_Guide.md` 的独立 Authority Cutover procedure 执行，不得改变上述单一活动权威源、Cutover 后冻结 Legacy Source 和禁止长期双写的稳定规则。

## 8. Git 安全

- 修改前和交付前检查工作树、分支、远端、上游和 diff。
- 保留用户已有修改与未跟踪资料；无法安全分离时停止。
- 只显式暂存本次文件，禁止 `git add .` 和 `git add -A`。
- 不 force push，不移动 Baseline Tag，不用破坏性方式处理冲突或非 fast-forward。
- 不将日志、缓存、临时项目、数据库、敏感信息或 `.git/config` 混入提交。
