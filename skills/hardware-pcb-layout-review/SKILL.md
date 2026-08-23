---
name: hardware-pcb-layout-review
description: Guide interactive PCB placement and review placement, layout, routing, copper, user-provided DRC evidence, and PCB release. Use for Layout Preflight, Layout / Routing Review, PCB Release Review, Altium rule Scope/Priority review, rule exemptions, or manufacturing-output checks.
---

# PCB Layout 与制造放行审查

## 1. 目的与边界

本 Skill 用于低压嵌入式、MCU 控制、传感器采集、电源管理、模拟前端和通信接口板，提供三种 PCB 协作模式；其中 Mode B 包含交互式 Placement 指导与正式 Layout / Routing Review：

1. **Layout Preflight**：确认正式布局前的制造、机械、封装、原理图门禁和规则基线。
2. **Layout / Routing Review**：审查布局、关键路径、布线、回流、过孔和铺铜。
3. **PCB Release Review**：审查完整 Batch DRC 结果、装配信息、制造输出、规则豁免和制造放行。

高压、射频、复杂高速数字、隔离电源、汽车、医疗、安规、HDI 或刚挠结合项目只能复用本 Skill 的通用部分，必须增加专项方法、checklist、标准和有资质的审查。

本 Skill 只维护方法、判断逻辑、风险分类、输出结论和能力边界。逐项检查使用：

- [PCB Layout Preflight Checklist](../../checklists/pcb_layout_preflight_checklist.md)
- [PCB Layout Checklist](../../checklists/pcb_layout_checklist.md)
- [PCB Release Checklist](../../checklists/pcb_release_checklist.md)

项目规则值写入 `docs/pcb_design_rules.md`；实际问题、关闭状态、Batch DRC 摘要、豁免引用和制造结论写入 `docs/pcb_review.md`。

## 2. 选择模式

| 用户请求                                                        | 模式                                      | 必需结论                                              |
| ----------------------------------------------------------- | --------------------------------------- | ------------------------------------------------- |
| 是否可开始布局、规则准备                                                | Layout Preflight                        | `批准开始正式布局` / `不批准开始正式布局`                          |
| “现在先摆什么？”、“哪些器件必须靠近？”、“下一步移动哪些器件？”或逐步完成布局                   | **B1 — Interactive Placement Guidance** | 工程指导；不要求每轮给出正式阶段门结论                               |
| 已有 Placement / Routing Evidence 的布局、布线、铺铜、回流或 PCB 图片正式/明确审查 | **B2 — Layout / Routing Review**        | `可进入 PCB Release Review` / `修改后复审` / `存在高风险，停止推进` |
| Batch DRC、Gerber、钻孔、坐标、制造包或放行                               | PCB Release Review                      | `批准制造` / `有条件批准` / `不批准制造`                        |

跨正式审查模式的请求按 A → B2 → C 顺序处理并分别给出阶段门结论，后续证据不能抵消前一阶段的阻断项。B1 可在 Mode B 内的任意合理 Placement 增量中使用，不应被强制包装为 Formal Review。

## 3. 最小上下文

默认、按需和禁止读取范围以 `docs/AI_Context_Guide.md` 的 Stage / Task context table 为准；本 Skill 不重复维护文件清单。

执行时仍按第 2 节选择 Layout Preflight、B1、B2 或 PCB Release Review，并按下文对应方法、证据边界和 checklist 完成工作。

## 4. 能力与证据边界

- `.PcbDoc` 是 PCB 权威实现源文件。没有可靠解析器、脚本或自动化接口时，不声称读取其内部对象、网络、规则、层、铺铜、尺寸或属性。
- PCB 图片只支持视觉判断，不能证明网络、精确间距、线宽、孔径、环宽、规则命中、铺铜状态、未布线数量或 DRC 通过。
- 不声称运行 Altium Designer、配置规则、布线、Repour、Batch DRC 或导出制造文件。
- 实际规则配置、Scope/Priority 核对、布局布线、Repour、DRC 和导出均由用户执行。
- 无法由当前证据确认的实现项标记为 `待 EDA 核对`。
- 始终区分“文档已定义”“用户确认 AD 已配置”“用户提供 DRC 结果”三种状态。

## 5. 模式 A 方法：Layout Preflight

1. 确认项目、硬件版本、原理图审查结论和未关闭高风险问题。
2. 确认目标板厂、材料、层数、板厚、铜厚、装配方式、板框、安装孔和机械边界。
3. 核对关键封装、Pin/Pad mapping、极性、Pin 1、机械模型和器件 Layout 要求。
4. 根据项目需求形成规则基线，区分板厂制造能力、项目设计默认值和制造极限。
5. 选择必要的 Net Class 或明确 Scope，记录规则值、依据、单位、Scope、Priority 和覆盖关系。
6. 由用户确认 Altium 实际规则已配置，并人工核对关键 Scope 与 Priority。
7. 使用 Preflight Checklist 记录阻断项与结论。

