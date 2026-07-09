# 设计说明

## 当前设计定位

本项目第一版定位为 `STM32F103C8T6 数据采集/控制开发板`，重点训练低压嵌入式硬件设计的完整流程：需求定义、最小系统、电源输入与保护、通信接口、ADC 输入、MOSFET 输出、PCB Layout、上电调试和测试验证。

第一版优先保证可实现、可焊接、可调试和文档完整，不追求复杂功能，不做高速接口，不做大电流输出，不做高精度模拟前端。

## MCU 选择说明

MCU 确定为 `STM32F103C8T6`。

选择原因：

- 器件常见，资料丰富。
- 适合 STM32 入门、最小系统和基础外设训练。
- LQFP48 方向适合手焊练习和 2 层板布局训练。
- Keil、STM32CubeMX、ST-Link/SWD 调试链路成熟。

后续原理图阶段需要根据 STM32F103C8T6 datasheet / reference manual 核对封装、引脚、电源脚、去耦、BOOT、NRST、SWD、HSE 和 ADC 等细节。

## MCU 最小系统草图设计说明

当前 MCU 最小系统仍属于原理图前草图和参数反推阶段，用于记录连接关系、草图参数和后续审查重点，不生成最终 BOM。

MCU 使用 `STM32F103C8T6`，封装按 `LQFP48`。本模块目标是完成 STM32 最小系统原理图草图，包括供电、去耦、VDDA/VSSA、VBAT、NRST、BOOT0、HSE 8MHz 晶振、SWD 下载调试接口和基础测试点。

### 数字电源与去耦

- `VDD_1`、`VDD_2`、`VDD_3` 全部接 `3.3V`。
- `VSS_1`、`VSS_2`、`VSS_3` 全部接 `GND`。
- 每个 VDD 附近放置 `100nF` 去耦电容。
- MCU 附近额外放置 `4.7uF` 总去耦电容，Layout 时尽量靠近 `VDD_3`。
- `VBAT` 不使用备用电池时接 `3.3V`，避免悬空；可根据需要预留 `100nF` 去耦。

### VDDA / VSSA 模拟电源

- `STM32F103C8T6 LQFP48` 中 pin8 为 `VSSA`，pin9 为 `VDDA`。
- `VSSA` 接 `GND`，`VDDA` 接独立网络 `VDDA_3V3`。
- `VDDA_3V3` 由 `3.3V` 通过 `0Ω` 电阻 `R2` 接入，`R2` 作为磁珠/小电阻替换预留。
- `VDDA_3V3` 对 `GND` 放置 `100nF + 1uF` 去耦电容，靠近 VDDA/VSSA 引脚。
- 第一版建议 `R2` 先使用 `0Ω`、`0603` 普通贴片电阻，不直接使用磁珠。
- 原因：本项目 ADC 只是低速采集和功能验证，不追求高精度模拟测量；`0Ω` 更简单、可靠、方便调试，也便于后续发现 ADC 抖动时替换为磁珠。
- `VDDA` 不能悬空，也不能与 `VSSA` 接反。`VDDA` 主要给 ADC、模拟相关模块、复位/内部 RC/PLL 等部分供电，并影响 ADC 采集稳定性。

### NRST 复位电路

- `NRST` 接复位按键到 `GND`。
- `NRST` 对 `GND` 放置 `100nF` 电容。
- `NRST` 同时引出到 SWD 接口。
- STM32 NRST 内部已有弱上拉，因此外部 `10k` 上拉可不放或预留 DNP；当前草图以按键 + `100nF` 为主。
- 后续原理图审查时确认 `NRST` 网络标签必须接到 pin7 `NRST`，不能误接到 HSE 晶振脚。

### BOOT0 启动配置

- `BOOT0` 通过 `10k` 下拉到 `GND`，默认从用户 Flash 启动。
- 预留 3Pin 跳帽 `H1`：`H1-1` 接 `3.3V`，`H1-2` 接 `BOOT0`，`H1-3` 接 `GND`。
- 不插跳帽时 `BOOT0` 由 `10k` 下拉，默认运行用户程序。
- 跳帽接 `1-2` 时 `BOOT0` 拉高，可进入系统 Bootloader。
- 跳帽接 `2-3` 时 `BOOT0` 强制拉低，仍从 Flash 启动。
- 注意不要画成会导致 `3.3V` 和 `GND` 被跳帽短接的结构。

### HSE 8MHz 晶振

- HSE 使用 `8MHz` 无源晶振。
- `STM32F103C8T6 LQFP48` 中 pin5 = `PD0 / OSC_IN`，pin6 = `PD1 / OSC_OUT`。
- 8MHz 晶振 `X1` 接在 `OSC_IN` 与 `OSC_OUT` 之间。
- `OSC_IN` 对 `GND` 放置负载电容 `C6`，`OSC_OUT` 对 `GND` 放置负载电容 `C7`。
- 当前草图 `C6/C7` 暂按 `10pF` 标注，后续根据具体晶振 datasheet 的负载电容 `CL`、PCB 寄生电容和 STM32 硬件设计资料反推最终值。
- `PC14/PC15` 是 LSE 32.768kHz 低速晶振脚，不是本项目 8MHz HSE 晶振脚。本项目暂不使用 LSE，`PC14/PC15` 可先悬空。
- Layout 时晶振和负载电容尽量靠近 `OSC_IN/OSC_OUT`，走线短、对称，远离高速/大电流信号。

### SWD 调试接口

- 保留 `1x5` SWD 接口 `H2`：`3.3V`、`SWDIO`、`SWCLK`、`NRST`、`GND`。
- `SWDIO` 使用 `PA13`，`SWCLK` 使用 `PA14`。
- 网络名统一使用 `SWDIO`、`SWCLK`、`NRST`，不建议使用容易混淆的 `CLK`。
- 后续建议预留测试点：`3.3V`、`GND`、`NRST`、`SWDIO`、`SWCLK`。

### 当前原理图草图检查结论

MCU 最小系统草图已完成第一轮修改。已完成内容包括：VDD/VSS 连接、基础去耦、VBAT 接 3.3V、VDDA/VSSA 简单模拟电源、NRST 复位、BOOT0 跳帽、HSE 8MHz、SWD 接口。

