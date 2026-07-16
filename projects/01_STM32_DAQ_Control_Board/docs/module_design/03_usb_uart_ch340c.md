# USB 转 UART / CH340C 设计说明

> 文档状态：当前有效，模块详细依据
> 适用版本：Rev A

## 1. 模块定位

本模块记录 USB-C 数据线、CH340C USB 转 UART、USB 数据线 ESD、UART TX/RX 和未用脚处理。第一版使用 USB-C 供电 + USB 转 UART，不使用 STM32 原生 USB。

## 2. 设计边界

- USB-C D+ / D- 连接 USB 转 UART 芯片。
- USB-C D+ / D- 不连接 STM32 PA11 / PA12。
- STM32 PA11 / PA12 第一版不作为 USB 功能使用。
- USB 转 UART 与 STM32 之间使用 3.3V UART 电平。
- 推荐使用 USART1，USB 转 UART TXD 接 PA10，USB 转 UART RXD 接 PA9，注意 TX/RX 交叉。

采用 USB 转 UART，而不是 STM32 原生 USB，原因是降低第一版固件和 USB 硬件调试复杂度，电脑端 COM 串口更适合早期打印日志、调试命令和数据上传。

## 3. CH340C 模块设计方案

当前 USB 转 UART 方案已从候选比较收敛为 `CH340C` 主选，当前位号为 `U7`，封装按 `SOP-16`。CH340C 用于电脑端 COM 串口调试、日志输出、ADC 数据上传和控制命令下发。

CH340C 支持 USB2.0 全速设备接口，UART 波特率覆盖本项目串口调试需求，并且内置时钟，不需要外部 12MHz 晶振，适合降低第一版复杂度。

## 4. CH340C 供电与去耦

- CH340C 按 `3.3V` 供电方案设计。
- `Pin16 VCC` 接 `3.3V`。
- `Pin4 V3` 接 `3.3V`。
- `Pin1 GND` 接 `GND`。
- `C12 = 100nF`，`3.3V -> GND`，靠近 `VCC`。
- `C14 = 100nF`，`3.3V -> GND`，靠近 `V3`。
- `C13 = 1uF`，`3.3V -> GND`，作为 CH340C 局部储能电容。
- 不采用 CH340C 5V 供电后直连 STM32 UART 的方案，以避免 5V/3.3V 电平风险。

## 5. USB 数据线连接

- USB-C 模块引出的 `USB_DP` 接 CH340C `Pin5 D+ / UD+`。
- USB-C 模块引出的 `USB_DM` 接 CH340C `Pin6 D- / UD-`。
- CH340C datasheet 建议 `UD+ / UD-` 直接连接 USB 总线，本项目模块设计不在 `USB_DP / USB_DM` 上串联 `22Ω` 电阻。
- USB-C 的 `D+ / D-` 不连接 STM32 `PA11 / PA12`。

## 6. USB 数据线 ESD 保护

- `U6` 使用 `TPD2EUSB30DRTR-N`，作为 `USB_DP / USB_DM` 的双路低电容 ESD 保护器件。
- `TPD2EUSB30DRTR-N` 当前是 USB 数据线 ESD 主选，本地已有相关资料，但完整型号与实际 datasheet 的一致性仍待 EDA / datasheet 人工核对。
- `U6 Pin1 / I/O` 接 `USB_DP`。
- `U6 Pin2 / I/O` 接 `USB_DM`。
- `U6 Pin3 / GND` 接 `GND`。
- U6 是并联钳位保护器件，不是串联器件。
- 当前记录的规格书关键参数：`VRWM=5V`，I/O-to-GND 结电容典型 `0.45pF`、最大 `0.6pF`，IEC 61000-4-2 接触放电 `±20kV`、空气放电 `±25kV`。
- PCB Layout 时 U6 应靠近 USB-C 接口放置，GND 回流路径要短，优先就近接地铜或地过孔。
- U6 不接 `3.3V`，也不接 `VBUS / 5V`。
- 后续仍需人工核对 U6 原理图针号与 SOT-723 封装焊盘映射，以及 USB-C、CH340C 和其他关键封装方向。

## 7. UART 到 STM32

- CH340C `Pin2 TXD` 接 STM32 `USART1_RX / PA10`，当前网络名为 `MCU_RX`。
- CH340C `Pin3 RXD` 接 STM32 `USART1_TX / PA9`，当前网络名为 `MCU_TX`。
- TX/RX 必须交叉连接。
- 后续可考虑将网络名进一步规范为 `MCU_USART1_RX_PA10`、`MCU_USART1_TX_PA9`，或在文档中说明当前网络名是从 MCU 视角命名。

## 8. 模式脚和未用脚

- CH340C `Pin15 R232` 接 `GND`，用于保持普通 TTL UART 模式，不启用辅助 RS232 模式。
- `Pin7 NC` 加 No Connect 标记。
- `Pin8 OUT#`、`Pin9 CTS#`、`Pin10 DSR#`、`Pin11 RI#`、`Pin12 DCD#`、`Pin13 DTR#`、`Pin14 RTS#` 当前均不使用，加 No Connect 标记。
- 第一版不做 `DTR/RTS` 自动下载电路，仍使用 SWD 下载调试和 BOOT0 跳帽。

## 9. 后续 PCB 检查项

1. `U6 TPD2EUSB30DRTR-N` 是否靠近 USB-C 接口，且先于较长 USB 数据线进入板内区域。
2. `USB_DP / USB_DM` 从 USB-C 到 U6、再到 CH340C 的走线是否短、成对、少过孔，并尽量避免穿越分割地或强干扰区域。
3. U6 的 `GND` 是否就近接地铜或地过孔，回流路径是否短直。
4. CH340C 的 `C12/C14/C13` 是否靠近对应电源引脚，3.3V 与 GND 回路是否紧凑。
5. CH340C `TXD/RXD` 到 STM32 `PA10/PA9` 是否交叉正确，网络名是否明确说明为 MCU 视角。
6. `R232` 是否可靠接地，未用握手脚和 `NC` 脚是否加 No Connect 标记。
7. USB-C `D+ / D-` 是否只接 CH340C，不误接 STM32 `PA11/PA12`。
8. PCB 丝印或调试文档是否明确第一版不支持 STM32 原生 USB，也不支持 DTR/RTS 自动下载。
