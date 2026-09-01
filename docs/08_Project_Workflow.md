# Hardware Project Workflow

> 文档状态：Framework v1 Contract
> 适用范围：Project Bootstrap、Gate 1.5 与八个硬件主阶段
> 权威职责：Lifecycle、进入/退出/回退条件与阶段门

## 1. Lifecycle

```text
Project Bootstrap
        ↓
Stage 1 — Requirements Definition
        ↓
Gate 1.5 — Project Initialization & Requirements Baseline
        ↓
Stage 2 → Stage 3 → Stage 4 → Stage 5 → Stage 6 → Stage 7 → Stage 8
```

Bootstrap 位于八阶段之前，不是 Stage 0，也不属于 Stage 1。Gate 1.5 位于 Stage 1 与 Stage 2 之间，只检查初始化和第一版 Requirements Baseline，不产生器件、原理图、PCB、DRC、制造或测试结果。

项目结构、绑定 schema 和 Stage-enabled 路径以 [Project Structure Standard](Project_Structure_Standard.md) 为准；AI 读取范围以 [AI Context Guide](AI_Context_Guide.md) 为准；执行方法由对应 Skill 维护；逐项检查由 checklist 维护。

## 2. 通用原则

- 八个主阶段的数量和顺序保持不变；datasheet、BOM、制造输出、测试与改版是阶段内活动。
- 项目当前阶段只在根 `README.md` 的唯一字段维护，不能由文件存在推断。
- Required 文件在 Bootstrap 建立；Conditional 内容按项目需要建立；Stage-enabled 文件只在进入相关工作时创建。
- 规则文件描述“应该是什么”，Review、DRC、Bring-up 和 Test 记录描述“实际是否做到”。
- `.SchDoc` / `.PcbDoc` 是权威 EDA 实现源；无可靠解析能力时 AI 不声称读取内部对象或运行 Altium、ERC、Repour、DRC。
- 证据不足的结论必须明确限制或标记 `TBD` / `待确认` / `待 EDA 核对` / `待用户确认` / `待实测`。
- 回退到上游阶段后，所有受影响下游 Gate 必须重新评估。

### Stage exit 与授权转换

Stage exit / readiness conclusion 只是技术就绪结论。例如“可以进入 PCB Layout / Layout Preflight”不表示根 `README.md` 的 `Current Project Stage` 已改变，不表示下一 Stage 已自动执行或完成，也不授权修改 repository state。

只有用户明确授权完成 transition / 进入下一 Stage 时，AI/Codex 才能执行 Stage transition。获授权的 transition 必须作为一个 bounded、validation-closed transaction 规划和交付：在 transaction 完成时，根 `README.md` 已指向 target Stage，且 [Project Structure Standard](Project_Structure_Standard.md) 定义为该 target Stage entry 立即启用、Project Validator 在该 post-state 立即要求的 Stage-enabled artifacts 已存在，final Project Validator 对该 post-state 通过。只要原授权已经覆盖完成 transition / 进入下一 Stage，不应把 `README.md` 更新与上述 artifact activation 人为拆成需要第二次授权的两个 transaction。

若 target Stage entry 需要的 artifact 尚不存在，可在同一 authorized transition 中做 minimum truthful initialization。初始化只能记录已确认的 Project facts、已有工程事实、有实际职责的结构，以及真实的 `TBD`、`待确认` 或 `Pending <relevant activity>`；不得为 Validator、文件完整度或 transition completion 虚构工程参数，也不得创建只有标题或没有职责内容的低信息量 placeholder。Artifact activation 只建立 target-stage 合法 repository state，不表示 target-stage engineering activity 已开始，更不表示该 Stage 已完成。

用户明确给出的更窄 Exact Scope 始终优先。若用户限定只能修改 A、B，而合法 target-stage post-state 还必须创建或修改 C，则不得自行扩大 scope，也不得提交 partial transition；应停止并报告 blocker。上述规则解决 transition scope planning，不构成 scope override。仅由 target Stage 中实际 activity 触发的 artifact 不因 Stage entry 自动创建，具体 activation condition 以 Project Structure Standard 为准。

## 3. Project Bootstrap

### 目标

