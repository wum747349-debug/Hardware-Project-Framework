# PCB 设计规则

> 文档状态：当前有效，规则基线已确认，尚未在 Altium Designer 中配置和验证
>
> 当前阶段：整板原理图系统审查 / PCB Layout 前准备
>
> 适用对象：STM32 DAQ Control Board Rev A
>
> 默认目标板厂：嘉立创 / JLCPCB
>
> 官方工艺核对日期：2026-07-28

## 事实边界

- 本文档是用户人工配置 Altium Designer 规则的依据。
- 工程可能使用 Constraint Manager 或 PCB Rules and Constraints Editor；本文规定规则逻辑、Scope 和参数，不强制具体菜单路径。
- 本文档中的规则值尚未写入或核实到实际 `.PcbDoc`。
- AI/Codex 未运行 Altium Designer、未配置规则、未运行 Batch DRC。
- 最终制造能力、价格和订单选项必须在下单时再次核对。
- 本项目为两层低压、低速、小电流开发板，不使用制造极限。
- 本文档不代表 PCB Review、SMT 可制造性审核或 DRC 已完成，当前尚不可直接投产。

### 单位约定

- mm 是所有规则的权威值。
- mil 仅作为近似辅助显示，统一保留一位小数；`0 mil` 是 `0.00 mm` 的辅助显示。
- 不得用四舍五入后的 mil 反向替代原始 mm。
- 板框总体尺寸 `70 mm × 50 mm` 继续只使用 mm，避免无意义的大 mil 数值。

## 1. 制造基线

| 制造项目 | 当前基线 | 简短解释 |
| --- | --- | --- |
| 板材 | `FR-4` | 常见玻纤环氧树脂刚性板材料。 |
| 层数 | 2 层（`2 layers`） | 只有顶层和底层两层铜。 |
| 成品板厚 | `1.60 mm (≈63.0 mil)` 标称值（`nominal`） | 该数值是标称成品板厚，实际有板厂公差。 |
| 外层铜厚 | 1 oz 外层铜（`1 oz outer copper`） | 常用外层铜厚规格，不是 `1 mm (≈39.4 mil)`。 |
| 过孔类型 | 仅通孔过孔（`Through vias only`） | 只使用贯穿顶层和底层的通孔过孔。 |
| 盲埋孔 | 不使用盲孔、埋孔（`No blind/buried vias`） | 不使用只连接部分铜层的盲孔或埋孔。 |
| 阻抗声明 | 不声明受控阻抗（`No controlled-impedance claim`） | 不声明受控阻抗，不声称已实现 `90 Ω`。 |
| 组装目标 | 嘉立创贴片/组装（`JLCPCB SMT/PCBA`） | 目标由嘉立创进行贴片或组装，但尚未完成可制造性审核。 |

制造能力、板厚与铜厚公差、装配类型、费用和订单选项必须在下单前复核。当前 PCB 尚未完成 SMT 可制造性审核，上述基线不代表已经具备可制造或可投产条件。

## 2. 规则优先级原则

- 具体网络 Width 规则优先于 `All` 默认 Width 规则。
- 默认规则放在最低优先级。
- 不建立没有明确需求的复杂 Net Class、阻抗或高速规则。
- Scope 可直接使用明确网络查询，不要求额外导出 Net Class 报告。
- 下文 Routing Width 规则按列出顺序从高到低配置；若 Altium Designer 中存在其他重叠规则，用户应人工核对最终优先级和适用对象。

## 3. 电气间距（Electrical Clearance）

```text
Rule Name: Clearance_Default
Scope 1: All
Scope 2: All
Minimum Clearance: 0.20 mm (≈7.9 mil)
```

## 4. 走线宽度（Routing Width）

`Preferred` 是交互布线时优先采用的宽度；`Min` 和 `Max` 定义允许范围，也是 DRC 检查边界。

规则优先级从高到低为：

1. `Width_Load_500mA`
2. `Width_Power_5V`
3. `Width_Power_3V3`
4. `Width_GND`
5. `Width_Default_Signal`

### 4.1 `Width_Load_500mA`

```text
Scope:
InNet('VLOAD_EXT1') Or
InNet('VLOAD_EXT2') Or
InNet('MOS_OUT1') Or
InNet('MOS_OUT2')

Min: 0.50 mm (≈19.7 mil)
Preferred: 0.80 mm (≈31.5 mil)
Max: 1.20 mm (≈47.2 mil)
```

### 4.2 `Width_Power_5V`

