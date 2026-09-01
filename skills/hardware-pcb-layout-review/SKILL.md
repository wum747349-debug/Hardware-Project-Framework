---
name: hardware-pcb-layout-review
description: Guide and review PCB placement, routing, copper, return paths, and related rule preparation. Use for Layout Preflight, Interactive Placement, Interactive Routing, Layout / Routing Review, or Rule Scope / Altium Rule Priority review during Stage 5–6.
---

# PCB Layout / Routing

## 1. 目的与边界

本 Skill 用于低压嵌入式、MCU 控制、传感器采集、电源管理、模拟前端和通信接口板的 Stage 5–6 PCB Layout / Routing 协作：

1. **Mode A — Layout Preflight**：确认正式布局前的制造、机械、封装、原理图门禁和规则基线。
2. **Mode B — PCB Layout / Routing Work**：逐步指导 Placement / Routing，并正式审查布局、关键路径、布线、回流、过孔和铺铜。
高压、射频、复杂高速数字、隔离电源、汽车、医疗、安规、HDI 或刚挠结合项目只能复用本 Skill 的通用部分，必须增加专项方法、checklist、标准和有资质的审查。

本 Skill 只维护方法、判断逻辑、风险分类、输出结论和能力边界。逐项检查使用：

- [PCB Layout Preflight Checklist](../../checklists/pcb_layout_preflight_checklist.md)
- [PCB Layout Checklist](../../checklists/pcb_layout_checklist.md)

项目规则值写入 `docs/pcb_design_rules.md`；需要跨回合追踪的 Layout / Routing 问题与 Formal Review 结论写入 `docs/pcb_review.md`。Stage 7 由 `hardware-pcb-release-review` 负责。

## 2. 选择模式

| 用户请求                                                        | 模式                                      | 必需结论                                              |
| ----------------------------------------------------------- | --------------------------------------- | ------------------------------------------------- |
| 是否可开始布局、规则准备                                                | **Mode A — Layout Preflight**           | `批准开始正式布局` / `不批准开始正式布局`                          |
| “现在先摆什么？”、“哪些器件必须靠近？”、“下一步移动哪些器件？”或逐步完成布局                   | **B1 — Interactive Placement Guidance** | 工程指导；不要求每轮给出正式阶段门结论                               |
| “下一根线先走什么？”、“当前模块先走哪些网络？”或逐步解决 routing conflict                 | **B2 — Interactive Routing Guidance**  | 工程指导；不要求每轮给出正式阶段门结论                               |
| 已有 Placement / Routing Evidence 的布局、布线、铺铜、回流或 PCB 图片正式/明确审查 | **B3 — Layout / Routing Review**        | `可进入 PCB Release Review` / `修改后复审` / `存在高风险，停止推进` |

跨正式审查模式的 Stage 5–6 请求按 A → B3 顺序处理并分别给出阶段门结论，后续证据不能抵消前一阶段的阻断项。B1 / B2 可在 Mode B 内的任意合理 Placement / Routing 增量中使用，不应被强制包装为 Formal Review。

## 3. 最小上下文

默认、按需和禁止读取范围以 `docs/AI_Context_Guide.md` 的 Stage / Task context table 为准；本 Skill 不重复维护文件清单。

执行时仍按第 2 节选择 Layout Preflight、B1、B2 或 B3，并按下文对应方法、证据边界和 checklist 完成工作。

## 4. 能力与证据边界

- `.PcbDoc` 是 PCB 权威实现源文件。没有可靠解析器、脚本或自动化接口时，不声称读取其内部对象、网络、规则、层、铺铜、尺寸或属性。
- PCB 图片只支持视觉判断，不能证明网络、精确间距、线宽、孔径、环宽、规则命中、铺铜状态、未布线数量或 DRC 通过。
- 不声称运行 Altium Designer、配置规则、布线、Repour、Batch DRC 或导出制造文件。
- 实际规则配置、Rule Scope / Altium Rule Priority 核对、布局布线、Repour、DRC 和导出均由用户执行。
- 无法由当前证据确认的实现项标记为 `待 EDA 核对`。
- 始终区分“文档已定义”“用户确认 AD 已配置”“用户提供 DRC 结果”三种状态。