后续原理图审查 / PCB Layout 前重点检查：

1. `VDDA/VSSA` 是否接反。
2. `NRST` 是否误接到 `OSC_OUT`。
3. `BOOT0` 跳帽是否会造成 `3.3V` 与 `GND` 短接。
4. HSE 负载电容最终值是否根据晶振 `CL` 反推。
5. `4.7uF` 总去耦电容是否靠近 `VDD_3`。
6. 晶振和 VDDA 去耦在 PCB 上是否靠近 MCU。

## 时钟设计说明

外部高速晶振确定为 `8MHz`，用于训练 STM32 常见 HSE 时钟设计。

晶振型号、负载电容、匹配电容、启动条件、布线和接地处理后续必须根据 STM32F103C8T6 datasheet、reference manual 和 ST 硬件设计资料核对。本阶段 HSE 草图已按 8MHz 无源晶振、`OSC_IN/OSC_OUT` 两端各接负载电容的方式记录，`C6/C7=10pF` 只是草图标注值，不是最终定稿参数。

## PCB 尺寸与结构说明

第一版 PCB 尺寸暂定约 `70mm x 50mm`，这个尺寸用于约束第一版复杂度，同时保留 MCU 最小系统、电源、USB-C、排针、ADC 前端、MOSFET 输出和测试点的基本布局空间。

后续 Layout 前可根据接口位置、测试点可达性、安装孔、丝印清晰度和走线情况微调。第一版可预留 2-4 个安装孔，孔径、边距和禁布区在 PCB 结构规划阶段再确认。

## USB-C 与串口通信说明

第一版使用 USB-C 作为 5V 供电入口，同时通过 USB 转 UART 芯片实现电脑与 STM32 的串口通信。

采用 USB 转 UART，而不是 STM32 原生 USB，原因是：

- 降低第一版固件复杂度。
- 降低 USB 硬件调试复杂度。
- 电脑端 COM 串口更适合早期打印日志、调试命令和数据上传。
- 有利于先把电源、最小系统、串口、ADC 和 MOSFET 控制链路跑通。

设计边界：

- USB-C D+ / D- 连接 USB 转 UART 芯片。
- USB-C D+ / D- 不连接 STM32 PA11 / PA12。
- STM32 PA11 / PA12 第一版不作为 USB 功能使用。
- USB 转 UART 与 STM32 之间使用 3.3V UART 电平。
- 推荐使用 USART1，USB 转 UART TXD 接 PA10，USB 转 UART RXD 接 PA9，注意 TX/RX 交叉。

USB-C CC 电阻、ESD/TVS、USB 转 UART 芯片型号、供电方式和逻辑电平后续需要根据 datasheet / application note 核对。

### USB 转 UART / CH340C 草图方案

当前 USB 转 UART 方案已从候选比较收敛为 `CH340C` 主选，位号暂定 `U3`，封装按 `SOP-16`。本项目第一版使用 USB-C 供电 + USB 转 UART，不使用 STM32 原生 USB；CH340C 用于电脑端 COM 串口调试、日志输出、ADC 数据上传和控制命令下发。

#### CH340C 供电与去耦

- CH340C 按 `3.3V` 供电方案设计。
- `Pin16 VCC` 接 `3.3V`。
- `Pin4 V3` 接 `3.3V`。
- `Pin1 GND` 接 `GND`。
- `C13 = 100nF`，`3.3V -> GND`，靠近 `VCC`。
- `C14 = 100nF`，`3.3V -> GND`，靠近 `V3`。
- `C15 = 1uF`，`3.3V -> GND`，作为 CH340C 局部储能电容。
- 不采用 CH340C 5V 供电后直连 STM32 UART 的方案，以避免 5V/3.3V 电平风险。

#### USB 数据线连接

- USB-C 模块引出的 `USB_DP` 接 CH340C `Pin5 D+ / UD+`。
- USB-C 模块引出的 `USB_DM` 接 CH340C `Pin6 D- / UD-`。
- CH340C datasheet 建议 `UD+ / UD-` 直接连接 USB 总线，本项目草图不在 `USB_DP / USB_DM` 上串联 `22Ω` 电阻。
- USB-C 的 `D+ / D-` 不连接 STM32 `PA11 / PA12`。

#### USB 数据线 ESD 保护

- `D2` 使用 `TPD2EUSB30DRTR-N`，作为 `USB_DP / USB_DM` 的双路低电容 ESD 保护器件。
- `D2 Pin1 / I/O` 接 `USB_DP`。
- `D2 Pin2 / I/O` 接 `USB_DM`。
- `D2 Pin3 / GND` 接 `GND`。
- D2 是并联钳位保护器件，不是串联器件。
- 当前记录的规格书关键参数：`VRWM=5V`，I/O-to-GND 结电容典型 `0.45pF`、最大 `0.6pF`，IEC 61000-4-2 接触放电 `±20kV`、空气放电 `±25kV`。
- PCB Layout 时 D2 应靠近 USB-C 接口放置，GND 回流路径要短，优先就近接地铜或地过孔。
- D2 不接 `3.3V`，也不接 `VBUS / 5V`。

#### UART 到 STM32

- CH340C `Pin2 TXD` 接 STM32 `USART1_RX / PA10`，当前网络名为 `MCU_RX`。
- CH340C `Pin3 RXD` 接 STM32 `USART1_TX / PA9`，当前网络名为 `MCU_TX`。
- TX/RX 必须交叉连接。
- 后续可考虑将网络名进一步规范为 `MCU_USART1_RX_PA10`、`MCU_USART1_TX_PA9`，或在文档中说明当前网络名是从 MCU 视角命名。

#### 模式脚和未用脚

- CH340C `Pin15 R232` 接 `GND`，用于保持普通 TTL UART 模式，不启用辅助 RS232 模式。
- `Pin7 NC` 加 No Connect 标记。
- `Pin8 OUT#`、`Pin9 CTS#`、`Pin10 DSR#`、`Pin11 RI#`、`Pin12 DCD#`、`Pin13 DTR#`、`Pin14 RTS#` 当前均不使用，加 No Connect 标记。
- 第一版不做 `DTR/RTS` 自动下载电路，仍使用 SWD 下载调试和 BOOT0 跳帽。