```text
Scope:
InNet('VBUS_RAW') Or
InNet('VBUS_FUSED') Or
InNet('+5V_SYS')

Min: 0.30 mm (≈11.8 mil)
Preferred: 0.50 mm (≈19.7 mil)
Max: 1.00 mm (≈39.4 mil)
```

### 4.3 `Width_Power_3V3`

```text
Scope:
InNet('3.3V') Or
InNet('VDDA_3V3')

Min: 0.25 mm (≈9.8 mil)
Preferred: 0.40 mm (≈15.7 mil)
Max: 0.80 mm (≈31.5 mil)
```

### 4.4 `Width_GND`

```text
Scope: InNet('GND')
Min: 0.30 mm (≈11.8 mil)
Preferred: 0.50 mm (≈19.7 mil)
Max: 1.50 mm (≈59.1 mil)
```

GND 主要使用顶层和底层 Polygon；本 Width 规则只控制独立走线。

### 4.5 `Width_Default_Signal`

```text
Scope: All
Min: 0.15 mm (≈5.9 mil)
Preferred: 0.20 mm (≈7.9 mil)
Max: 0.50 mm (≈19.7 mil)
Priority: 最低
```

## 5. 布线过孔样式（Routing Via Style）

```text
Rule Name: ViaStyle_Default
Scope: All
Mode: Min/Max Preferred

Via Diameter:
Min: 0.60 mm (≈23.6 mil)
Preferred: 0.60 mm (≈23.6 mil)
Max: 1.00 mm (≈39.4 mil)

Via Hole:
Min: 0.30 mm (≈11.8 mil)
Preferred: 0.30 mm (≈11.8 mil)
Max: 0.50 mm (≈19.7 mil)
```

- 默认过孔为外径 `0.60 mm (≈23.6 mil)`、钻孔 `0.30 mm (≈11.8 mil)`。
- 默认使用 Top-to-Bottom 通孔。
- 禁止盲孔、埋孔和未经确认的 Via-in-Pad。
- 普通过孔默认双面盖油，测试用途过孔除外。

## 6. 孔径与环宽（Hole Size / Minimum Annular Ring）

```text
Rule Name: HoleSize_Via
Scope: IsVia
Measurement Method: Absolute
Min: 0.30 mm (≈11.8 mil)
Max: 0.50 mm (≈19.7 mil)
```

```text
Rule Name: HoleSize_Pad
Scope: IsPadHoleValid
Measurement Method: Absolute
Min: 0.50 mm (≈19.7 mil)
Max: 6.30 mm (≈248.0 mil)
```

```text
Rule Name: HoleToHoleClearance
Scope: All
Minimum: 0.45 mm (≈17.7 mil)
```

```text
Rule Name: MinimumAnnularRing_Via
Scope: IsVia
Minimum: 0.15 mm (≈5.9 mil)
```

```text
Rule Name: MinimumAnnularRing_Pad
Scope: IsPadHoleValid
Minimum: 0.20 mm (≈7.9 mil)
```

SMD Pad 没有钻孔，不应被错误理解为违反 PTH 最小孔径。Routing Via Style 控制交互布线采用的默认过孔；Hole Size 和 Minimum Annular Ring 用于检查板上已有对象，职责不同，因此不合并或删除。

## 7. USB 数据线当前处理

- 根据当前布局决定，`USB_DP` 与 `USB_DM` 暂不建立 Altium Differential Pair。
- 两个网络暂时受 `Width_Default_Signal` 和 `Clearance_Default` 约束。
- 只保留人工布局提醒：路径短、尽量少过孔、下方保持连续 GND、ESD 靠近 USB-C。
- 当前不要求严格并行、长度匹配或实现 `90 Ω`。
- 后续如调整器件方向或走线关系，再单独讨论是否建立差分对规则。

## 8. 阻焊与钢网（Solder Mask / Paste Mask）

```text
Rule Name: SolderMaskExpansion_Default
Scope: All
Expansion: 0.05 mm (≈2.0 mil)
```

```text
Rule Name: PasteMaskExpansion_Default
Scope: All
Expansion: 0.00 mm (0 mil)
```

```text
Rule Name: MinimumSolderMaskSliver_Default
Scope: All
Minimum: 0.10 mm (≈3.9 mil)
```

- `0.10 mm (≈3.9 mil)` 阻焊桥按绿色阻焊基线。
- 如果下单改为黑色或白色阻焊，改为至少 `0.13 mm (≈5.1 mil)`。
- LQFP、USB-C 等细间距焊盘若触发阻焊桥问题，应优先检查具体封装并局部改为 `0.00 mm (0 mil)` Expansion，不得直接降低全局规则。
- Paste Mask 默认跟随焊盘；特殊器件根据器件或钢网要求单独覆盖。

