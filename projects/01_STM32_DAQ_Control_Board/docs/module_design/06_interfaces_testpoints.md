# 接口、测试点与丝印设计说明

## 1. 模块定位

本模块记录第一版接口形式、测试点覆盖范围、接口电平边界和丝印提醒。具体电源、ADC、MOSFET、CH340C 细节分别见对应模块设计文档。

第一版接口形式暂定为排针，便于手工连线、示波器/万用表测量和固件调试。

## 2. 需要保留的接口

- SWD 下载调试接口。
- USB-C 接口。
- UART2 扩展接口 `H_UART2`。
- I2C1 扩展接口 `H_I2C`。
- SPI1 扩展接口 `H_SPI`。
- 公用电源 + GPIO 扩展接口 `H_EXT_PWR_GPIO`。
- 2 路 ADC 输入排针。
- 2 路 MOSFET 输出排针。
- 5V / 3.3V / GND 测试点或扩展引脚。

## 3. 电平边界

- `UART / I2C / SPI` 扩展接口第一版均为 `3.3V` 逻辑。
- 不直接兼容 `5V` 逻辑信号。
- 如果外接 5V 模块，需要外部电平转换或重新评估输入保护方案。
- 3.3V 电源排针可给外部低功耗模块供电，外供电流限制为 `<=100mA`。
- `+5V_SYS` 来自 USB-C 输入经过保护/开关后的系统 5V。接到扩展排针时更适合作为 5V 输出取电点，不建议作为外部反灌供电入口；若未来确需外部供电输入，需要重新核对 USB 输入保护、保险丝、电源开关、反灌路径和走线宽度。

## 4. SWD 接口

SWD 接口建议保留 `1x5`：

| 引脚 | 网络 |
|---|---|
| 1 | `3.3V` |
| 2 | `SWDIO` |
| 3 | `SWCLK` |
| 4 | `NRST` |
| 5 | `GND` |

注意：

- `SWDIO` 使用 `PA13`。
- `SWCLK` 使用 `PA14`。
- 网络名统一使用 `SWDIO`、`SWCLK`、`NRST`，避免使用容易混淆的 `CLK`。
- SWD 附近建议保留清晰方向丝印，避免接反。

## 5. UART2 / I2C1 / SPI1 扩展接口

扩展接口第一版只声明 `3.3V` 逻辑边界，不直接兼容 5V 模块。

### 5.1 I2C 扩展接口 `H_I2C`

采用 `I2C1`：

| 接口引脚 | 网络 / 功能 |
|---|---|
| 1 | `3.3V` |
| 2 | `GND` |
| 3 | `PB6 / I2C1_SCL` |
| 4 | `PB7 / I2C1_SDA` |

注意：

- 当前原理图暂时没有给 I2C 预留外部 `4.7k` 上拉电阻。
- 当前版本依赖外接 I2C 模块自带上拉，或后续根据需要再补充上拉电阻。
- 若外接裸 I2C 器件，需要确认 `SCL/SDA` 是否具备合适的 `3.3V` 上拉。
- 后续复审时可考虑是否补 `R_SCL/R_SDA` 预留焊盘。

### 5.2 公用电源 + GPIO 扩展接口 `H_EXT_PWR_GPIO`

采用 `2x5` 排针：

| 引脚 | 网络 | 引脚 | 网络 |
|---|---|---|---|
| 1 | `3.3V` | 2 | `GND` |
| 3 | `3.3V` | 4 | `GND` |
| 5 | `PA8 / GPIO_EXT` | 6 | `PB12 / GPIO_EXT` |
| 7 | `PB13 / GPIO_EXT` | 8 | `PB14 / GPIO_EXT` |
| 9 | `PB15 / GPIO_EXT` | 10 | `+5V_SYS` |

说明：

- 该接口用于提供公用 `3.3V`、`GND` 和少量 GPIO 扩展。
- `+5V_SYS` 来自 USB-C 输入经过保护/开关后的系统 5V，更适合作为 5V 输出取电点，不建议作为外部反灌供电入口。
- `PA8`、`PB12`、`PB13`、`PB14`、`PB15` 作为普通 GPIO 扩展使用。
- GPIO 扩展接口不追求接出全部空闲引脚，优先保证布局简洁、走线合理、功能清晰。

