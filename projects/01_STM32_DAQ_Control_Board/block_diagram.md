# 系统框图

> 文档状态：当前有效
> 适用阶段：阶段 1 至阶段 7
> 适用对象：STM32 DAQ Control Board Rev A 的系统结构与模块边界
> 最后核对依据：当前原理图 PDF、当前 BOM 与已确认设计决定

```text
电脑 USB-C
   │
   │ 5V 输入
   ▼
USB-C 接口
   │
   ├─ D+ / D- ─────► USB 转 UART 芯片 ── TX/RX，3.3V UART ──► STM32F103C8T6 USART1
   │                                                        PA10/RX  PA9/TX
   │
   ▼
电源开关 / 保险丝或自恢复保险丝 / TVS-ESD / 输入滤波
   │
   ▼
3.3V 稳压
   │
   ├─► STM32F103C8T6
   │      ├─ 8MHz HSE 外部晶振
   │      ├─ NRST 复位
   │      ├─ BOOT 配置
   │      ├─ SWD 下载调试接口
   │      ├─ PB5 用户 LED，低电平点亮
   │      ├─ PB8 用户按键，内部上拉，按下为低
   │      ├─ USART2 扩展排针 H_UART2，PA2/TX2、PA3/RX2，3.3V 逻辑
   │      ├─ I2C1 传感器接口排针 H_I2C，PB6/SCL、PB7/SDA，3.3V 逻辑
   │      ├─ SPI1 扩展接口排针 H_SPI，PA4/CS、PA5/SCK、PA6/MISO、PA7/MOSI，3.3V 逻辑
   │      ├─ 公用电源 + GPIO 扩展 H_EXT_PWR_GPIO，3.3V/GND/PA8/PB12-PB15/+5V_SYS
   │      ├─ ADC1 输入  ◄── 分压 / 限流 / RC 滤波 / 保护 ◄── ADC IN1 0-5V + GND
   │      ├─ ADC2 输入  ◄── 分压 / 限流 / RC 滤波 / 保护 ◄── ADC IN2 0-5V + GND
   │      ├─ GPIO ─────► MOSFET 低边输出 CH1 ── OUT1 / VLOAD1 5V-12V / GND
   │      └─ GPIO ─────► MOSFET 低边输出 CH2 ── OUT2 / VLOAD2 5V-12V / GND
   │
   ├─► USB 转 UART 芯片逻辑侧
   ├─► 电源指示 LED
   ├─► 3.3V 电源排针，外部低功耗模块 <=100mA
   └─► 接口上拉 / 低压外围电路

测试点：
5V / 3.3V / GND / NRST / SWDIO / SWCLK / USART TX-RX /
USB 转 UART 关键电源 / ADC 分压后节点 / MOSFET 栅极 / MOSFET 输出端

PCB 目标：
当前板框外接尺寸为 `59.563mm × 60.000mm`（用户在 Altium 中确认），当前 4 个安装孔的孔径、孔位、禁布区和机械间隙仍在阶段 7：PCB 审查阶段跟踪。

注意：
- USB-C D+ / D- 只接 USB 转 UART 芯片，不接 STM32 PA11 / PA12。
- PA9 / PA10 保持作为板载 CH340C 的 USART1，不接外部 UART 扩展排针。
- I2C1 已有 R19/R20 = 4.7kΩ 板载上拉到 3.3V；若外部模块也自带上拉，需检查并联后的等效上拉阻值和低电平灌电流。
- +5V_SYS 从 USB-C 输入经过保护/开关后引出，更适合作为 5V 输出取电点，不建议作为外部反灌供电入口。
- ADC 外部接口可接 0-5V，但进入 STM32 ADC 引脚前必须限制在 0-3.3V。
- ADC 第一版用于每通道 10Hz-1kHz 级别低速采集和功能验证。
- UART / I2C / SPI 扩展接口均为 3.3V 逻辑，不直接兼容 5V 逻辑。
- MOSFET 外部负载电源 VLOAD 建议 5V-12V，最大不超过 12V，且必须与板子 GND 共地。
```