建立独立 Project 容器、Project Identity、Framework Binding 和 Required 入口，使 Project 可以在不依赖 monorepo 路径或本地 Framework 目录的情况下继续 Stage 1。

### 输入

- 一个用于初始化的固定 Framework Release；
- 该 Release 对应的 immutable commit；
- Project 名称与活动权威仓库位置；
- Template 与 Project Validator 发布快照。

### 活动

1. 从固定 Framework Release 获取 `templates/hardware_project_template/`，不复制 Framework `main` 的漂移工作树。
2. 创建结构标准定义的全部 Required 文件与职责目录。
3. 填写 Project Identity 和 `FRAMEWORK.md` binding；尚未正式发布时的 Framework 自测使用明确 Development Binding。
4. 将根 `README.md` 当前状态设为 `Bootstrap`，建立项目导航。
5. 清除必须替换的 Template placeholder；未知项目事实保留为 `TBD`、`待确认` 或 Draft，不虚构答案。
6. 只按实际需要启用 Conditional 内容，不预建 Stage-enabled 文件。

### 允许状态

Bootstrap 允许 Draft、TBD 与待确认，但禁止为清除占位符而虚构器件、参数、原理图、PCB、ERC、DRC、Manufacturing 或 Test。

### 输出与退出条件

- Project Identity 唯一且不含其他 Project 残留；
- `FRAMEWORK.md` schema 完整，Release + Commit 不含歧义；
- Required files 齐全，导航链接有效；
- Project Validator 可在 Standalone Project 中独立运行；
- 根 `README.md` 可以真实切换到 Stage 1。

Bootstrap 完成只证明项目容器可用，不证明 Requirements Baseline 已建立。

## 4. Stage 1 — Requirements Definition

### 目标

建立第一版 Requirements Baseline，明确做什么、不做什么、模块边界及进入关键器件选型所需的工程约束。

### 必需输入

- 已完成的 Project Bootstrap；
- 项目用途、应用场景和第一版约束；
- 已知电源、接口、负载、安全、成本、尺寸、制造与装配要求。

### 主要活动

- 记录项目目标与第一版不做内容；
- 定义功能边界和模块边界；
- 建立主要能量流、信号流与接口需求；
- 记录电源、安全、误接、首次上电和调试边界；
- 建立制造基础要求与机械/装配约束；
- 定义可验证的验收标准；
- 将未决事项记录为待确认问题，并说明影响与核对计划。

### 主要输出

- `requirements.md` 第一版 baseline；
- `block_diagram.md` 第一版模块、能量流和信号流；
- `design_notes.md` 的整板设计意图入口；
- `references.md` 的资料需求入口；
- 根 `README.md` 的真实 Stage 1 状态与导航。

### 退出条件

目标、不做内容、功能/模块/电源/接口/安全/制造边界、验收标准和待确认问题足以支撑 Gate 1.5；未知项没有被虚构为已确认事实。

Stage 1 完成后必须执行 Gate 1.5，不能直接进入 Stage 2。

## 5. Gate 1.5 — Project Initialization & Requirements Baseline

### 位置与职责

Gate 1.5 位于 Stage 1 与 Stage 2 之间。它验证 Project 容器、Framework Binding、事实入口和第一版 Requirements Baseline 是否可用；不产生设计结果。

### 检查范围

- Project Identity 唯一且与当前仓库一致；
- Framework Repository、Release、Commit、Project Structure Version、Repository Model、Initialization Framework Release 与 Status 完整一致；
- 根事实入口齐全，根 `README.md` 是当前阶段唯一事实源；
- README Navigation 的必要相对链接有效；
- Template placeholder 已替换，`TBD` / `待确认` 仅作为真实未决状态存在；
- 不含未标注的其他 Project facts 或非法旧 monorepo runtime dependency；显式标注的 Source Repository、Legacy Project Path 等 migration provenance 可以保留；
- Required 齐全，Conditional 未被误判为 Required，Stage-enabled 内容未为目录整齐提前预建；
- 无职责的空目录和低信息量文件不存在；
- Stage 1 Requirements Baseline 覆盖目标、不做内容、功能/模块/电源/接口/安全/制造边界、验收标准和待确认问题；
- 尚未开始的选型、EDA、Review、DRC、Manufacturing、Bring-up、Test 明确保持未开始/未验证状态；
- 没有提前产生或声称后续阶段结论。