## 5. 模式 A 方法：Layout Preflight

1. 确认项目、硬件版本、原理图审查结论和未关闭高风险问题。
2. 确认目标板厂、材料、层数、板厚、铜厚、装配方式、板框、安装孔和机械边界。
3. 核对关键封装、Pin/Pad mapping、极性、Pin 1、机械模型和器件 Layout 要求。
4. 根据项目需求形成规则基线，区分板厂制造能力、项目设计默认值和制造极限。
5. 选择必要的 Net Class 或明确 Scope，记录规则值、依据、单位、Scope、Altium Rule Priority 和覆盖关系。
6. 由用户确认 Altium 实际规则已配置，并人工核对关键 Scope 与 Altium Rule Priority。
7. 使用 Preflight Checklist 记录阻断项与结论。

Rule organization principle：使用能够准确表达工程意图的最简单 Scope，并保持最小且可维护的规则集。

- 多个对象共享相同 electrical、routing 或 manufacturing behavior，且形成稳定、有工程意义的类别时，优先使用对应的 Net Class 或 Object Class scope，避免重复成员 Query。
- 单个特殊 Net、Object、Layer 或例外情况，使用最简单准确的 Explicit Scope 或 Custom Query；不要仅因工具支持复杂 Query 就增加复杂度。
- 只有存在真实的 electrical、routing、manufacturing、mechanical 或 verification / traceability difference 时，才新增 Altium Rule Priority 更高的 exception rule；不要创建行为完全相同的重复 Rule。

当当前任务意图主要是 PCB rule preparation、EDA rule preparation、Altium rule configuration 或 Layout Preflight rule baseline 时，Mode A 默认采用 configuration-first 输出：先给出已知的 manufacturer / stackup baseline，再给出当前证据可支持、可直接配置的规则表示，随后补充简短工程依据、例外和真正未决项；若制造与 stackup baseline 已明确，不机械重复完整背景说明。不要先长篇解释全部 rule category，也不要因为 EDA tool 或 checklist 中存在某类 rule 就逐项展开。

规则表示优先使用紧凑表格或等价结构，使用户不需要从散文中重新拼装配置。字段可按规则类型调整，通常应让 `Rule`、`Scope`、`Value / Range / Setting`、`Unit`、`Priority / Note` 清楚可见；使用 Net Class、Differential Pair Class 或 Object Class 时，列出当前可靠 evidence 已确认的实际 members，无法可靠确认的成员标记为 `待 Project / netlist / EDA evidence 核对`，不得猜测。存在重叠规则时，应明确 default rule、exception rule 及其覆盖 / priority 关系；不要求所有规则使用数字 Priority，也不要求所有规则都建立 Class。

第一轮 rule baseline 只展开当前项目真正适用的 electrical、routing、placement、plane-copper、mechanical 或 manufacturing constraints。普通项目中 Clearance、Width、Routing Via Style、Component Clearance，以及使用 polygon / copper pour 时的 Polygon Connect Style 等可能常见；Differential Pair、Impedance、Length / Matched Length、creepage / isolation、Board Outline / mechanical clearance、hole / drilling、mask / paste / silkscreen 或其他特殊制造约束只在项目需求、资料或制造基线实际触发时展开。这些只是 examples，不是固定分类或强制清单。

Rule Preparation 默认回答 `what to configure`，不主动输出 Altium click-by-click UI tutorial；只有用户明确询问设置位置、提供 AD 截图要求操作指导，或配置问题需要 Interactive EDA Guidance 时，才说明具体 UI 操作。单纯 Rule Preparation 也不自动扩展到 placement、routing sequence、GND stitching、polygon geometry、copper shape 或铺铜实现建议，除非规则定义本身依赖这些内容，或用户明确询问。

Layout Preflight 不要求初始 DRC。用户可以使用 Altium 在线规则检查或临时检查，但不得把 DRC 结果作为批准开始正式布局的默认仓库门禁。

## 6. 模式 B 方法

