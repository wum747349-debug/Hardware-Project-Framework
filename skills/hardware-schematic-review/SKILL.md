# Hardware Schematic Review Skill

## 适用场景

本 Skill 提供 schematic review 方法，主要用于 Stage 4 Formal Schematic Review，也可在其他 Stage 对明确的 scoped review / risk-review 任务按需使用。Stage 3 日常模块设计、连接核对、参数计算和轻量 verification 默认由 `hardware-schematic-design` Skill 处理；读取或按需使用本 Skill 不自动改变 Project Stage，不自动构成 Stage 4 Formal Review，也不等同于 Stage 4 PASS 或 PCB Layout approval。

本 Skill 用于在进入 PCB Layout 前发现电源、接口、保护、最小系统、模拟前端和调试可达性问题。

## 适用项目范围

本 Skill 适用于常见低压嵌入式、电源管理、传感器采集、模拟前端和 MCU 控制类项目。高压、射频、高速数字、隔离、汽车、医疗或安规场景需增加专项检查方法。

## 最小读取上下文

使用本 Skill 时，AI 默认读取：

1. Layer 0/1：Project `FRAMEWORK.md`、`PROJECT_RULES.md` 与绑定 Framework 的 `docs/AI_Context_Guide.md`
2. 本 Skill

Stage 4 Formal Schematic Review 还默认读取当前 Project 的 `requirements.md`、`design_notes.md`、`references.md`，以及 component / footprint convergence 后由 authoritative `.SchDoc` 导出的当前完整原理图 PDF 与当前 BOM。Scoped review / risk review 只读取足以判断当前明确 scope 的 owning design context 与 evidence，不默认扩展为整板输入。

按需读取：

- 当前 Project 已有的 `docs/schematic_review.md`
- `skills/hardware-datasheet-reading/SKILL.md` 或 `skills/hardware-component-selection/SKILL.md`
- [Schematic Core Checklist](../../checklists/schematic_checklist.md)（Formal Review 使用完整适用范围；Scoped Review 只取对应项）
- 当前问题需要的 netlist、ERC、component / pin / footprint mapping 或 screenshot evidence

## 使用范围

### Formal Schematic Review

用于 Stage 4。Formal Review 在剩余 component / footprint convergence 已反映到 authoritative schematic 与当前 BOM 后开始；本 Skill 审查该 post-convergence completed whole-design evidence，不承担前置 procurement workflow。执行适用的完整检查范围，形成 formal findings 和 `docs/schematic_review.md`，并给出明确的 PCB Layout-entry conclusion。完整覆盖可以由对当前设计、适用范围和所需结论仍有效的既有 review evidence 与本次必要的增量检查共同满足，不等于重新执行全部检查；这不得削弱 post-convergence 完整原理图 PDF、当前 BOM 和整板适用范围的要求。

Formal Review 包含两个互补层次：

1. **Engineering Design Verification**：独立判断 current whole design 是否满足 requirements，topology 与 operating point 是否适用，关键 voltage / current / thermal / headroom / gain / bandwidth / filtering / ADC settling / timing 是否成立，startup / shutdown / default / fault behavior、protection、power integrity、cross-module interaction 与适用的 hardware–firmware feasibility 是否充分。
2. **EDA Implementation Verification**：核对当前 schematic / BOM 是否忠实实现上述 design intent，包括 pin / net、power / ground、decoupling、unused-pin handling、polarity、connector definition、symbol、package / footprint、pin-to-pad mapping 与 component identity consistency。

Independent verification 要求 reviewer 对是否接受当前设计作独立判断，但不要求对仍有可追溯依据、assumption 未变且未出现可信矛盾的 Stage 3 engineering rationale 机械重新推导。若发现真实 contradiction、evidence gap、changed assumption 或此前未覆盖的 mandatory review scope，则只重新评估受影响范围。

若 Formal Review 尚未开始就发现会影响设计或实现有效性的必要 component identity、pinout、package / footprint、connector definition 或其他 required design definition 仍未收敛，应报告 `NOT READY FOR FORMAL SCHEMATIC REVIEW — Stage 3 convergence incomplete`。**Missing required design definition is a readiness failure; a defined implementation proven incorrect is a review finding.**