### 5.3 SPI 扩展接口 `H_SPI`

采用 `SPI1`：

| 接口引脚 | 网络 / 功能 |
|---|---|
| 1 | `GND` |
| 2 | `PA4 / SPI1_CS` |
| 3 | `PA5 / SPI1_SCK` |
| 4 | `PA6 / SPI1_MISO` |
| 5 | `PA7 / SPI1_MOSI` |

说明：

- SPI 接口当前只带 `GND` 和信号。
- 外设如需 `3.3V`，可从 `H_EXT_PWR_GPIO` 取电。
- 后续 PCB 丝印建议标注 `GND / CS / SCK / MISO / MOSI`。

### 5.4 UART2 扩展接口 `H_UART2`

外部 UART 不再复用 `PA9/PA10`，改用 `USART2`：

| 接口引脚 | 网络 / 功能 |
|---|---|
| 1 | `GND` |
| 2 | `PA2 / TX2` |
| 3 | `PA3 / RX2` |

说明：

- `TX2` 是 MCU 发送，接外部模块 `RX`。
- `RX2` 是 MCU 接收，接外部模块 `TX`。
- `PA9/PA10` 保持作为板载 CH340C 的 `USART1` USB-UART，不再接外部 UART 扩展排针，避免外部模块和 CH340C 同时驱动导致冲突。

建议在原理图审查时确认：

- UART TX/RX 方向是否从 MCU 视角标注清楚。
- I2C 外接模块是否已有 `3.3V` 上拉；若外接裸 I2C 器件，是否需要补 `R_SCL/R_SDA`。
- SPI 信号是否避开 SWD、ADC 和关键启动脚冲突。
- 排针附近丝印是否标注 `3V3` 或 `3.3V LOGIC`。

## 6. LED 和按键

第一版至少包含：

- 1 个电源指示 LED。
- 1 个用户 LED。
- 1 个复位按键。
- 1 个用户按键。

注意：

- 电源指示 LED 当前在 AP2112 输出侧：`3.3V -> R6 1kΩ -> LED1 -> GND`。
- 复位按键接 `NRST` 到 `GND`，并配合 `100nF` 电容。
- 用户 LED 分配到 `PB5`，推荐电路为 `PB5 -> 限流电阻 1kΩ -> LED_USER -> GND`，高电平点亮，用于基础 GPIO 输出测试、程序运行状态指示和固件调试。
- 用户按键分配到 `PB8`，推荐电路为 `PB8 -> KEY_USER -> GND`。固件中将 `PB8` 配置为内部上拉输入，未按下为高电平，按下为低电平；当前不额外增加外部上拉电阻。

## 7. 当前 MCU 引脚分配

| 引脚 | 功能 / 网络 | 说明 |
|---|---|---|
| `PA0` | `ADC1` 输入 | 第一路 ADC 输入 |
| `PA1` | `ADC2` 输入 | 第二路 ADC 输入 |
| `PA2` | `UART2_TX` | 外部 UART2，MCU 发送，接模块 RX |
| `PA3` | `UART2_RX` | 外部 UART2，MCU 接收，接模块 TX |
| `PA4` | `SPI1_CS` | SPI1 片选 / NSS |
| `PA5` | `SPI1_SCK` | SPI1 时钟 |
| `PA6` | `SPI1_MISO` | SPI1 主入从出 |
| `PA7` | `SPI1_MOSI` | SPI1 主出从入 |
| `PA8` | `GPIO_EXT` | 公用 GPIO 扩展 |
| `PA9` | `CH340 / USART1_TX` | 板载 CH340C USB-UART，不接外部 UART 排针 |
| `PA10` | `CH340 / USART1_RX` | 板载 CH340C USB-UART，不接外部 UART 排针 |
| `PA13` | `SWDIO` | SWD 下载调试 |
| `PA14` | `SWCLK` | SWD 下载调试 |
| `PB0` | `MOS_CTRL1` | 第一路 MOSFET 控制 |
| `PB1` | `MOS_CTRL2` | 第二路 MOSFET 控制 |
| `PB5` | `USER_LED` | 用户 LED，高电平点亮 |
| `PB6` | `I2C1_SCL` | I2C1 时钟 |
| `PB7` | `I2C1_SDA` | I2C1 数据 |
| `PB8` | `USER_KEY` | 用户按键，内部上拉输入，按下为低 |
| `PB12` | `GPIO_EXT` | 公用 GPIO 扩展 |
| `PB13` | `GPIO_EXT` | 公用 GPIO 扩展 |
| `PB14` | `GPIO_EXT` | 公用 GPIO 扩展 |
| `PB15` | `GPIO_EXT` | 公用 GPIO 扩展 |