### 结论与授权边界

全部阻断项关闭、Gate Validator 通过且人工事实审查无阻断项时，technical conclusion 为 `READY`；任何阻断项存在时为 `NOT READY`，Project 保持 Stage 1 / `Gate 1.5 Pending`。

Read-only request 只允许输出 `READY / NOT READY`，不得记录 Gate PASS、不得把 `Initialization Status` 更新为 `Initialized`、不得推进 Stage。Explicit execution request 已明确要求执行 Gate 1.5、完成初始化或在条件满足后进入下一阶段时，该请求本身构成 execution authorization；若结论为 `READY`，无需第二次 approval round-trip，可直接记录 Gate 1.5 PASS、将 `Initialization Status` 更新为 `Initialized`，再运行 final Project Validator。只有 final Project Validator 通过后才允许进入 Stage 2。

`READY` 本身从不授权状态变化。该简化不新增或删除 Gate，也不削弱用户控制；它只删除重复的 separate approval round-trip。

Gate 1.5 PASS 是进入 Stage 2 的必要条件，但不证明任何关键器件、EDA 或验证结果。

逐项执行使用 `checklists/project_initialization_checklist.md`，自动结构检查使用 Project Validator；人工事实判断不能由 Validator 完全替代。

## 6. Stage 2 — Critical Component Selection

### 目标与活动

选择影响架构、外围、封装、布局、散热和采购的关键器件，依据官方资料形成主选、备选与淘汰理由。普通阻容等不影响架构的器件可以后置。

### 进入条件

Gate 1.5 已 PASS，Requirements Baseline 足以筛选器件。

### 主要输出与退出条件

启用 `docs/component_selection_plan.md` 并由其维护 selection decision。只有 `design_notes.md` 负责的整板架构/跨模块事实或 `references.md` 负责的资料索引与核对事实实际变化时，才更新相应文件。影响架构/封装/Layout 的关键器件有可靠依据或明确核对计划，候选记录未被误写为最终 BOM。

需求、供电、接口、尺寸、装配或制造边界因器件选择实质变化时回到 Stage 1 并重新执行 Gate 1.5。

## 7. Stage 3 — Schematic Module Design and Capture

### 目标与活动

使用 `skills/hardware-schematic-design/SKILL.md`，依据 Requirements、器件决策和关键资料按需执行 module planning、module-by-module design、parameter calculation、EDA capture guidance 与 Cross-Module Integration Check；完成模块连接、外围参数、startup / fault behavior、保护与专项 Layout 输入。由用户在 Altium Designer 中实现正式原理图并导出同版完整原理图 PDF 与当前 BOM。

### 进入条件

关键器件与资料足以确定当前模块方向。

### 主要输出与退出条件

Stage 3 entry 至少启用一个 owning module design record，承接当前 detailed design work；是否按模块拆分更多 `docs/module_design/*.md` 仍由复杂度和追溯价值决定，不要求每个模块各有一份文件。形成可追溯模块依据、BOM 草稿、Altium 原理图、同版完整 PDF 与当前 BOM，并完成轻量整板自洽检查。满足 Stage 3 条件时只报告 `READY FOR SCHEMATIC REVIEW`；该结论不等于 ERC PASS、Stage 4 PASS 或 PCB Layout approval，也不自行改变 `Current Project Stage`。AI 不声称完成 EDA 实现。

**No automatic reverse implementation sync：**普通 resistor / capacitor、pull-up、net naming、support component、module pin connection、filter 或 NTC 外围值调整，通常只更新当前 module design record；若 underlying component decision、qualification basis、architecture impact、selection risk 或 requirement 实质变化，则更新对应 owner，并按影响范围返回相关 Stage reevaluation。Stage 2 artifacts 不是 immutable，但不因普通实现调整而机械同步。

器件/资料不成立回到 Stage 2；需求或模块边界冲突回到 Stage 1 与 Gate 1.5。

## 8. Stage 4 — Schematic Review

### 目标与活动

依据可追溯完整原理图 PDF、当前 BOM、Requirements、Design Notes、References 与模块资料，审查供电、接口、保护、封装、引脚、板级安全与关键 Layout 输入。只在用户提供 ERC 结果时分析 ERC。

