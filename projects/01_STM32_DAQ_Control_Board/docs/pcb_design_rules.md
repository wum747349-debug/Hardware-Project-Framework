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
- 本文档中的规则值尚未写入或核实到实际 `.PcbDoc`。
- AI/Codex 未运行 Altium Designer、未配置规则、未运行 Batch DRC。
- 最终制造能力、价格和订单选项必须在下单时再次核对。
- 本规则使用 mm 作为统一单位。
- 本项目为两层低压、低速、小电流开发板，不使用制造极限。
- 本文档不代表 PCB Review、SMT 可制造性审核或 DRC 已完成。

## 1. 制造基线

```text
FR-4
2 layers
1.60mm nominal finished thickness
1 oz outer copper
Through vias only
No blind/buried vias
No controlled-impedance claim
Target: JLCPCB SMT/PCBA
```

两层 USB 数据线只建立线宽、间距、同层、短路径和回流连续性等几何一致性规则，不声明或保证实现 `90Ω` 差分阻抗。

## 2. 规则优先级原则

- 具体网络 Width 规则优先于 `All` 默认 Width 规则。
- 默认规则放在最低优先级。
- Differential Pair Routing 单独管理 `USB_DP` / `USB_DM`。
- 不建立没有明确需求的复杂 Net Class、阻抗或高速规则。
- Scope 可直接使用明确网络查询，不要求额外导出 Net Class 报告。
- 下文 Routing Width 规则按列出顺序从高到低配置；若 Altium Designer 中存在其他重叠规则，用户应人工核对最终优先级和适用对象。

## 3. Electrical Clearance

```text
Rule Name: Clearance_Default
Scope 1: All
Scope 2: All
Minimum Clearance: 0.20mm
```

## 4. Routing Width

以下规则按优先级从高到低排列。

### Width_Load_500mA

Scope：

```text
InNet('VLOAD_EXT1') Or
InNet('VLOAD_EXT2') Or
InNet('MOS_OUT1') Or
InNet('MOS_OUT2')
```

数值：

```text
Min: 0.50mm
Preferred: 0.80mm
Max: 1.20mm
```

### Width_Power_5V

Scope：

```text
InNet('VBUS_RAW') Or
InNet('VBUS_FUSED') Or
InNet('+5V_SYS')
```

数值：

```text
Min: 0.30mm
Preferred: 0.50mm
Max: 1.00mm
```

### Width_Power_3V3

Scope：

```text
InNet('3.3V') Or
InNet('VDDA_3V3')
```

数值：

```text
Min: 0.25mm
Preferred: 0.40mm
Max: 0.80mm
```

### Width_GND

Scope：

```text
InNet('GND')
```

数值：

```text
Min: 0.30mm
Preferred: 0.50mm
Max: 1.50mm
```

GND 主要使用顶层和底层 Polygon；本 Width 规则只控制独立走线。

### Width_Default_Signal

```text
Scope: All
Min: 0.15mm
Preferred: 0.20mm
Max: 0.50mm
Priority: 最低
```

## 5. Routing Via Style

```text
Rule Name: ViaStyle_Default
Scope: All

Via Diameter:
Min: 0.60mm
Preferred: 0.60mm
Max: 1.00mm

Via Hole:
Min: 0.30mm
Preferred: 0.30mm
Max: 0.50mm
```

- 默认过孔为 `0.60/0.30mm`。
- 默认使用 Top-to-Bottom 通孔。
- 禁止盲孔、埋孔和未经确认的 Via-in-Pad。
- 普通过孔默认双面盖油，测试用途过孔除外。

## 6. Hole 与 Annular Ring

```text
Rule Name: HoleSize_Via
Scope: IsVia
Min: 0.30mm
Max: 0.50mm
```

```text
Rule Name: HoleSize_Pad
Scope: 有钻孔的 Pad
Min: 0.50mm
Max: 6.30mm
```

`HoleSize_Pad` 只适用于有钻孔的 Pad。用户应在当前 Altium Designer 版本中确认能准确排除 SMD Pad 的查询表达式后再配置。

```text
Rule Name: HoleToHoleClearance
Minimum: 0.45mm
```

```text
Rule Name: MinimumAnnularRing_Via
Scope: IsVia
Minimum: 0.15mm
```

```text
Rule Name: MinimumAnnularRing_Pad
Scope: IsPad
Minimum: 0.20mm
```