## 9. 丝印（Silkscreen）

```text
Rule Name: SilkToSolderMaskClearance_Default
Scope: All
Checking Mode: Check Clearance To Solder Mask Openings
Minimum Clearance: 0.15 mm (≈5.9 mil)
```

人工检查规范：

- 最小丝印线宽：`0.15 mm (≈5.9 mil)`。
- 最小文字高度：`1.00 mm (≈39.4 mil)`。

最小丝印线宽和文字高度仅作为人工检查规范，不声称已在 Altium Designer 中配置对应 DRC。

## 10. 板边间距（Board Outline Clearance）

```text
Rule Name: BoardOutlineClearance_Default
Scope: All
Minimum Clearance: 0.25 mm (≈9.8 mil)
```

该规则可能同时检查铜、走线、焊盘、过孔等电气对象和 Overlay 丝印对象到铣边板框的间距。全局默认保持 `0.25 mm (≈9.8 mil)`；USB-C、连接器、丝印或其他结构对象如需靠近板边，应进行局部人工核对或设置具体例外，不得把全局规则改为 `0.00 mm (0 mil)`。

## 11. 铺铜连接方式（Polygon Connect Style）

```text
Rule Name: PolygonConnect_GND_Via
Scope: IsVia And InNet('GND')
Connect Style: Direct Connect
Priority: 高
```

```text
Rule Name: PolygonConnect_GND_Pad
Scope: IsPad And InNet('GND')
Connect Style: Relief Connect
Conductors: 4
Air Gap: 0.20 mm (≈7.9 mil)
Conductor Width: 0.25 mm (≈9.8 mil)
Priority: 低于 PolygonConnect_GND_Via
```

MOSFET、电源或负载焊盘如需 Direct Connect，按具体焊盘单独处理；当前不建立尚不需要的复杂规则。

## 12. 布局指导但不强制建立 DRC 的内容

- 晶振靠近 MCU，走线短且对称，尽量无过孔。
- USB ESD 靠近 USB-C。
- ADC 模拟区域远离 MOSFET 输出和负载回路。
- MOSFET 负载电流回路短且宽。
- 顶层和底层尽量保持连续 GND。
- 安装孔、USB-C 方向、连接器可达性和丝印由用户人工核对。

不要为这些内容创建没有明确意义的复杂规则。

## 13. 最终 DRC 检查项

最终应启用并检查：

- Clearance
- Short-Circuit
- Un-Routed Net
- Width
- Routing Via Style
- Layer Pairs / Via Type
- Hole Size
- Hole-To-Hole Clearance
- Minimum Annular Ring
- Minimum Solder Mask Sliver
- Silk To Solder Mask Clearance
- Board Outline Clearance

`Layer Pairs / Via Type` 用于确认当前只使用 Top-to-Bottom 通孔。以上仅表示“应检查”，不表示 Batch DRC 已运行或任何检查已通过。最终应由用户在 Altium Designer 中完整运行 Batch DRC，并确认所有问题均已解决或有明确、合理的豁免。

## 14. 官方依据

官方页面核对日期：`2026-07-28`。

- [JLCPCB PCB Manufacturing Capabilities](https://jlcpcb.com/capabilities/pcb-capabilities/)：用于核对层数、走线、孔、阻焊和丝印等制造能力。
- [JLCPCB PCB Assembly Capabilities](https://jlcpcb.com/capabilities/pcb-assembly-capabilities)：用于核对 Economic PCBA 与 Standard PCBA 的装配面数、尺寸和可选工艺边界。
- [JLCPCB 在线报价页](https://cart.jlcpcb.com/quote)：当前计价界面中，`0.30 mm (≈11.8 mil)` 过孔不增加小孔费用；该界面、价格、促销和免费条件可能变化。

`0.30 mm (≈11.8 mil)` 过孔在当前计价条件下属于标准低成本选择，但最终制造能力、费用、促销资格和工程处理方式均以下单页面与工程审核为准，不作为永久保证。

## 装配与下单提醒

- 如果所有需要贴装的器件都位于同一面，可优先采用 Economic PCBA。
- 如果需要双面贴装，应使用 Standard PCBA。
- 当前约 `70 mm × 50 mm` 单板有一边小于 Standard PCBA 当前列出的 `70 mm` 单板下限，可能需要拼板或调整尺寸，必须在下单前复核。
- 阻焊颜色、表面处理、数量、铜厚、板厚及其他订单项应在投产前逐项复核。
- 当前 PCB 尚未完成 SMT 可制造性审核，不能据本文档声称已达到可制造或可投产状态。
