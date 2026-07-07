# 系统框图

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
   │      ├─ 用户 LED
   │      ├─ 用户按键
   │      ├─ UART 排针，3.3V 逻辑
   │      ├─ I2C 传感器接口排针，3.3V 逻辑
   │      ├─ SPI 扩展接口排针，3.3V 逻辑
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
约 70mm x 50mm，可预留 2-4 个安装孔，后续随布局微调。

注意：
- USB-C D+ / D- 只接 USB 转 UART 芯片，不接 STM32 PA11 / PA12。
- ADC 外部接口可接 0-5V，但进入 STM32 ADC 引脚前必须限制在 0-3.3V。
- ADC 第一版用于每通道 10Hz-1kHz 级别低速采集和功能验证。
- UART / I2C / SPI 扩展接口均为 3.3V 逻辑，不直接兼容 5V 逻辑。
- MOSFET 外部负载电源 VLOAD 建议 5V-12V，最大不超过 12V，且必须与板子 GND 共地。
```