### 主要输出与退出条件

启用 `docs/schematic_review.md`。高风险及影响封装、接口、安全和关键 Layout 的问题关闭；其他问题有明确处置；给出是否允许进入 Layout Preflight 的显式技术结论。该 Stage exit conclusion 不自行执行 Stage 4 → Stage 5 transition。

器件或封装问题回 Stage 2；连接/参数问题回 Stage 3；功能/安全边界变化回 Stage 1 与 Gate 1.5。

## 9. Stage 5 — PCB Layout

### 目标与活动

完成 Layout Preflight、制造/机械基线、封装核对、规则值、Scope、Priority 与关键布局。用户在 Altium 配置并人工核对实际规则。

### 主要输出与退出条件

启用 `docs/pcb_design_rules.md`，并在需要记录 Preflight 时启用唯一的 `docs/pcb_review.md`。规则基线与关键布局前置条件满足，无阻断正式布局的问题。

Stage 5 不要求初始 DRC，也不以 DRC 作为正式布局门禁。制造/机械基线变化回 Stage 1 与 Gate 1.5；原理图问题回 Stage 3/4。

## 10. Stage 6 — Routing and Copper

### 目标与活动

完成布线、换层、回流路径、过孔、热与铺铜；用户在相关修改后执行 Repour，并可按需使用实时或临时检查。

### 主要输出与退出条件

完成可追溯 `.PcbDoc` 与 Review 输入；若 Stage 5 尚未因记录 Layout Preflight 而启用 `docs/pcb_review.md`，则在进入 Stage 6 的 authorized transition 中启用它，Stage 6/7 继续维护同一文件并记录需要跨回合追踪的重要问题，不创建第二份 artifact。计划布局布线铺铜完成，关键路径已人工检查，重要问题已处理。

Stage 6 不要求保存、导出或归档中间 DRC 记录，也不以中间 DRC 作为继续工作的仓库门禁。

## 11. Stage 7 — PCB Release Review

### 目标与活动

无歧义识别 exact release candidate，确认当前 evidence 足以支持放行判断；由用户对该版本运行 Final Full Batch DRC，识别实际 manufacturing-data / submission path，审查一个对该路径所用最终制造数据忠实且能力足够的 manufacturing interpretation，确认适用的制造与下单参数，处理 findings / waivers，并给出显式 Manufacturing Release Decision。PCBA 与 special fabrication 只在项目实际需要时触发。

Stage 7 不重复已完成的 Stage 5–6 design-quality review；只有未关闭的 Stage 6 finding 或 Stage 7 design delta 需要重新评估时，才按影响范围调用 PCB Layout / Routing 方法。Evidence 选择、充分性、新鲜度与持久化边界以 [AI Context Guide](AI_Context_Guide.md) 为准，具体方法与逐项核对分别由 PCB Release Skill 与 Release Checklist 维护。

### 主要输出与退出条件

在 `docs/pcb_review.md` 留下最小 durable summary，使 release candidate、Final Full Batch DRC、actual manufacturing-data path、final manufacturing interpretation、findings / waivers、适用的 conditional review 与 Manufacturing Release Decision 可追溯。退出前，用户确认当前 release candidate 的完整 Batch DRC 已运行；实际违规已解决或具有批准的合理豁免；实际提交路径与最终制造解读已确认；放行结论已显式记录。

AI 的 evidence 使用与能力边界按 AI Context Guide 和 PCB Release Skill 执行；不声称自行运行工具、导出输出或批准制造。

## 12. Stage 8 — Assembly, Bring-up and Hardware Test

### 目标与活动

安全完成装配、首次限流上电、下载通信、功能/性能/边界验证，记录条件、期望、实测、异常和改版影响。

### 主要输出与退出条件

按实际活动启用 `docs/bringup_log.md`、`docs/test_report.md`，必要时启用 `docs/revision_history.md`。核心功能与验收边界已测试，未测项和异常有明确后续，记录可追溯到硬件版本。

AI 生成计划并分析用户数据；用户负责实际焊接、上电、测量与测试。

## 13. 完成后的维护

项目展示、简历整理、仓库导航和经验复盘不作为第九阶段。只有测试与实际职责有可追溯证据时，才能写成已完成成果。