## 8. 测试点覆盖范围

测试点优先覆盖：

- `5V`
- `3.3V`
- `GND`
- `NRST`
- `SWDIO`
- `SWCLK`
- USART1 TX/RX、USART2 TX/RX
- USB 转 UART 芯片关键电源
- ADC 分压后输入节点
- MOSFET 栅极
- MOSFET 输出端

当前已明确的测试点建议：

| 测试点 | 网络 | 用途 |
|---|---|---|
| `TP_VBUS` | `VBUS_RAW` | 测 USB-C 原始输入 5V |
| `TP_5V` | `+5V_SYS` | 测开关后系统 5V |
| `TP_3V3` | `3.3V` | 测 AP2112 输出 3.3V |
| `TP_GND` | `GND` | 万用表黑表笔或示波器地夹参考点 |
| `TP_ADC1` | `ADC12_IN0` | 测第一路 MCU 实际 ADC 输入节点 |
| `TP_ADC2` | `ADC12_IN1` | 测第二路 MCU 实际 ADC 输入节点 |
| `TP_GATE1` | `GATE1` | 测第一路 MOSFET 栅极驱动电压 |
| `TP_OUT1` | `MOS_OUT1` | 测第一路低边输出节点 |
| `TP_GATE2` | `GATE2` | 测第二路 MOSFET 栅极驱动电压 |
| `TP_OUT2` | `MOS_OUT2` | 测第二路低边输出节点 |

## 9. 丝印提醒

建议后续 PCB 丝印或接口附近文档说明保留以下边界：

- USB-C 接口附近：`USB-C 5V ONLY`。
- ADC 输入接口附近：`ADC IN 0-5V`。
- MOSFET 输出接口附近：`VLOAD 5-12V ONLY`、`COMMON GND REQUIRED`。
- UART/I2C/SPI 接口附近：`3.3V LOGIC`。
- `H_UART2`：`GND / TX2 / RX2`，并在文档中说明 TX2/RX2 为 MCU 视角。
- `H_SPI`：`GND / CS / SCK / MISO / MOSI`。
- `H_I2C`：`3V3 / GND / SCL / SDA`。
- `H_EXT_PWR_GPIO`：明确 `3V3`、`GND`、`+5V_SYS` 和 GPIO 引脚名。
- MOSFET H3/H4 排针：`VLOADx 5-12V`、`OUTx`、`GND`。

丝印应避免过密导致不可读；如果 PCB 空间不足，优先保证接口引脚名、极性、电压边界和 GND 标识清楚。

## 10. 后续审查项

- SWD、UART、I2C、SPI、ADC、MOSFET 排针脚位定义是否与原理图网络一致。
- 电源、GND、信号脚在排针上的顺序是否便于接线和调试。
- `H_EXT_PWR_GPIO` 的 `+5V_SYS` 是否仅作为 5V 输出取电点标注，是否避免被误认为外部供电输入。
- `H_UART2` 是否使用 `PA2/PA3`，且 `PA9/PA10` 未被外部 UART 排针复用。
- `H_I2C` 当前无板载上拉是否已记录为待复审事项；是否需要补 `R_SCL/R_SDA` 预留焊盘。
- `PB5 USER_LED` 是否为高电平点亮，`PB8 USER_KEY` 是否按内部上拉、按下为低的固件约定设计。
- 所有 3.3V 逻辑接口是否避免被误认为 5V 兼容。
- 测试点是否靠近被测节点，同时不影响关键走线和可制造性。
- 丝印是否准确反映 `USB-C 5V ONLY`、`ADC IN 0-5V`、`VLOAD 5-12V`、`COMMON GND` 等安全边界。