#### 后续 PCB 检查项

1. `D2 TPD2EUSB30DRTR-N` 是否靠近 USB-C 接口，且先于较长 USB 数据线进入板内区域。
2. `USB_DP / USB_DM` 从 USB-C 到 D2、再到 CH340C 的走线是否短、成对、少过孔，并尽量避免穿越分割地或强干扰区域。
3. D2 的 `GND` 是否就近接地铜或地过孔，回流路径是否短直。
4. CH340C 的 `C13/C14/C15` 是否靠近对应电源引脚，3.3V 与 GND 回路是否紧凑。
5. CH340C `TXD/RXD` 到 STM32 `PA10/PA9` 是否交叉正确，网络名是否明确说明为 MCU 视角。
6. `R232` 是否可靠接地，未用握手脚和 `NC` 脚是否加 No Connect 标记。
7. USB-C `D+ / D-` 是否只接 CH340C，不误接 STM32 `PA11/PA12`。
8. PCB 丝印或调试文档是否明确第一版不支持 STM32 原生 USB，也不支持 DTR/RTS 自动下载。

## 电源设计说明

第一版电源路径为 USB-C 输入 5V，经电源保护和电源开关后转换为 3.3V。

3.3V 供电对象包括 STM32、USB 转 UART 芯片逻辑侧、LED、接口上拉和其他低压外围电路。

需要预留或评估：

- 电源开关
- 保险丝或自恢复保险丝
- TVS / ESD 保护
- 输入滤波
- 3.3V 稳压电路
- 电源指示 LED
- 5V、3.3V、GND 测试点

电源扩展边界：

- 可以单独预留若干个 `3.3V` 电源排针。
- `3.3V` 排针允许给外部低功耗模块供电。
- 外部模块从板载 `3.3V` 取电时，最大电流限制为 `<=100mA`。
- `5V` 引脚主要用于测试点或低风险扩展。
- 后续若把 `5V` 作为外部供电输出，需要结合 USB 输入保护、保险丝、电源开关和走线宽度重新核对。

这些限制会影响 LDO 输出能力、热耗散、保险丝、电源开关、电源测试点和电源排针选型。保险丝、TVS、LDO、USB-C CC 电阻、电源指示 LED 限流电阻等参数后续必须根据器件 datasheet / application note 核对。

## USB-C 供电 + AP2112K 3.3V 电源模块

本模块用于实现 USB-C 5V 输入、入口保护、板级 5V 开关控制和 AP2112K-3.3TRG1 生成 3.3V 系统电源。当前仍属于模块电路设计说明 / 原理图前参数反推阶段，以下内容记录草图参数、当前主选和后续待核对项，不是最终 BOM。

### 模块功能说明

- USB-C 母座选用 `TYPE-C 16PIN 2MD(073)`，用于本板 USB-C 5V 输入和 USB2.0 `D+ / D-` 接口。
- 当前只使用 USB2.0 与 5V VBUS，不做 USB-PD 协议，不支持 9V/12V 高压输入。
- 5V 输入经自恢复保险丝、VBUS TVS 和电源开关后形成板级 `+5V_SYS`，再进入 AP2112K 生成 `3.3V`。
- 第一版外部 3.3V 供电继续按 `<=100mA` 标注，3.3V 总负载应保持保守，避免 AP2112K SOT25 封装过热。

### USB-C 输入接口连接

| USB-C 引脚 | 网络 / 器件连接 | 说明 |
|---|---|---|
| A4 / A9 / B4 / B9 | `VBUS_RAW` | USB-C 母座刚输入的原始 5V |
| A1 / A12 / B1 / B12 | `GND` | 电源地 |
| A5 / CC1 | `R3 5.1kΩ -> GND` | Type-C UFP 取电设备 CC 下拉 |
| B5 / CC2 | `R4 5.1kΩ -> GND` | Type-C UFP 取电设备 CC 下拉 |
| A6 / B6 | `USB_DP` | USB2.0 D+，后续接 USB 转 UART |
| A7 / B7 | `USB_DM` | USB2.0 D-，后续接 USB 转 UART |
| SBU1 / SBU2 | NC | 本项目暂不使用，原理图应加 NC 标记 |
| EH / Shield | `SHIELD -> R7 0Ω -> GND` | Shield 先通过 0Ω 接地，后续按 EMI/ESD 结果调整 |

CC1/CC2 分别使用 `5.1kΩ` 下拉到 GND，使本板作为 Type-C 取电设备。Shield 通过 `0Ω` 电阻接 GND，便于后续根据 EMI/ESD 测试改为 DNP、磁珠或其他连接方式。

### 入口保护与 5V 系统电源路径

当前电源路径定义为：

```text
USB-C VBUS
-> VBUS_RAW
-> TP_VBUS
-> F1 自恢复保险丝
-> VBUS_FUSED
   ├─ D1 SMF5.0A TVS -> GND
   └─ SW2 单刀单掷电源开关 -> +5V_SYS -> TP_5V -> AP2112 VIN
```

关键网络定义：

| 网络           | 含义                                       |
| ------------ | ---------------------------------------- |
| `VBUS_RAW`   | USB-C 母座刚输入的原始 5V                        |
| `VBUS_FUSED` | 经过 F1 自恢复保险丝后的 5V 节点                     |
| `+5V_SYS`    | 经过 F1 和 SW2 后的板级系统 5V，供 AP2112 VIN 等后级使用 |
| `AP2112 VIN` | AP2112 的 5V 输入脚，用于将 `+5V_SYS` 转换为 3.3V   |
| `3.3V`       | AP2112 输出的板级 3.3V 电源                     |
| `GND`        | 板级参考地                                    |

### 保护器件与开关选型