### B1 — Interactive Placement Guidance

适用于用户询问当前先摆什么、模块内部如何摆、哪些器件必须靠近、哪些可以稍远、下一步移动什么、哪些先不要动，或要求一步一步完成布局。它是基于用户提供的当前事实、截图和器件/资料的工程指导，不替代 `.PcbDoc`、不证明 EDA 实现，也不要求每轮形成正式审查结论。

按以下顺序推进，除非当前证据表明应先解决明确冲突：

```text
已确认的机械锚点
        ↓
外部连接器 / 用户可操作器件
        ↓
宏观功能区
        ↓
关键模块锚定器件
        ↓
暂定宏观布局冻结
        ↓
一次处理一个关键模块
        ↓
布局敏感的局部 cluster
        ↓
普通支持器件
        ↓
测试点 / 指示器 / 丝印
        ↓
可开始布线
```

“暂定宏观布局冻结”不是永久锁定；仅当出现机械冲突、关键环路冲突、热冲突或布线不可能等合理原因时，重新打开宏观布局。

指导具体模块时，优先明确：

1. Anchor device、must-stay-close cluster，以及每个关键 capacitor / resistor / support component 对应的 pin 或功能。
2. 必须最短的 current loop / sensitive path、noisy side 与 quiet side。
3. 可稍远的器件、暂时不要摆的 ordinary support components，以及所需的相对 placement envelope / routing space。
4. 当前 `Keep fixed`、`Move now`、`Move next`、`Do not move yet`。

Placement envelope 只根据 footprint、机械间隙、布线空间、热要求与装配/探测可达性做相对或粗略判断；不得虚构具体毫米尺寸。布局敏感支持器件应早摆，普通非敏感支持器件可后摆。常见前者包括去耦电容、反馈电阻、补偿 RC、bootstrap 电容、电流采样电阻、栅极电阻、晶振负载电容、端接和 ESD / protection 器件。

电气/机械关系优先于视觉对齐/对称，后者又优先于飞线外观。飞线可作为辅助信息，但不得为缩短或整齐飞线而破坏去耦、反馈、关键电流环路、保护位置、晶振 cluster 或高阻模拟 cluster。

每次协作优先只完成一个有意义的 Placement 变更：用户提供当前截图 → 审查当前 cluster → 已接受器件暂定冻结 → 进入下一 cluster。不要要求用户先一次摆完几十个器件。

相对位置难以文字表达时，可使用 top-view ASCII PCB sketch 或模块内部 Placement sketch；它们仅为 conceptual、not to scale、not EDA evidence，只表达相对位置、方向和功能关系，不能证明实际间隙、线宽、网络连通、DRC 或机械尺寸。

通用 Placement archetype（具体 pinout 与资料要求仍以当前项目事实为准）：

| 区域 | 优先关系 |
|---|---|
| Switching regulator | 将 Power IC、input capacitor、switching / energy-storage components 与 output capacitor 按当前 topology / datasheet 组织成紧凑 critical loop；控制 hot-loop、switch-node area、pin-specific 去耦与 quiet feedback path。 |
| Charger / power-path IC | 输入、储能/去耦、功率路径与电池/负载端按功能流向紧凑；保留热与大电流布线空间。 |
| Load switch / eFuse | 保护/控制器靠近受保护电源路径；输入/输出去耦和电流路径短、直接。 |
| Protected external interface | 连接器入口先经过 ESD / protection；保护回路短，并与内部敏感区域分开。 |
| Analog / high-impedance region | 输入与反馈/偏置 cluster 紧凑、远离 noisy side；保留安静参考与回流空间。 |
| Clock / crystal region | 晶体与 load capacitors 靠近相关器件引脚；远离开关节点、大电流和噪声路径。 |

### B2 — Interactive Routing Guidance

适用于逐步决定下一根线、当前模块 routing 顺序、冲突让路、short crossover、routing corridor、GND 时机或是否局部重开 Placement。它提供工程施工指导，不要求每轮形成 Formal Findings table、Stage Gate 或 PCB Release 结论。

#### Evidence before specificity

