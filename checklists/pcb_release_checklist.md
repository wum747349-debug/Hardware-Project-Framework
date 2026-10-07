# PCB Release Checklist

> 文档状态：当前有效
> 适用阶段：阶段 7：PCB 审查阶段
> 适用对象：待 PCB Release Review / Manufacturing Preparation 的项目和硬件版本
> 最后核对依据：exact release candidate、用户 Final Full Batch DRC 结果、实际 manufacturing-data path 与最终制造解读

## 使用说明

- 将适用检查及结果记录到当前 Project `docs/pcb_review.md`。
- `状态` 使用：`待核对`、`已确认`、`不通过`、`不适用`、`已豁免`；`不适用` 和 `已豁免` 必须说明依据、风险和批准记录。
- 方法、evidence readiness、waiver、增量复审与输出格式见 [PCB Release Skill](../skills/hardware-pcb-release-review/SKILL.md)；项目专属范围与持久化按 [AI Context Guide](../docs/AI_Context_Guide.md) 执行。
- 清单完成率不能自动推导制造放行，必须填写显式 Manufacturing Release Decision。

## 1. Release Identity / Evidence

| 检查项 | 结论 | 依据 / 证据 | 状态 |
| --- | --- | --- | --- |
| 项目、hardware revision 与待生产 PCB 已无歧义识别 |  |  |  |
| `.PcbDoc` / EDA source、Git identity 与 release candidate 关系已记录 |  |  |  |
| 当前 evidence 对本轮具体结论足够且与 release candidate 版本兼容 |  |  |  |
| session implementation 与 persistent repository source 的同步/漂移状态已说明 |  |  |  |
| 只存在已明确记录的 minimum evidence gaps |  |  |  |

## 2. Final Full Batch DRC

| 检查项 | 结论 | 依据 / 证据 | 状态 |
| --- | --- | --- | --- |
| Final Full Batch DRC 针对 exact release candidate |  |  |  |
| 用户确认完整 Batch DRC 已运行，日期 / context 与规则基线可追溯 |  |  |  |
| 适用规则与关键类别已启用，结果足以支持判断 |  |  |  |
| Warnings / Rule Violations 已分类处置 |  |  |  |
| 实际违规已解决或进入明确、合理、可追溯的 waiver |  |  |  |
| 适用修改与 Repour 后已重跑 Final Full Batch DRC |  |  |  |

## 3. Manufacturing Data Path

| 检查项 | 结论 | 依据 / 证据 | 状态 |
| --- | --- | --- | --- |
| 实际 manufacturing-data / submission path 已识别 |  |  |  |
| 被审查表示与实际提交/生产使用的最终制造数据对应 |  |  |  |
| 当前 representation 有能力显示本项目需核对的 feature |  |  |  |
| 若发现 interpretation / conversion gap，已用其他适当 representation 弥补 |  |  |  |

## 4. Core Manufacturing Interpretation

| 检查项 | 结论 | 依据 / 证据 | 状态 |
| --- | --- | --- | --- |
| Copper / layer mapping：层数、正反面、铜层几何与制造意图一致 |  |  |  |
| Solder Mask：开窗、遮盖、sliver 与 pad-level override 符合意图 |  |  |  |
| Drill / Slot / PTH / NPTH：数量、位置、形状、孔类与 plating semantics 正确 |  |  |  |
| Board Outline / Cutout / routed geometry：外形、内挖、槽与铣切几何完整无歧义 |  |  |  |
| Composite / Registration：铜、阻焊、钻孔与外形的 cross-layer 对位合理 |  |  |  |

## 5. Basic Fabrication Parameters / Critical Marking

| 检查项 | 结论 | 依据 / 证据 | 状态 |
| --- | --- | --- | --- |
| 适用的板材、层数、成品板厚、铜厚与表面处理已确认 |  |  |  |
| 阻焊、数量、单片/拼板、外形与其他适用下单参数已确认 |  |  |  |
| Pin 1、极性、power / GND、connector identity 和 critical user-facing / safety marking 正确 |  |  |  |
| 普通位号或 outline clipping 若存在，已按实际工程影响处置 |  |  |  |

## 6. PCBA — Conditional

> 只有项目实际需要 PCB Assembly 时执行；否则记录 `不适用`及理由。

| 检查项 | 结论 | 依据 / 证据 | 状态 |
| --- | --- | --- | --- |
| BOM 与 release candidate 的位号、数量、型号 / 参数和 footprint 一致 |  |  |  |
| Pick & Place 的单位、原点、正反面、旋转和位号正确 |  |  |  |
| Paste Mask 和特殊钢网要求正确 |  |  |  |
| Assembly Drawing 包含所需外形、位号、极性、Pin 1 和装配面信息 |  |  |  |
| DNP / Variant、population 与 orientation 已核对 |  |  |  |

## 7. Special Fabrication — Conditional

> 只有实际存在 non-standard fabrication feature 时执行；普通 rigid PCB、standard PTH / NPTH 和 ordinary plated slots 不因此自动进入专项流程。

| 检查项 | 结论 | 依据 / 证据 | 状态 |
| --- | --- | --- | --- |
| controlled impedance / special stackup 的设计、制造数据与下单声明一致或不适用 |  |  |  |
| blind / buried vias、HDI、castellated holes、edge plating 或 rigid-flex 已使用适用方法核对或不适用 |  |  |  |
| special copper / solder-mask process 或其他 non-standard feature 的制造语义与能力已确认或不适用 |  |  |  |

## 8. Findings / Waivers

- [ ] Findings / waivers 的对象、影响与风险、技术依据、动作 / 验证、批准与状态可追溯。
- [ ] 修改后已刷新适用输出、重跑 Final Full Batch DRC 并复审受影响的 manufacturing interpretation。
- [ ] 影响 placement、routing、via topology、copper 或 critical return/reference geometry 的 delta 已完成 scoped B3 upstream re-review；其他范围未机械重审。

## 9. Manufacturing Release Decision

- [ ] Exact release candidate 已无歧义识别。
- [ ] 用户已运行并确认该版本的 Final Full Batch DRC。
- [ ] 所有实际违规已解决，或具有明确、合理、可追溯的已批准 waiver。
- [ ] 实际 submission path 与一个 capable and faithful final manufacturing interpretation 已确认。
- [ ] 适用的 bare-PCB、conditional PCBA 与 conditional special-fabrication 项已确认。
- [ ] `docs/pcb_review.md` 已按 AI Context Guide 留下最小 durable summary。
- [ ] 已按 Skill 显式填写 Manufacturing Release Decision：`批准制造` / `有条件批准` / `不批准制造`。
- [ ] 阻断问题、未关闭非阻断问题、已批准 waivers 与下一步明确；有条件批准已说明条件、风险和责任。
