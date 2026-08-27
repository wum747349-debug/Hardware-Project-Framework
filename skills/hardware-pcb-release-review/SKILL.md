---
name: hardware-pcb-release-review
description: Review an exact PCB release candidate for manufacturing readiness. Use for Stage 7 Final Full Batch DRC analysis, manufacturing-data path and interpretation review, conditional PCBA or special-fabrication checks, findings and waivers, and the Manufacturing Release Decision.
---

# PCB Release Review / Manufacturing Preparation

## 1. Purpose / Boundary

本 Skill 只负责 Stage 7 的 PCB Release Review / Manufacturing Preparation：识别 exact release candidate，判断 evidence readiness，分析用户运行的 Final Full Batch DRC，核对实际 manufacturing-data path 的最终制造解读，处理 findings / waivers，并给出 Manufacturing Release Decision。逐项执行使用 [PCB Release Checklist](../../checklists/pcb_release_checklist.md)；实际结果写入 Project `docs/pcb_review.md`。

本 Skill 不负责 interactive placement、interactive routing、routing criticality / corridor、GND implementation strategy、whole-board return-path review 或普通 Stage 6 routing-quality review。已完成 Stage 5–6 Formal Review 的普通 bare PCB 不在 Stage 7 默认重做 schematic、BOM、placement、routing、return-path 或 whole-board screenshot review。

## 2. Release Candidate and Evidence Readiness

先无歧义记录实际要生产的 PCB / hardware version、`.PcbDoc` 或其他 EDA source identity、Git identity 与当前 review context。只有 exact release candidate 与各项 evidence 的版本关系清楚，才能进入最终放行。

Evidence 的选择、充分性、新鲜度、session / persistent authority 和 durable summary 边界以 [AI Context Guide](../../docs/AI_Context_Guide.md) 为准。本 Skill 只要求对当前具体放行结论充分的 evidence；存在 gap 时请求 minimum missing evidence，不自动索要全部 raw screenshots 或 reports。

## 3. Final Full Batch DRC

DRC verifies the EDA design against applicable design rules. 确认用户对 exact release candidate 运行完整 Batch DRC，规则基线和关键检查类别适用，Warnings / Rule Violations 已分类处置。实际违规必须修正或进入明确、合理、可追溯的 waiver；修改并在适用时 Repour 后，由用户重新运行 Final Full Batch DRC。

AI/Codex 只分析用户提供的结果，不声称自行运行 Altium、Repour 或 DRC。用户摘要可以成为 evidence；只在无法判断具体违规、规则或 waiver 时请求最小局部证据。

## 4. Manufacturing Data Path

识别实际 submission path，而不固定某个板厂、导出格式或目录：

- Path A：Final PCB → user-generated Gerber / Drill package → review exact package → submit exact reviewed package。
- Path B：Final PCB source → manufacturer-side source conversion → review manufacturer interpretation of submitted source。
- Path C：submitted manufacturing data → downstream processed production interpretation → review when necessary。

核心原则是：**Review one capable and faithful representation of the exact manufacturing data used by the actual submission path.** 不要求同时使用 manufacturer viewer、independent viewer 和 drill viewer。只有当 plating semantics、slot interpretation、drill representation 不完整、preview 不能显示所需 feature，或 manufacturer conversion 疑似不一致时，才选择其他合适 representation 弥补 gap。

## 5. Final Manufacturing Interpretation

Manufacturing interpretation verifies that the actual manufacturing-data path faithfully represents the intended manufacturing geometry. DRC 是 EDA / design-rule verification，CAM / Gerber interpretation 是 manufacturing translation verification；两者互补，不重复、不可互换。例如 pad-level Solder Mask override 可能不按用户预期被普通 DRC 暴露，而最终 manufacturing interpretation 可直接显示异常开窗。

按制造意图检查，不依赖 viewer 的具体 layer naming：

