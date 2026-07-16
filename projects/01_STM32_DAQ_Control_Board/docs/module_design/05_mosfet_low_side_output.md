# MOSFET 低边输出设计说明

> 文档状态：当前有效，模块详细依据
> 适用版本：Rev A

## 1. 模块定位

第一版设计 2 路 N-MOSFET 低边开关输出，用于控制 5V/12V 小电流低压负载。该模块用于训练 STM32 GPIO 控制外部负载、低边 MOSFET 开关、续流保护、接口标识、测试点和后续 PCB Layout 能力。

## 2. 使用边界

- 输出通道数：2 路。
- 输出形式：N-MOSFET 低边开关。
- 主选 MOSFET：`AO3400A`。
- 外部负载电源：`VLOAD_EXT1 / VLOAD_EXT2`。
- `VLOAD` 范围：建议 `5V-12V`，最大不超过 `12V`。
- 推荐使用电流：`<=300mA`。
- 设计预留目标：`<=500mA`。
- 外部负载电源必须与板子 `GND` 共地。
- 适合小电流 LED 模块、蜂鸣器、小风扇、继电器线圈等低压负载实验。
- 不作为大电流电机驱动模块使用。
- 若驱动感性负载，必须保留续流二极管或其他保护路径。

## 3. MOSFET 选型依据

`AO3400A` 进入 MOSFET 低边输出主选。

datasheet 关键参数：

- 类型：30V N-Channel MOSFET。
- 封装：`SOT-23`。
- `VDS = 30V`。
- `ID = 5.7A @ VGS=10V` 条件下规格值。
- `RDS(on) < 32mΩ @ VGS=4.5V`。
- `RDS(on) < 48mΩ @ VGS=2.5V`。
- `VGS` 绝对最大额定值：`±12V`。

本项目采用 STM32F103C8T6 的 3.3V GPIO 直接驱动 MOSFET Gate。由于 AO3400A 在 `VGS=2.5V` 和 `VGS=4.5V` 条件下均给出了较低 `RDS(on)`，因此适合本项目 3.3V GPIO 直接驱动的小电流低边开关场景。

按最保守 `RDS(on)=48mΩ` 估算，`I=0.5A` 时导通损耗约为：

```text
P = I^2 * R = 0.5^2 * 0.048 ≈ 0.012W
```

在本项目 `<=500mA` 预留目标下，导通损耗很低，`SOT-23` 封装基本够用。但不能因为 datasheet 中 `ID` 标称较大，就将该模块作为大电流输出模块使用。本项目仍按低压小电流训练板设计。

## 4. MCU GPIO 分配

当前原理图网络名已调整为：

| 通道 | MCU 引脚 | 网络名 | 说明 |
|---|---|---|---|
| MOSFET 输出 1 | `PB0` | `MOS_CTRL1` | 控制 Q1 Gate |
| MOSFET 输出 2 | `PB1` | `MOS_CTRL2` | 控制 Q2 Gate |

选择 `PB0 / PB1` 的原因：

- 两者可作为普通 GPIO 推挽输出使用。
- 避开 `PA0/PA1` ADC 输入、`PA9/PA10` USART1、`PA13/PA14` SWD 等关键功能脚。
- `PB0/PB1` 保留 `TIM3_CH3/TIM3_CH4` 双路硬件 PWM 能力，后续可用于 LED 调光、小风扇 PWM 或蜂鸣器控制实验。
- 与当前 2 路 MOSFET 输出需求匹配。

## 5. 每路电路结构

每路 MOSFET 低边输出采用相同结构。

通道 1：

```text
STM32 PB0 / MOS_CTRL1
-> R1 100Ω 栅极串联电阻
-> GATE1
-> Q1 AO3400A Gate

GATE1
-> R3 100kΩ
-> GND
```

Q1 AO3400A：

- Gate 接 `GATE1`。
- Source 接 `GND`。
- Drain 接 `MOS_OUT1`。

H1 作为第一路外部输出接口：

- `H1-1` 接 `VLOAD_EXT1`。
- `H1-2` 接 `MOS_OUT1`。
- `H1-3` 接 `GND`。