| 位号              | 当前主选                  | 类型 / 封装              | 关键参数                                             | 用途                                  | 注意事项                               |
| --------------- | --------------------- | -------------------- | ------------------------------------------------ | ----------------------------------- | ---------------------------------- |
| D1 / D_VBUS_TVS | R+O / 宏嘉诚 `SMF5.0A`   | 单向 TVS，SOD-123FL     | VRWM=5V，VBR=6.4V~7.0V，VC=9.2V，IPP=21.7A，IR=400µA | USB-C VBUS 瞬态电压 / ESD 保护            | 只用于 VBUS 电源线保护，不用于 `USB_DP/USB_DM` |
| F1              | R+O / 宏嘉诚 `C46640983` | PPTC 自恢复保险丝，0805     | Vmax=6V，Imax=40A，Ihold=500mA，Itrip=1A            | USB 输入短路、后级严重过流、TVS 失效短路时限流保护       | Vmax=6V，仅适合当前 5V USB 输入设计          |
| SW2             | HCTL / 华灿天禄插件船型开关     | 单刀单掷，约 15mm x 10.5mm | 实际引脚导通关系、孔距和封装尺寸待 PCB 前复核                        | `VBUS_FUSED -> SW2 -> +5V_SYS` 电源开关 | 体积较大，但第一版练习板可以接受                   |

`SMF5.0A` 连接方式：阴极 K / 色环端接 `VBUS_FUSED`，阳极 A 接 `GND`。`USB_DP/USB_DM` 后续需要单独选择低电容 USB ESD 器件。

### AP2112K 3.3V 电源设计

| 项目 | 当前设计 |
|---|---|
| U2 | `AP2112K-3.3TRG1` |
| 类型 | 固定 3.3V LDO |
| 封装 | SOT25 |
| 标称输出能力 | 600mA |
| 推荐 VIN 工作范围 | 2.5V ~ 6.0V |
| 绝对最大电源电压 | 6.5V |
| SOT25 θJA | 184°C/W |

原理图连接：

| AP2112K 引脚 / 网络 | 连接 |
|---|---|
| VIN | `+5V_SYS` |
| GND | `GND` |
| EN | `R5 10kΩ -> +5V_SYS` |
| NC | NC |
| VOUT | `3.3V` |

外围器件：

| 位号   | 参数    | 连接                          | 说明             |
| ---- | ----- | --------------------------- | -------------- |
| C10  | 1µF   | `+5V_SYS -> GND`            | 靠近 VIN         |
| C11  | 1µF   | `3.3V -> GND`               | 靠近 VOUT        |
| C12  | 4.7µF | `3.3V -> GND`               | 3.3V 总线储能      |
| R6   | 1kΩ   | `3.3V -> R6 -> LED1 -> GND` | 3.3V 电源指示灯限流   |
| LED1 | 电源指示灯 | `3.3V -> R6 -> LED1 -> GND` | 指示 AP2112 输出存在 |

AP2112K 虽然标称 600mA，但 5V 转 3.3V 时会产生线性损耗，不建议长期接近满载使用。功耗估算可按 `P=(5V-3.3V)*Iout` 计算；SOT25 θJA 约 `184°C/W`。例如 `Iout=100mA` 时，功耗约 `0.17W`，理想估算温升约 `31°C`；`Iout=200mA` 时，功耗约 `0.34W`，理想估算温升约 `63°C`。因此第一版建议 3.3V 长期总电流控制在约 `150mA~200mA` 以内，外部 3.3V 排针继续限制 `<=100mA`。

### 测试点设计

| 测试点 | 网络 | 用途 |
|---|---|---|
| `TP_VBUS` | `VBUS_RAW` | 测 USB-C 原始输入 5V |
| `TP_5V` | `+5V_SYS` | 测开关后系统 5V |
| `TP_3V3` | `3.3V` | 测 AP2112 输出 3.3V |
| `TP_GND` | `GND` | 万用表黑表笔或示波器地夹参考点 |

### 风险与注意事项

- USB-C 仅支持 5V 输入，不支持 USB-PD 9V/12V 高压输入；后续 PCB 丝印建议增加 `USB-C 5V ONLY`。
- `SMF5.0A` 是瞬态保护器件，不能替代长期过压保护。
- `F1` 为自恢复保险丝，不是精确限流器。
- `AP2112K-3.3TRG1` 不能按 600mA 长期满载设计，需考虑热耗散。
- `USB_DP/USB_DM` 后续还需要低电容 ESD 保护。
- `SW2` 船型开关封装和引脚导通关系需在 PCB 前复核。
- 所有电源网络命名需保持一致，推荐使用 `VBUS_RAW`、`VBUS_FUSED`、`+5V_SYS`、`3.3V`、`GND`。本项目后续原理图优先统一使用 `3.3V` 作为 3.3V 电源网络名，不再混用 `+3V3`。

### 后续 PCB 检查项

1. USB-C 母座封装、固定脚、0.5mm pitch 焊盘、阻焊和可检查性。
2. `VBUS_RAW -> F1 -> VBUS_FUSED -> SW2 -> +5V_SYS` 走线宽度和回流路径。
3. D1 TVS 从 `VBUS_FUSED` 并联到 `GND`，且靠近 VBUS 入口，GND 回流短直。
4. F1 与 SW2 的封装、电流能力、孔距和实际导通关系。
5. AP2112K 的 C10/C11 是否靠近 VIN/VOUT，C12 是否靠近 3.3V 总线入口。
6. `TP_VBUS`、`TP_5V`、`TP_3V3`、`TP_GND` 是否便于万用表和示波器探测。

## ADC 输入设计说明

第一版设计 2 路 ADC 输入。板级外部接口允许接入 `0-5V` 信号，但 STM32 ADC 引脚实际输入范围为 `0-VDDA`，当前约 `0-3.3V`。STM32 ADC 引脚不能直接承受 5V，因此外部 0-5V 信号进入 MCU 前必须经过分压、限流、滤波和钳位保护。

第一版 ADC 目标是低速电压采集和功能验证，目标采样频率按每通道 `10Hz-1kHz` 级别考虑。不用于高速波形采集，不追求高精度模拟测量。

### ADC 输入通道与接口

| 通道 | MCU 引脚 / ADC 通道 | 外部接口 | 测试点 | 说明 |
|---|---|---|---|---|
| ADC1 | `PA0 / ADC12_IN0` | `ADC1_EXT_IN + GND` 2Pin | `TP_ADC1` | 0-5V 外部输入，经分压、限流、滤波、钳位后进入 MCU |
| ADC2 | `PA1 / ADC12_IN1` | `ADC2_EXT_IN + GND` 2Pin | `TP_ADC2` | 0-5V 外部输入，经分压、限流、滤波、钳位后进入 MCU |