SMD Pad 没有钻孔，不应被错误理解为违反 PTH 最小孔径。

## 7. USB Differential Pair

需要由用户在 Altium Designer 中人工建立：

```text
Pair Name: USB_FS
Positive Net: USB_DP
Negative Net: USB_DM
```

Differential Pairs Routing：

```text
Width:
Min: 0.15mm
Preferred: 0.20mm
Max: 0.25mm

Gap:
Min: 0.15mm
Preferred: 0.20mm
Max: 0.25mm
```

布局要求：

```text
Length mismatch target: <=1.0mm
Keep both traces on the same layer
Keep routing short
Avoid vias where practical
Maintain continuous GND return
Do not claim controlled impedance
```

如果当前 Altium 工程尚未定义 `USB_FS` Differential Pair，本文档只要求用户人工创建，不声称该 Pair 已经存在。

## 8. Mask 和 Paste

```text
Solder Mask Expansion: 0.05mm
Minimum Solder Mask Sliver: 0.10mm
Paste Mask Expansion: 0.00mm
```

- `0.10mm` 阻焊桥按绿色阻焊基线。
- 如果下单改为黑色或白色阻焊，改为至少 `0.13mm`。
- LQFP、USB-C 等细间距焊盘若触发阻焊桥问题，应优先检查具体封装并局部改为 `0mm` Expansion，不得直接降低全局规则。
- Paste Mask 默认跟随焊盘；特殊器件根据器件或钢网要求单独覆盖。

## 9. Silkscreen

```text
Silk To Solder Mask Clearance: 0.15mm
Minimum silkscreen line width: 0.15mm
Minimum text height: 1.00mm
```

最小线宽和字符高度如果当前 Altium Designer 版本不能直接建立对应 DRC，则作为人工检查规范。

## 10. Board Outline Clearance

```text
Board Outline Clearance: 0.25mm
```

该规则用于铜、走线、焊盘和过孔到铣边板框的间距。

USB-C、连接器或其他器件如因结构要求靠近板边，应通过器件封装和机械位置人工核对，不得把整个板边规则降为 `0`。

## 11. Polygon Connect Style

推荐值：

```text
普通焊盘连接 GND Polygon：
Thermal Relief
4 spokes
Air Gap: 0.20mm
Spoke Width: 0.25mm

GND stitching vias：
Direct Connect
```

MOSFET、电源和负载焊盘如需 Direct Connect，应按具体焊盘单独处理。

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
- Differential Pair Routing
- Routing Via Style
- Hole Size
- Hole-To-Hole Clearance
- Minimum Annular Ring
- Minimum Solder Mask Sliver
- Silk To Solder Mask Clearance
- Board Outline Clearance

以上仅表示“应检查”，不表示 Batch DRC 已运行或任何检查已通过。最终应由用户在 Altium Designer 中完整运行 Batch DRC，并确认所有问题均已解决或有明确、合理的豁免。

## 14. 官方依据

官方页面核对日期：`2026-07-28`。

- [JLCPCB PCB Manufacturing Capabilities](https://jlcpcb.com/capabilities/pcb-capabilities/)：用于核对层数、走线、孔、阻焊和丝印等制造能力。
- [JLCPCB PCB Assembly Capabilities](https://jlcpcb.com/capabilities/pcb-assembly-capabilities)：用于核对 Economic PCBA 与 Standard PCBA 的装配面数、尺寸和可选工艺边界。
- [JLCPCB 在线报价页](https://cart.jlcpcb.com/quote)：当前计价界面中，`0.30mm` 过孔不增加小孔费用；该界面、价格、促销和免费条件可能变化。

`0.30mm` 过孔在当前计价条件下属于标准低成本选择，但最终制造能力、费用、促销资格和工程处理方式均以下单页面与工程审核为准，不作为永久保证。

## 装配与下单提醒

- 如果所有需要贴装的器件都位于同一面，可优先采用 Economic PCBA。
- 如果需要双面贴装，应使用 Standard PCBA。
- 当前约 `70mm × 50mm` 单板有一边小于 Standard PCBA 当前列出的 `70mm` 单板下限，可能需要拼板或调整尺寸，必须在下单前复核。
- 阻焊颜色、表面处理、数量、铜厚、板厚及其他订单项应在投产前逐项复核。
- 当前 PCB 尚未完成 SMT 可制造性审核，不能据本文档声称已达到可制造或可投产状态。