D1 使用 `SS14` 作为续流二极管：

- D1 阴极 K 接 `VLOAD_EXT1`。
- D1 阳极 A 接 `MOS_OUT1`。

测试点：

- `TP_GATE1` 接 `GATE1`。
- `TP_OUT1` 接 `MOS_OUT1`。

通道 2：

```text
STM32 PB1 / MOS_CTRL2
-> R6 100Ω 栅极串联电阻
-> GATE2
-> Q2 AO3400A Gate

GATE2
-> R7 100kΩ
-> GND
```

Q2 AO3400A：

- Gate 接 `GATE2`。
- Source 接 `GND`。
- Drain 接 `MOS_OUT2`。

H3 作为第二路外部输出接口：

- `H3-1` 接 `VLOAD_EXT2`。
- `H3-2` 接 `MOS_OUT2`。
- `H3-3` 接 `GND`。

D2 使用 `SS14` 作为续流二极管：

- D2 阴极 K 接 `VLOAD_EXT2`。
- D2 阳极 A 接 `MOS_OUT2`。

测试点：

- `TP_GATE2` 接 `GATE2`。
- `TP_OUT2` 接 `MOS_OUT2`。

## 6. 栅极电阻和下拉电阻

每路 Gate 前串联 `100Ω` 电阻：

- 限制 GPIO 对 MOSFET 栅极电容的瞬态充放电电流。
- 减小开关沿过快造成的振铃和 EMI 风险。
- 对本项目低频开关 / 低速 PWM 场景足够。

每路 Gate 对 GND 下拉 `100kΩ`：

- 保证 MCU 上电复位、下载调试或 GPIO 高阻期间 MOSFET 默认关断。
- 防止 Gate 悬空导致 MOSFET 误导通。
- 不会明显增加 GPIO 驱动负担。

## 7. 外部负载接法

以第一路 H1 为例：

- 外部电源正极 `+5V / +12V` 接 `H1-1 VLOAD_EXT1`。
- 负载一端接 `H1-1 VLOAD_EXT1`。
- 负载另一端接 `H1-2 MOS_OUT1`。
- 外部电源负极接 `H1-3 GND`。

即负载接在 `H3-1` 和 `H3-2` 之间，外部电源接在 `H3-1` 和 `H3-3` 之间。

MOSFET 导通时电流路径为：

```text
外部电源正极
-> H1-1 / VLOAD_EXT1
-> 外部负载
-> H1-2 / MOS_OUT1
-> Q1 AO3400A
-> GND
-> 外部电源负极
```

因此该模块是低边开关，控制的是“负载负端是否接地”。

第二路 H3 同理：

- `H3-1`：`VLOAD_EXT2`。
- `H3-2`：`MOS_OUT2`。
- `H3-3`：`GND`。

## 8. 续流二极管设计说明

`D1 / D2` 使用 `SS14`，作为感性负载的续流保护器件。

当前已补充 SS14 datasheet，本项目只提取与续流保护相关的参数：

| 参数 | datasheet 规格 | 本项目意义 |
|---|---|---|
| 器件 | `SS14` | 用作 D1/D2 感性负载续流二极管 |
| 封装 | `SMA / DO-214AC` | 需按实际封装和焊盘检查 PCB 库 |
| 应用方向 | Free Wheeling / Polarity Protection | 符合本项目续流保护用途 |
| 最大重复反向电压 | `VRRM = 40V` | 覆盖本项目 `VLOAD 5V-12V` 边界 |
| 平均正向电流 | `IF(AV) = 1.0A` | 高于本项目 `<=300mA` 推荐、`<=500mA` 预留目标 |
| 非重复浪涌电流 | `IFSM = 40A` | 对短时续流冲击有余量，但不能替代负载能量评估 |
| 正向压降 | SS12-SS14 组 `VF max = 500mV @ IF=1A` | 用于估算续流时 MOS_OUT 被钳位到约 `VLOAD_EXT + VF` |
| 功耗 / 热阻 | `PD = 1.1W`，`RθJA = 88°C/W` | 后续若驱动更高能量感性负载需重新评估温升 |
| 极性标识 | Color band denotes cathode | PCB Layout 和焊接时色带端应接 `VLOAD_EXT` |