测试点应接在 `330Ω` 串联限流电阻之后、靠近 MCU 的实际 ADC 输入节点，也就是 `ADC12_IN0 / ADC12_IN1` 节点，而不是接在分压前节点。这样调试时测到的是 MCU 实际看到的电压。

### 每路 ADC 前端草图参数

每一路 ADC 输入采用相同结构：

```text
ADCx_EXT_IN
-> 10kΩ / 18kΩ 分压
-> 330Ω 串联限流
-> ADC12_INx 节点
   ├─ 10nF -> GND
   ├─ BAT54S 上下轨钳位到 GND / VDDA_3V3
   └─ TP_ADCx
-> STM32 PA0/PA1
```

| 项目 | 当前草图 |
|---|---|
| 外部输入范围 | `0-5V` |
| MCU ADC 输入范围 | `0-VDDA`，当前约 `0-3.3V` |
| 分压上臂 | `10kΩ` |
| 分压下臂 | `18kΩ` |
| 5V 输入时分压后电压 | `5V * 18kΩ / (10kΩ + 18kΩ) ≈ 3.21V` |
| 串联限流电阻 | `330Ω` |
| ADC 节点滤波电容 | `10nF -> GND` |
| 钳位器件 | `BAT54S`，`SOT-23` |
| BAT54S 接法 | `Pin3` 接 ADC 节点，`Pin1` 接 `GND`，`Pin2` 接 `VDDA_3V3` |

正常输入 `0-5V` 时，分压后 ADC 节点最高约 `3.21V`，低于当前 `VDDA_3V3`，BAT54S 不应长期导通。`10nF` 电容用于在 ADC 节点形成低通滤波，降低外部输入噪声；`330Ω` 电阻用于限制异常钳位电流，并隔离 ADC 采样电容瞬态和外部保护支路。

### BAT54S 上下轨钳位原理

`BAT54S` 内部为串联双肖特基二极管结构。本项目将公共端接 ADC 节点，两端分别接 `GND` 和 `VDDA_3V3`，用于形成上下轨钳位：

- 当 ADC 节点高于 `VDDA_3V3 + VF` 时，上钳位导通，将异常电流导向 `VDDA_3V3`。
- 当 ADC 节点低于 `GND - VF` 时，下钳位导通，将负向异常电压限制在 GND 附近。
- BAT54S 不是让 ADC 长期承受 `3.6V~3.7V`，而是在异常过压时提供限流条件下的外部钳位路径。
- 正常 `0-5V` 输入经 `10kΩ/18kΩ` 分压后约为 `0-3.21V`，BAT54S 不应作为长期导通器件使用。

需要注意：上钳位导通时，异常电流会被导入 `VDDA_3V3`。如果板卡未上电但外部 ADC 输入存在电压，可能通过钳位路径反灌 VDDA，因此 ADC 输入仅限本项目定义的 `0-5V` 正常信号，不支持长期过压输入或带电热插拔滥用场景。

### BAT54S datasheet 依据

当前已阅读的 BAT54S 资料为 `BAT54 THRU BAT54S` SOT-23 肖特基势垒二极管规格书，资料中说明该系列可用于 high speed switching、circuit protection 和 voltage clamping。本项目只提取与 ADC 输入保护相关的参数：

| 参数 | datasheet 规格 | 本项目意义 |
|---|---|---|
| 器件 | `BAT54S` | 选用串联双肖特基结构做 ADC 上下轨钳位 |
| 封装 | `SOT-23` | 适合当前 2 层练习板和手焊/返修 |
| 最大反向电压 | `VR = 30V` | 满足当前低压 ADC 输入保护需求，但不代表 ADC 接口可长期承受 30V |
| 平均正向电流 | `IF(AV) = 0.2A / 200mA` | 需通过前级分压电阻和 330Ω 串联电阻限制钳位电流 |
| 正向压降 | `VF ≤ 320mV @ IF=1mA`，`VF ≤ 400mV @ IF=10mA` | 估算上下轨钳位阈值和异常导通电压 |
| 结电容 | `CT ≤ 10pF` | 对本项目 `10Hz-1kHz` 低速 ADC 功能验证可接受 |
| 反向恢复时间 | `trr ≤ 5ns` | 对低速 ADC 保护不是瓶颈 |
| 反向漏电 | `IR ≤ 2uA @ VR=25V` | 对高精度或高阻抗采样可能引入误差 |

结论：BAT54S 用于第一版 `10Hz-1kHz` 低速 ADC 功能验证是可以接受的。若后续追求高精度、高阻抗采样或更严格误差预算，需要重新评估 BAT54S 的反向漏电、结电容、温度漂移和钳位电流对测量精度的影响。

### 风险与后续检查项

- ADC 输入接口丝印建议标注 `ADC IN 0-5V`，避免误接更高电压。
- ADC 输入仅限 `0-5V` 正常输入，不支持长期过压输入。
- BAT54S 上钳位会把异常电流导入 `VDDA_3V3`，存在板卡未上电时由外部 ADC 输入反灌 VDDA 的风险。
- 前级 `10kΩ/18kΩ` 分压和 `330Ω` 串联电阻用于限制钳位电流，原理图审查时需确认没有被短接或绕过。
- 原理图审查时确认钳位器件必须选 `BAT54S`，不要误选 `BAT54`、`BAT54A` 或 `BAT54C`。
- 原理图审查时确认 `D2/D3` 引脚映射：`Pin3 = ADC 节点`，`Pin1 = GND`，`Pin2 = VDDA_3V3`。
- 原理图审查时确认 `TP_ADC1` 接 `ADC12_IN0`，`TP_ADC2` 接 `ADC12_IN1`，不要交叉命名。
- PCB Layout 时 BAT54S、`10nF` 电容和测试点靠近 MCU ADC 输入节点；外部接口侧可预留 ESD/TVS 焊盘作为后续增强保护。
- 后续仍需结合 STM32 ADC 采样时间、源阻抗、ADC 采样电容和 VDDA 噪声进一步核对采样误差。