### Scoped Review / Risk Review

用于一个明确限定的问题、模块、连接或风险。只读取足以判断当前 scope 的 evidence，只执行与该 scope 相关的 review checks，并输出 scope-bounded findings、risk、evidence limits 和 recommended action。

Scoped review / risk review 不默认要求完整整板原理图 PDF、完整整板 BOM、完整 schematic checklist、Stage 4 artifact、PCB Layout-entry conclusion 或 Stage 4 PASS。调用本 Skill 不会因此进入或满足 Stage 4。

## 审查输入能力边界

- `.SchDoc` 是 Altium 原理图的权威设计源文件，用于人工编辑、版本追踪和工程归档。
- 在没有可靠 Altium 解析器、脚本或自动化接口时，AI 不得声称已经读取、解析或核对 `.SchDoc` 内部电路。
- 原理图 PDF 主要用于图形连线、网络名和页面结构审查；BOM 用于核对位号、数量、参数或型号和 PCB 封装。Stage 4 Formal Schematic Review 使用 convergence 后同一 current design 的完整原理图 PDF 和当前版本 BOM 支持整板系统审查；无法由二者确认的实际网络、引脚映射、封装映射或其他 EDA 实现事项，应说明结论限制或标记为“待 EDA 核对”。
- BOM 最低字段不要求所有行都有具体制造商料号；关键器件缺少明确型号或封装时应记录具体缺失项，通用件可用参数、额定值、精度和封装描述。
- ERC 输出不是默认必需审查输入。AI 只有在用户提供 ERC 报告、Messages 导出或相关截图时，才分析 ERC 问题；未提供 ERC 输出时，不声称已经核对 ERC，不记录 ERC 执行或结果状态，也不把“未提供 ERC 输出”本身作为审查未完成或不能进入 PCB Layout 的理由。
- 网表、元件报告、引脚或封装映射报告和局部截图均为条件触发证据。局部截图可作为 scoped review 的局部证据，但结论必须受其覆盖范围限制；在 Formal Schematic Review 中只能补充局部证据，不能代替完整原理图 PDF。
- `requirements.md`、`design_notes.md` 和 `docs/module_design/*.md` 是需求和设计意图，不能单独证明 EDA 实现已经同步。
- Stage 4 可复用可追溯且足以覆盖当前目标的既有 review evidence；无需 schematic、PDF 或 BOM byte- / SHA-identical。复用前应判断该 evidence 与当前设计、适用范围和所需结论的关系；只对 changed、previously uncovered、evidence-insufficient，或因真实错误 / 新 evidence 而失效的受影响部分执行必要检查，不因局部修改机械重审全部模块。Reuse 不等于跳过 Stage 4，也不得因曾完成 Scoped Review 而虚构尚未完成的 Formal Review coverage，或把未验证的 ERC、EDA mapping 或 footprint mapping 升级为 PASS；ERC 未验证不因此自动成为 Stage 4 blocker。

## 形成检查范围与执行审查

按 [AI Context Guide](../../docs/AI_Context_Guide.md) 的 Checklist 分层指导，先从当前架构、能量流、信号流与已知风险确定实际模块，再以 [Schematic Core Checklist](../../checklists/schematic_checklist.md) 防遗漏。按电源与保护、功能模块、跨模块接口、封装与测试访问的依赖顺序审查，不因项目名称或 MCU 品牌固定套用整套清单。

对 Core 无法充分表达的器件 / 模块约束，从当前 Project Facts、schematic / BOM、Manufacturer official documentation 和已知风险推导具体检查项及判定依据。适用时参考 [STM32 条件片段](../../checklists/stm32_board_checklist.md)、[电池 / 电源条件片段](../../checklists/power_board_safety_checklist.md)、[模拟前端条件片段](../../checklists/analog_frontend_checklist.md)；这些只提供补充提示，不替代当前型号资料，也不用于无对应模块的项目。