正确方向：

- 阴极 K，也就是封装色带端 / 原理图竖线端，接 `VLOAD_EXT`。
- 阳极 A 接 `MOS_OUT`。

正常导通时：

- MOSFET 导通，`MOS_OUT` 被拉低到接近 GND。
- `VLOAD_EXT` 高于 `MOS_OUT`。
- SS14 反向截止，不参与负载供电。

MOSFET 关断感性负载时：

- 继电器线圈、电机、电磁阀等感性负载中的电流不能瞬间消失。
- 关断瞬间电感会抬高 `MOS_OUT` 节点电压。
- 当 `MOS_OUT` 高于 `VLOAD_EXT` 一个二极管正向压降时，SS14 导通。
- 电感电流通过“负载线圈 -> MOS_OUT -> SS14 -> VLOAD_EXT -> 负载线圈”形成局部续流回路。
- 电感能量通过续流回路逐渐释放，避免 `MOS_OUT` 产生过高尖峰电压，从而保护 AO3400A。

必须强调：续流二极管不能反接。若反接，MOSFET 导通时可能形成 `VLOAD_EXT -> 二极管 -> MOSFET -> GND` 的近似短路通路。PCB Layout 和焊接时必须确认 SS14 色带端接 `VLOAD_EXT`。

## 9. 接口丝印建议

H1 丝印建议：

- `VLOAD1 5-12V`
- `OUT1`
- `GND`

H3 丝印建议：

- `VLOAD2 5-12V`
- `OUT2`
- `GND`

模块附近建议增加总说明丝印或文档说明：

- `VLOAD 5-12V ONLY`
- `COMMON GND REQUIRED`
- `OUTx is low-side switched output`
- `Inductive load requires flyback diode`

## 10. 测试点设计

| 测试点 | 网络 | 用途 |
|---|---|---|
| `TP_GATE1` | `GATE1` | 测第一路 MOSFET 栅极驱动电压 |
| `TP_OUT1` | `MOS_OUT1` | 测第一路低边输出节点 |
| `TP_GATE2` | `GATE2` | 测第二路 MOSFET 栅极驱动电压 |
| `TP_OUT2` | `MOS_OUT2` | 测第二路低边输出节点 |

调试时可用万用表或示波器检查：

- `MOS_CTRL` 为低时，GATE 应被 `100kΩ` 下拉到低电平，`MOS_OUT` 不应被拉低。
- `MOS_CTRL` 为高时，GATE 约为 `3.3V`，MOSFET 导通，`MOS_OUT` 应接近 GND。
- 接感性负载关断时，`MOS_OUT` 尖峰应被续流二极管限制。

## 11. 风险与后续检查项

1. AO3400A 引脚映射是否正确：Gate 接 GATE，Source 接 GND，Drain 接 MOS_OUT。
2. `D1 / D2` SS14 极性是否正确：阴极 K 接 `VLOAD_EXT`，阳极 A 接 `MOS_OUT`。
3. `H1 / H3` 引脚定义是否清晰：Pin1 = `VLOAD_EXT`，Pin2 = `MOS_OUT`，Pin3 = `GND`。
4. 外部电源必须与板子 GND 共地：`H1/H3` 的 GND 必须与系统 GND 相连，文档和丝印需要提醒 `COMMON GND`。
5. 电流边界：推荐 `<=300mA`，设计预留 `<=500mA`，不作为大电流输出使用。
6. 负载类型：电阻性负载、LED 模块等风险较低；继电器、电机、电磁阀等感性负载必须使用 `D1/D2` 续流保护；若未来驱动更高能量感性负载，需要重新评估 TVS、栅极保护、走线宽度和热耗散。
7. PCB Layout：MOSFET Source 到 GND 回流路径要短；`MOS_OUT` 走线按负载电流适当加宽；`D1/D2` 靠近接口和 `MOS_OUT / VLOAD` 回路放置；Gate 走线远离 `MOS_OUT` 大电流开关节点；`TP_GATE / TP_OUT` 放在便于探测的位置；`H1/H3` 附近丝印必须清楚，避免用户误接。