## MOSFET 输出设计说明

第一版设计 2 路 N-MOSFET 低边开关输出，用于控制 5V/12V 小电流低压负载。该模块用于训练 STM32 GPIO 控制外部负载、低边 MOSFET 开关、续流保护、接口标识、测试点和后续 PCB Layout 能力。

### 使用边界

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

### MOSFET 选型依据

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

### MCU GPIO 分配

当前原理图网络名已调整为：

| 通道 | MCU 引脚 | 网络名 | 说明 |
|---|---|---|---|
| MOSFET 输出 1 | `PB0` | `MOS_CTRL1` | 控制 Q1 Gate |
| MOSFET 输出 2 | `PB1` | `MOS_CTRL2` | 控制 Q2 Gate |

选择 `PB0 / PB1` 的原因：

- 两者可作为普通 GPIO 推挽输出使用。
- 避开 `PA0/PA1` ADC 输入、`PA9/PA10` USART1、`PA13/PA14` SWD 等关键功能脚。
- 后续可根据需要配置为定时器 PWM 输出，用于 LED 调光、小风扇 PWM 或蜂鸣器控制实验。
- 与当前 2 路 MOSFET 输出需求匹配。

### 每路电路结构

每路 MOSFET 低边输出采用相同结构。

通道 1：

```text
STM32 PB0 / MOS_CTRL1
-> R14 100Ω 栅极串联电阻
-> GATE1
-> Q1 AO3400A Gate

GATE1
-> R15 100kΩ
-> GND
```

Q1 AO3400A：

- Gate 接 `GATE1`。
- Source 接 `GND`。
- Drain 接 `MOS_OUT1`。

H3 作为第一路外部输出接口：

- `H3-1` 接 `VLOAD_EXT1`。
- `H3-2` 接 `MOS_OUT1`。
- `H3-3` 接 `GND`。

D4 使用 `SS14` 作为续流二极管：

- D4 阴极 K 接 `VLOAD_EXT1`。
- D4 阳极 A 接 `MOS_OUT1`。

测试点：

- `TP_GATE1` 接 `GATE1`。
- `TP_OUT1` 接 `MOS_OUT1`。

通道 2：

```text
STM32 PB1 / MOS_CTRL2
-> R16 100Ω 栅极串联电阻
-> GATE2
-> Q2 AO3400A Gate

GATE2
-> R17 100kΩ
-> GND
```

Q2 AO3400A：

- Gate 接 `GATE2`。
- Source 接 `GND`。
- Drain 接 `MOS_OUT2`。

H4 作为第二路外部输出接口：

- `H4-1` 接 `VLOAD_EXT2`。
- `H4-2` 接 `MOS_OUT2`。
- `H4-3` 接 `GND`。

D5 使用 `SS14` 作为续流二极管：

- D5 阴极 K 接 `VLOAD_EXT2`。
- D5 阳极 A 接 `MOS_OUT2`。

测试点：

- `TP_GATE2` 接 `GATE2`。
- `TP_OUT2` 接 `MOS_OUT2`。

### 栅极电阻和下拉电阻

每路 Gate 前串联 `100Ω` 电阻：

- 限制 GPIO 对 MOSFET 栅极电容的瞬态充放电电流。
- 减小开关沿过快造成的振铃和 EMI 风险。
- 对本项目低频开关 / 低速 PWM 场景足够。

每路 Gate 对 GND 下拉 `100kΩ`：

- 保证 MCU 上电复位、下载调试或 GPIO 高阻期间 MOSFET 默认关断。
- 防止 Gate 悬空导致 MOSFET 误导通。
- 不会明显增加 GPIO 驱动负担。

### 外部负载接法

以第一路 H3 为例：

- 外部电源正极 `+5V / +12V` 接 `H3-1 VLOAD_EXT1`。
- 负载一端接 `H3-1 VLOAD_EXT1`。
- 负载另一端接 `H3-2 MOS_OUT1`。
- 外部电源负极接 `H3-3 GND`。

即负载接在 `H3-1` 和 `H3-2` 之间，外部电源接在 `H3-1` 和 `H3-3` 之间。

MOSFET 导通时电流路径为：

```text
外部电源正极
-> H3-1 / VLOAD_EXT1
-> 外部负载
-> H3-2 / MOS_OUT1
-> Q1 AO3400A
-> GND
-> 外部电源负极
```

因此该模块是低边开关，控制的是“负载负端是否接地”。

第二路 H4 同理：

- `H4-1`：`VLOAD_EXT2`。
- `H4-2`：`MOS_OUT2`。
- `H4-3`：`GND`。

### 续流二极管设计说明

`D4 / D5` 使用 `SS14`，作为感性负载的续流保护器件。

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

### 接口丝印建议

H3 丝印建议：

- `VLOAD1 5-12V`
- `OUT1`
- `GND`

H4 丝印建议：

- `VLOAD2 5-12V`
- `OUT2`
- `GND`

模块附近建议增加总说明丝印或文档说明：

- `VLOAD 5-12V ONLY`
- `COMMON GND REQUIRED`
- `OUTx is low-side switched output`
- `Inductive load requires flyback diode`

### 测试点设计

本模块预留 4 个关键测试点：

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

### 风险与后续检查项

原理图审查和 PCB Layout 前重点检查：

1. AO3400A 引脚映射是否正确：Gate 接 GATE，Source 接 GND，Drain 接 MOS_OUT。
2. `D4 / D5` SS14 极性是否正确：阴极 K 接 `VLOAD_EXT`，阳极 A 接 `MOS_OUT`。
3. `H3 / H4` 引脚定义是否清晰：Pin1 = `VLOAD_EXT`，Pin2 = `MOS_OUT`，Pin3 = `GND`。
4. 外部电源必须与板子 GND 共地：`H3/H4` 的 GND 必须与系统 GND 相连，文档和丝印需要提醒 `COMMON GND`。
5. 电流边界：推荐 `<=300mA`，设计预留 `<=500mA`，不作为大电流输出使用。
6. 负载类型：电阻性负载、LED 模块等风险较低；继电器、电机、电磁阀等感性负载必须使用 `D4/D5` 续流保护；若未来驱动更高能量感性负载，需要重新评估 TVS、栅极保护、走线宽度和热耗散。
7. PCB Layout：MOSFET Source 到 GND 回流路径要短；`MOS_OUT` 走线按负载电流适当加宽；`D4/D5` 靠近接口和 `MOS_OUT / VLOAD` 回路放置；Gate 走线远离 `MOS_OUT` 大电流开关节点；`TP_GATE / TP_OUT` 放在便于探测的位置；`H3/H4` 附近丝印必须清楚，避免用户误接。