具体 net / pin-to-pin routing 指令必须遵守 `docs/AI_Context_Guide.md` 的 context / evidence boundary，并有足够可靠的 connectivity evidence。只有 PCB 视觉证据时，指导限于视觉或几何 routing review，明确不推断 connectivity 或 net function；不得根据 PCB screenshot 与丝印猜测 pad net、pin function 或 feedback、enable、threshold、sensing 等分类。

#### Routing Criticality 与 Dominant Constraint

只对真正需要特殊保护的 route 使用以下轻量分级。已有足够 Project evidence 可判断当前 route 的 connectivity、function 与 applicable constraints 时，未被识别为 Critical 或 Constrained 的 routing 才默认按 **Ordinary** 处理；evidence-unknown / function-unknown routing 不得仅因未分类而视为 Ordinary。开始 Stage 6 前仍不要求建立全网完整分级表。

- **Critical**：存在 topology、datasheet、safety、power integrity、signal integrity、noise 或 measurement 等明确关键约束，明显恶化 routing geometry 会产生实际工程风险。
- **Constrained**：存在明确 routing preference / constraint，但通常可在不违反自身 mandatory constraint 的情况下向 Critical routing 让路。
- **Ordinary**：没有特殊 routing geometry requirement。

Routing Criticality 是 engineering routing decision，与用于 Width、Clearance、Polygon 等规则覆盖关系的 **Altium Rule Priority** 不同，不得混用。

对 Critical 及必要的 Constrained route，同时说明其 **Dominant Constraint**，即该 route 为何重要，例如 critical loop area、current capacity / voltage drop、quiet sensing / reference、high impedance / noise coupling、continuous return/reference、matched geometry 或 datasheet-defined path。这是工程描述，不建立额外编码 taxonomy。只有长期有价值时，才在 Project `docs/pcb_design_rules.md` 记录具体 Critical / Constrained route 与 dominant constraint；Ordinary nets 不需要持久化完整表格。

Topology- 或 datasheet-defined routing constraints 在适用时覆盖 generic routing order，例如 switching hot loop、Kelvin sensing、high-speed differential、RF、crystal 与 precision reference；不得把这些示例固化为 universal Criticality ranking。

#### Reserve globally, route locally

采用 `Reserve critical constraints globally; execute routing locally.`：开始或继续 routing 前，先识别全板的重要 critical corridors、跨模块关键 route、关键 loop / return geometry、reference-plane needs，以及 Ordinary nets 不应占用的空间；实际人工施工仍以 module、local functional block 或 local cluster 为单位。

典型局部顺序为 current local Critical → current local Constrained → nearby Ordinary。Global reservation 不要求先完成全板每一条 Critical route 才能进行局部 routing；相邻 Ordinary route 只要不占用尚未解决的 critical routing space，也不破坏关键 return/reference geometry，就可以在当前 local block 一起完成。

#### Conflict resolution

Routing conflict 按以下顺序处理：

1. **Mandatory constraint**：不得为 routing convenience 牺牲 safety、required clearance、manufacturing requirement、mandatory datasheet / topology constraint 或其他 hard project requirement。
2. **Routing Criticality**：较低关键度 routing 让路，但不能因此违反其自身 mandatory constraint。
3. **Dominant electrical / return-reference constraint**：同一 Routing Criticality 时，优先保持 dominant electrical constraint 与 return / reference continuity。
4. **Optimization tie-break**：多个方案都满足上述要求后，再权衡 unwanted coupling、reference-plane disruption、via count、route length 与 routing simplicity；视觉整齐最后考虑。

Via count 与 route length 没有固定先后；若其中一项本身就是某 route 的 dominant constraint，则按前一层工程约束处理。不得为了让较低关键度网络少一两个 via 而明显恶化更关键的 route。

#### Layer、reference 与 return planning

遵循 Project layer / copper strategy，不预设 Bottom = GND 或固定的 Top routing / Bottom ground plane。当某层主要用于保持连续 reference plane 时，应控制该层 signal routing，避免实质割裂预期 return/reference path。需要且电气合理时允许 short crossover；保持其合理短小、避免长 slot / barrier、保护较高关键度 return path，并在可行时回到 primary routing layer。复杂高速、RF、HDI 等继续使用专项方法。