Rule organization principle：使用能够准确表达工程意图的最简单 Scope，并保持最小且可维护的规则集。

- 多个对象共享相同 electrical、routing 或 manufacturing behavior，且形成稳定、有工程意义的类别时，优先使用对应的 Net Class 或 Object Class scope，避免重复成员 Query。
- 单个特殊 Net、Object、Layer 或例外情况，使用最简单准确的 Explicit Scope 或 Custom Query；不要仅因工具支持复杂 Query 就增加复杂度。
- 只有存在真实的 electrical、manufacturing、mechanical 或 verification / traceability difference 时，才新增 higher-priority exception rule；不要创建行为完全相同的重复 Rule。

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

### B2 — Layout / Routing Review

1. 先确认审查对象、PCB / Git 版本、视图类型和证据限制。
2. 从板框、安装孔、连接器、机械边界和功能分区开始检查布局。
3. 结合项目需求检查关键电源、模拟、晶振、高速、MOSFET、保护、热和测试可达性。
4. 检查关键电流环路、敏感路径、回流连续性、换层、过孔、细颈和铺铜策略。
5. 用户在相关修改后执行 Repour，并提供需要复审的当前证据。
6. 将需要跨回合追踪的重要问题写入 `docs/pcb_review.md`，普通即时建议不强制沉淀。

本正式 Review 不要求 DRC 作为默认输入，也不要求保存中间 DRC 记录。具体逐项顺序以 PCB Layout Checklist 为准。

## 7. 模式 C 方法：PCB Release Review

1. 确认 PCB、BOM、Batch DRC 摘要和制造输出对应同一版本。
2. 按 Release Checklist 审查规则、实现、机械、装配、BOM 和制造输出。
3. 分析用户提供的完整 Batch DRC 结果与规则豁免。
4. 对修改项要求用户实际修改、Repour，并重新运行完整 Batch DRC。
5. 确认所有实际违规已解决或形成明确、合理、可追溯的豁免。
6. 由用户确认最终 Batch DRC、制造输出和下单参数。
7. 在 `docs/pcb_review.md` 给出显式制造结论。

文件存在不等于输出正确或已放行。制造输出的逐项核对由 Release Checklist 承担，本 Skill 不重复展开。

## 8. Batch DRC 分析

正式 Batch DRC 只在 PCB Release Review 中要求：

1. 确认用户运行的是当前 PCB 版本的完整 Batch DRC。
2. 确认对应 Git / PCB 版本和 `docs/pcb_design_rules.md` 规则基线。
3. 记录运行日期、Warnings 和 Rule Violations 数量。
4. 记录主要检查类别与关键违规文本；仅有 `0 violations` 但无法确认规则基线或关键类别时，给出受限结论。
5. 判断问题属于真实设计问题、规则定义/Scope/Priority 问题，还是合理豁免。
6. 用户修改后重新运行完整 Batch DRC。
7. 记录用户对最终结果的明确确认。

结果默认可直接来自用户对话，不要求专门 DRC 文件、导出报告或完整截图。只有具体问题无法判断时，才请求局部截图或报告片段。缺少报告文件不构成自动阻断，但制造放行必须有用户明确确认完整 Batch DRC 已运行。

## 9. 规则与豁免

`docs/pcb_design_rules.md` 负责规则值、Scope、Priority、AD 配置/人工核对状态和豁免定义，不长期维护“DRC 已验证”列。

每项豁免必须：

- 只覆盖明确对象；
- 有技术理由，不能用于隐藏设计错误；
- 评估电气、机械、制造和装配风险；
- 说明验证方式并由用户批准；
- 在规则文档中定义，并由 `docs/pcb_review.md` 引用。

项目选择不声明某项规则，不自动构成规则豁免。

## 10. 风险分类

- **高风险**：可能损坏硬件、造成不安全使用、反接/短路、关键连接失效、不可制造，或使关键规则/DRC 证据不可信；阻断当前阶段门。
- **中风险**：可能影响功能、信号/电源完整性、热、装配、可靠性、机械适配或造成高返工成本；制造前解决，或经合理豁免。
- **低风险**：主要影响可读性、丝印、探测便利或维护性；记录并安排处理。

证据不足不自动改变问题的电气严重性，但会限制问题关闭或制造放行结论。

## 11. 输出格式

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

### Formal Review（A、B2、C）

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

先列阻断项，再列用户 EDA 动作、需要补充的证据和允许进入的下一阶段。Release Review 另记录 Batch DRC 摘要、豁免引用和制造结论。

## 12. 禁止事项

- 不复制其他项目的数值、网络名、封装、尺寸、下单参数、问题或豁免。
- 不把参考项目当作默认规则集。
- 不虚构板厂能力、规则配置、DRC 结果、制造输出或验证状态。
- 不为得到零违规而放宽、关闭或删除必要规则。
- 不把视觉整洁等同于电气正确或可制造。
- 不在缺少用户完整 Batch DRC 确认时批准制造。
- 不把未制造、未装配、未上电或未测试的状态描述为已完成。