## 接口与调试设计说明

第一版接口形式暂定为排针，便于手工连线、示波器/万用表测量和固件调试。

需要保留：

- SWD 下载调试接口
- USB-C 接口
- UART 通信/扩展接口
- I2C 传感器接口
- SPI 扩展接口
- 2 路 ADC 输入排针
- 2 路 MOSFET 输出排针
- 5V / 3.3V / GND 测试点或扩展引脚

`UART / I2C / SPI` 扩展接口第一版均为 `3.3V` 逻辑，不直接兼容 `5V` 逻辑信号。如果外接 5V 模块，需要外部电平转换或重新评估输入保护方案。

测试点优先覆盖 5V、3.3V、GND、NRST、SWDIO、SWCLK、USART TX/RX、USB 转 UART 芯片关键电源、ADC 分压后节点、MOSFET 栅极和 MOSFET 输出端。

## 关键器件初选结论

本阶段只是关键器件候选和 datasheet 初步核对，用于支撑后续原理图前的方案收敛；不生成最终 BOM，不进入完整原理图设计。普通阻容、LED、排针、测试点、普通按键等后置外围器件仍等待模块参数明确后再选。

### 1. MCU

`STM32F103C8T6` 已确定为本项目 MCU。后续继续核对官方 datasheet / reference manual / 硬件设计指南，重点包括 LQFP48 引脚、电源脚与去耦、BOOT、NRST、SWD、USART1、ADC、HSE 和 VDDA/VSSA 处理。

### 2. USB-C

`TYPE-C 16PIN 2MD(073)` 进入 USB-C 供电和 USB2.0 数据接口主选。初步核对显示其额定 DC 5V 3A 满足本项目 USB-C 5V 输入需求。

原理图阶段需要正确处理 A4/A9/B4/B9 到 `VBUS_RAW`，A1/A12/B1/B12 到 GND，CC1、CC2 各接 5.1kΩ 下拉到 GND，A6/B6 合并为 `USB_DP`，A7/B7 合并为 `USB_DM`，SBU 暂不使用并标记 NC。Shield 先通过 `R7 0Ω` 接 GND，后续根据 EMI/ESD 测试评估是否改为 DNP、磁珠或其他连接方式。

### 3. USB 转 UART

`CH340C` 进入 USB 转 UART 主选。它支持 USB2.0 全速设备接口，UART 波特率覆盖本项目串口调试需求，并且内置时钟，不需要外部 12MHz 晶振，适合降低第一版复杂度。

本项目要求 CH340C 与 STM32 之间为 3.3V UART 电平，因此 CH340C 按 3.3V 供电方案设计：`Pin16 VCC` 接 `3.3V`，`Pin4 V3` 接 `3.3V`，`Pin1 GND` 接 `GND`。`C13=100nF` 靠近 VCC，`C14=100nF` 靠近 V3，`C15=1uF` 作为 CH340C 局部储能电容。不建议 CH340C 使用 5V 供电后直接连接 STM32 串口，以避免电平风险。

USB 数据线连接为：`USB_DP` 接 CH340C `Pin5 D+ / UD+`，`USB_DM` 接 CH340C `Pin6 D- / UD-`。CH340C datasheet 建议 `UD+ / UD-` 直接连接 USB 总线，因此本项目草图不在 `USB_DP / USB_DM` 上串联 `22Ω` 电阻。USB-C 的 `D+ / D-` 不连接 STM32 `PA11 / PA12`。

UART 连接为：CH340C `Pin2 TXD` 接 STM32 `USART1_RX / PA10`，当前网络名为 `MCU_RX`；CH340C `Pin3 RXD` 接 STM32 `USART1_TX / PA9`，当前网络名为 `MCU_TX`。TX/RX 必须交叉连接，后续可将网络名规范为 `MCU_USART1_RX_PA10`、`MCU_USART1_TX_PA9`，或在文档中说明当前网络名是从 MCU 视角命名。

模式脚和未用脚处理为：`Pin15 R232` 接 `GND`，保持普通 TTL UART 模式，不启用辅助 RS232 模式；`Pin7 NC` 加 No Connect 标记；`Pin8 OUT#`、`Pin9 CTS#`、`Pin10 DSR#`、`Pin11 RI#`、`Pin12 DCD#`、`Pin13 DTR#`、`Pin14 RTS#` 当前均不使用，加 No Connect 标记。第一版不做 `DTR/RTS` 自动下载电路，仍使用 SWD 下载调试和 BOOT0 跳帽。

### 3.1 USB 数据线 ESD

`TPD2EUSB30DRTR-N` 进入 USB 数据线 ESD 保护主选，位号暂定 `D2`。它作为 `USB_DP / USB_DM` 的双路低电容并联钳位保护器件，不是串联器件。

当前草图连接为：`D2 Pin1 / I/O` 接 `USB_DP`，`D2 Pin2 / I/O` 接 `USB_DM`，`D2 Pin3 / GND` 接 `GND`。D2 不接 `3.3V`，也不接 `VBUS / 5V`。当前记录的规格书关键参数包括：`VRWM=5V`，I/O-to-GND 结电容典型 `0.45pF`、最大 `0.6pF`，IEC 61000-4-2 接触放电 `±20kV`、空气放电 `±25kV`。后续需在用户保存本地 datasheet 后复核封装、方向、焊盘和实际丝印。

PCB Layout 时 D2 应靠近 USB-C 接口放置，GND 回流路径要短，优先就近接地铜或地过孔。`USB_DP / USB_DM` 应从 USB-C 先经过 ESD 保护区域，再走向 CH340C；走线尽量短、成对、少过孔，避免穿越分割地或靠近 MOSFET 输出等干扰区域。