Return planning is early; GND implementation is flexible。若 local GND via、critical reference connection 或 critical current return 本身属于 critical loop / reference geometry，应与该 critical route 同步实现，不机械推迟到统一 GND pass。其他普通 component GND vias、stitching vias、bulk ground completion 与 polygon completion 可在 dedicated GND pass 完成，但所需 return geometry、via landing 与 reference continuity 必须提前规划并保留。

#### Placement reopen

遵守 B1 的“暂定宏观布局冻结”（provisional placement freeze）。只有 routing-critical constraint 无法合理满足，或小范围移动能显著降低 electrical、thermal 或 mechanical risk 时，才局部 reopen placement；不要为了一个 Ordinary via、视觉整齐或略短的 Ordinary route 频繁重开 Placement。

### B3 — Layout / Routing Review

1. 先确认审查对象、PCB / Git 版本、视图类型和证据限制。
2. 从板框、安装孔、连接器、机械边界和功能分区开始检查布局。
3. 结合项目需求检查关键电源、模拟、晶振、高速、MOSFET、保护、热和测试可达性。
4. 检查关键电流环路、敏感路径、回流连续性、换层、过孔、细颈和铺铜策略。
5. 用户在相关修改后执行 Repour，并提供需要复审的当前证据。
6. 将需要跨回合追踪的重要问题写入 `docs/pcb_review.md`，普通即时建议不强制沉淀。

本正式 Review 不要求 DRC 作为默认输入，也不要求保存中间 DRC 记录。具体逐项顺序以 PCB Layout Checklist 为准。

## 7. 风险分类

- **高风险**：可能损坏硬件、造成不安全使用、反接/短路、关键连接失效、不可制造，或使关键规则/DRC 证据不可信；阻断当前阶段门。
- **中风险**：可能影响功能、信号/电源完整性、热、装配、可靠性、机械适配或造成高返工成本；制造前解决，或经合理豁免。
- **低风险**：主要影响可读性、丝印、探测便利或维护性；记录并安排处理。

证据不足不自动改变问题的电气严重性，但会限制问题关闭或当前 Formal Review 结论。

## 8. 输出格式

### B1 — Interactive Placement Guidance

```text
Current placement goal

Keep fixed

Move now

Move next

Do not move yet

Critical relationships

Optional ASCII top-view

What screenshot / evidence to provide next
```

该模板不要求完整 Findings table 或 Stage Gate conclusion。

### B2 — Interactive Routing Guidance

```text
Current routing objective

Protect / reserve

Route now

Yield / crossover candidate

Return / layer note

Placement reopen
<No / local reopen + reason>

Next evidence
```

无关字段可以省略；该模板不要求 Formal Findings table、Stage Gate result 或 full-board checklist。

### Formal Review（A、B3）

### 当前结论

给出与模式匹配的结论，并紧接说明证据范围和限制。

### 输入与版本

| 输入 | 版本 / 日期 | 用途 | 追溯风险 |
|---|---|---|---|

### 问题

| ID | 区域 | 问题 | 风险 | 依据 | 所需动作 | 责任人 | 状态 |
|---|---|---|---|---|---|---|---|

建议状态：`待决策`、`待修改`、`待核对`、`待 EDA 核对`、`待用户确认`、`已修改 / 待复核`、`已关闭`、`已豁免`。

### 阶段门与下一步

先列阻断项，再列用户 EDA 动作、需要补充的证据和允许进入的下一阶段。

## 9. 禁止事项

- 不复制其他项目的数值、网络名、封装、尺寸、下单参数、问题或豁免。
- 不把参考项目当作默认规则集。
- 不虚构板厂能力、规则配置、Repour、DRC 结果或验证状态。
- 不为得到零违规而放宽、关闭或删除必要规则。
- 不把视觉整洁等同于电气正确或可制造。
- 不把未制造、未装配、未上电或未测试的状态描述为已完成。