1. Copper / layer mapping：层数、正反面、铜层完整性与预期一致。
2. Solder Mask：开窗、遮盖、mask sliver 与特殊 override 符合意图。
3. Drill / Slot / PTH / NPTH：数量、位置、形状、孔类与 plating semantics 正确。
4. Board Outline / Cutout / routed geometry：外形、内挖、槽和铣切几何完整无歧义。
5. Composite / Registration：作为 cross-layer sanity check，确认铜、阻焊、钻孔与外形的对位关系；不将其定义为独立 manufacturing primitive。

对 plated slot 等 feature，问题是最终制造数据是否包含正确数量、位置、形状和 plating semantics，而不是它是否与 round drill 显示在同一 viewer layer。

## 6. Basic Fabrication / Critical Marking

确认适用的基本制造与下单参数，例如板材、层数、成品板厚、铜厚、表面处理、阻焊与数量/拼板要求，并确认它们与 release candidate 和制造路径一致。

Silkscreen 作为 Critical Marking 按真实工程影响检查：Pin 1、极性、power / GND、connector identity、critical user-facing label 与 safety-related marking。普通 component reference outline clipping 不自动阻断制造。

## 7. PCBA — Conditional

只在项目实际需要 PCB Assembly 时，才加载并核对 BOM、Pick & Place、Paste Mask、Assembly Drawing、DNP / Variant 以及 population / orientation。Bare-board fabrication 不默认承担这些输入。

## 8. Special Fabrication — Conditional

只在实际使用 controlled impedance、special stackup、blind / buried vias、HDI、castellated holes、edge plating、rigid-flex、special copper process、special solder-mask process 或其他 non-standard fabrication feature 时，才加载对应资料与专项方法。普通 2-layer / 4-layer rigid PCB、standard PTH / NPTH、ordinary plated slots、no controlled impedance 且 no HDI 的项目不默认执行这些流程。

## 9. Findings / Waivers

将 release finding 区分为真实设计/制造数据问题、规则配置问题、evidence gap 或可能的 waiver。问题修正后刷新受影响输出、重跑 Final Full Batch DRC，并复审受影响的 manufacturing interpretation。

每项 waiver 只能覆盖明确对象，必须有技术理由、风险评估、验证方式与用户批准，不得用于隐藏设计错误。Major waiver 按 AI Context Guide 在 `docs/pcb_review.md` 留下 durable summary。

## 10. Delta-triggered Upstream Re-review

Stage 7 design delta 按影响范围处理，不建立新 Gate，也不自动重跑整个 Stage 6。例如只修改 Solder Mask Rule Expansion：修改 PCB → 刷新适用输出 → 重跑 Final Full Batch DRC → 复审受影响的 Solder Mask manufacturing interpretation。

如果 delta 实际影响 routing、via topology、copper、component placement 或 critical return/reference geometry，按需加载 `hardware-pcb-layout-review`，对受影响 delta 执行 scoped B3 review；其他未变区域不机械复审。

## 11. Manufacturing Release Decision

按以下正常 bare-PCB baseline 完成收口：

```text
Identify exact release candidate
        ↓
Final Full Batch DRC
        ↓
Identify actual manufacturing-data / submission path
        ↓
Review one faithful final manufacturing interpretation
        ↓
Confirm applicable fabrication / order parameters
        ↓
Explicit Manufacturing Release Decision
```

结论使用 `批准制造` / `有条件批准` / `不批准制造`。`有条件批准` 必须明确条件、风险、责任与是否涉及正式 waiver。正式 closeout 在 `docs/pcb_review.md` 留下最小 durable summary。

## 12. Capability / Evidence Prohibitions

- 不声称自行读取 `.PcbDoc` 内部对象、运行 Altium / Repour / DRC、生成制造数据或完成下单。
- 不虚构 DRC、CAM / Gerber、钻孔、装配、板厂能力、制造参数、waiver 批准或放行状态。
- 不把 DRC 与 manufacturing interpretation 当作相互替代的证据。
- 不把文件存在、普通 PCB screenshot、单一 `0 violations` 文字或清单完成率当作自动制造放行。
- 不把未制造、未装配、未上电或未测试的状态描述为已完成。