### 4. 3.3V 电源

`AP2112K-3.3TRG1` 进入 3.3V LDO 主选。它输出 3.3V，标称输出能力 600mA，推荐 VIN 工作范围为 2.5V~6.0V，适合当前 USB-C 5V 输入转 3.3V。当前草图中 VIN 接 `+5V_SYS`，EN 通过 `R5 10kΩ` 上拉到 `+5V_SYS`，VOUT 输出 `3.3V`；输入/输出各放置 `1µF` 电容，并在 3.3V 总线上放置 `4.7µF` 储能电容。

`HR73L33V` 作为 LDO 备选，不作为当前第一版主选。它的优势是输入耐压高、静态电流低，适合低功耗和宽输入场景；限制是输出电流 300mA，余量小于 AP2112，典型外围电容为 10µF。本项目是 USB 5V 输入的 STM32 开发板，AP2112 更适合作为第一版主选。

电源风险重点是热耗散和总电流预算。5V 转 3.3V 是线性稳压，功耗约为 `P=(5V-3.3V)*Iout`。按 SOT25 θJA 约 `184°C/W` 粗略估算，`Iout=100mA` 时温升约 `31°C`，`Iout=200mA` 时温升约 `63°C`。第一版建议 3.3V 总电流长期控制在约 `150mA~200mA` 以内更稳妥，外部 3.3V 取电仍按 `<=100mA` 限制。

### 5. HSE 晶振

`XC53G2-8.000-F12NJHP` 进入 STM32F103C8T6 的 8MHz HSE 晶振候选。规格书显示该系列为 5.0mm x 3.2mm x 1.3mm 两焊盘贴片无源晶振，频率范围 8MHz-80MHz，8MHz 属于基频范围，8MHz-12MHz 对应 ESR 约 80Ω。

当前资料没有完整型号编码表，暂不能只根据型号中的 F12 直接确认负载电容 `CL=12pF`。负载电容、匹配电容和 STM32 HSE 匹配性仍需结合 STM32 datasheet / reference manual / 硬件设计指南进一步核对。原理图阶段应预留两颗负载电容，晶振靠近 STM32 OSC_IN / OSC_OUT，走线短、对称，远离 USB D+/D-、MOSFET 输出和其它干扰源。

### 6. MOSFET 输出

`AO3400A` 进入 2 路 N-MOSFET 低边输出主选。VDS=30V，满足本项目 VLOAD 5V-12V、最大不超过 12V 的需求。RDS(on) 在 VGS=4.5V 时小于约 32mΩ，在 VGS=2.5V 时小于约 48mΩ，说明适合 STM32 3.3V GPIO 直接驱动的小电流低边开关场景。

本项目推荐使用电流 `<=300mA`，设计预留 `<=500mA`。按 `RDS(on)=48mΩ`、`I=0.5A` 粗略估算，导通损耗约 `0.012W`，SOT-23 封装基本够用。但不能因为 datasheet 中 `ID` 标称较大，就将该模块作为大电流输出模块使用。

当前草图使用 `PB0 / MOS_CTRL1` 控制第一路 Q1 Gate，使用 `PB1 / MOS_CTRL2` 控制第二路 Q2 Gate。每路 Gate 前串联 `100Ω`，并通过 `100kΩ` 下拉到 GND，默认关断。外部接口采用 `VLOAD_EXT / MOS_OUT / GND` 三针形式，负载接在 `VLOAD_EXT` 与 `MOS_OUT` 之间，外部电源必须与板子 GND 共地。

感性负载保护当前使用 `SS14` 作为续流二极管：阴极 K / 色带端接 `VLOAD_EXT`，阳极 A 接 `MOS_OUT`。若驱动继电器、电机、电磁阀等感性负载，必须保留 D4/D5 续流路径；若未来驱动更高能量负载，需要重新评估 TVS、栅极保护、走线宽度和热耗散。

### 7. ADC 输入保护

`BAT54S` 进入 ADC 输入上下轨钳位主选。第一版 2 路 ADC 输入使用 `PA0 / ADC12_IN0` 和 `PA1 / ADC12_IN1`，外部接口范围限定为 `0-5V`，每路先通过 `10kΩ/18kΩ` 分压，将 5V 输入缩放到约 `3.21V`，再经过 `330Ω` 串联限流进入 MCU ADC 节点。ADC 节点对 GND 放置 `10nF` 滤波电容，并用 BAT54S 钳位到 `GND / VDDA_3V3`。

BAT54S 采用 `SOT-23` 封装，用于 circuit protection / voltage clamping。当前草图接法为 `Pin3` 接 ADC 节点，`Pin1` 接 `GND`，`Pin2` 接 `VDDA_3V3`。datasheet 关键参数包括：`VR=30V`，`IF(AV)=200mA`，`VF≤320mV @ IF=1mA`，`VF≤400mV @ IF=10mA`，`CT≤10pF`，`trr≤5ns`，`IR≤2uA @ VR=25V`。

本项目是 `10Hz-1kHz` 低速 ADC 功能验证，BAT54S 漏电和结电容暂可接受。风险重点是：ADC 输入不支持长期过压；上钳位会把异常电流导入 `VDDA_3V3`，板卡未上电时存在外部 ADC 输入反灌 VDDA 的风险；后续若追求高精度或高阻抗采样，需要重新评估 BAT54S 漏电、电容和钳位电流对误差的影响。原理图审查时必须确认器件为 `BAT54S`，不要误选 `BAT54`、`BAT54A` 或 `BAT54C`。

## 后续需核对事项

- STM32F103C8T6 datasheet / reference manual 中的供电、时钟、复位、BOOT、SWD、USART 和 ADC 要求。
- ST 硬件设计指南或 application note 中的最小系统、电源、晶振和 PCB Layout 建议。
- USB-C 取电、CC 电阻、ESD/TVS 和 USB 转 UART 芯片应用资料。
- LDO、TVS/ESD、保险丝、MOSFET、续流二极管、分压电阻和接口保护器件 datasheet。
- PCB 尺寸、安装孔、接口排布、测试点可达性和丝印安全说明。