在 `docs/schematic_review.md` 的现有审查记录中说明 Applicable Review Scope，例如 Core、实际 MCU、ADC / Reference、电池 / 电源、通信、保护与可测试性；项目不具备的模块不自动加入。关联检查依据、适用结论与 evidence gaps，再按上面的两个验证层次作独立判断。Formal Review 保持整板适用覆盖；Scoped Review 按其边界回写当前 owning record，不因此新建 Stage 4 文档。Skill 维护方法、风险和输出，逐项检查维护在 Checklist 或项目当前审查记录中。

## 输出格式

Formal Schematic Review 必须按以下完整格式输出：

### 当前结论

从以下三种中选择：

- 可以进入 PCB Layout：所有高风险问题已关闭；未关闭的中、低风险问题已有明确处置方案，且不影响板级安全、封装选择、接口定义和 PCB 关键布局。
- 修改后再进入 PCB Layout：仍存在会影响功能、封装、接口或布局的中风险问题。
- 存在高风险，暂不建议进入 PCB Layout：存在任何未关闭的高风险问题。

### 问题清单

| 编号 | 模块 | 问题描述 | 风险等级 | 建议修改 | 状态 | 证据或关联文件 |
|---|---|---|---|---|---|---|

状态建议统一使用：待决策、待修改、待核对、待 EDA 核对、已修改 / 待复核、已关闭。只有具备与问题类型相匹配的实现证据时，才能标记“已关闭”。

### 需要核对 datasheet 的项目

| 器件 | 需要核对的参数 | 核对原因 |
|---|---|---|

### 建议增加的测试点

| 网络 | 测试目的 | 是否必须 |
|---|---|---|

### 下一步操作

说明：

- 哪些地方必须修改
- 哪些地方建议优化
- 哪些资料需要补充
- 是否需要重新审查；如需要，明确实际触发原因、受影响范围和必要 evidence，不得只给出“建议再次全面审查”的笼统要求
- 是否可以进入 PCB Layout

Scoped review / risk review 可使用与 scope 对应的精简 findings，不要求套用上述完整格式；输出至少说明审查 scope、发现与风险、evidence limits 和 recommended action，不给出整板 PCB Layout-entry conclusion。

## 风险等级

- 高风险：可能损坏芯片、电池、电源，可能导致无法上电，或存在明显安全风险。
- 中风险：可能影响功能、稳定性、精度、温升、寿命或调试难度。
- 低风险：主要影响文档一致性、可读性、可维护性、丝印、测试便利性或后续整理。

## 结果记录

Formal Schematic Review 完成后，应提醒用户将结论写入或更新：

- 当前项目的 `docs/schematic_review.md`
- 必要时更新当前项目的 `design_notes.md`、当前 BOM、`requirements.md` 或 `docs/revision_history.md`

`docs/schematic_review.md` 的启用时机以 Project Structure Standard 的 Stage-enabled contract 为准；Stage 4 Formal Schematic Review 完成后更新其中的 findings、evidence limits 与 review result。

Scoped review / risk review 的结论如果具有长期价值，应记录回当前 owning design context、module record 或相关 Project fact owner；不得仅因调用本 Skill 就创建或要求创建 `docs/schematic_review.md`。

只有在实现证据足够、修改已由用户在 EDA 中完成并通过默认必需证据或与问题类型匹配的条件触发证据复核后，才能关闭对应问题；证据不足时标记为“待 EDA 核对”。高风险问题如果依赖 ERC、网表或封装映射才能关闭，则必须补充对应证据。

## 禁止事项

- 不要只说“看起来没问题”。
- Formal Review 不得跳过当前项目适用的高风险模块；Scoped Review / Risk Review 不得跳过其明确 scope 内的高风险因素。
- 不要在没有 datasheet 依据时确认关键连接完全正确。
- 不要把开源项目原理图当作最终依据。
- 不要忽略测试点、调试接口和首次上电安全检查。
- 不要建议用户直接进入 PCB Layout，除非所有高风险问题已经关闭；证据不足、待验证或待 EDA 核对的高风险问题均视为未关闭。
