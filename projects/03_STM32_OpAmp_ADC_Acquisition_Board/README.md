# STM32 + 运放 + ADC 模拟信号采集板

Migration Status: Frozen Migration Source

Active Authority: wum747349-debug/STM32-OpAmp-ADC-Acquisition-Board

本 Legacy 目录只用于历史迁移追溯。不得继续在这里维护 Project facts、EDA、manufacturing evidence、bring-up、test records 或 Hardware Stage progression。所有新的活动 Project 工作只能发生在 Standalone Repository。

## 项目目标

设计一块基于 STM32、运放前端和 ADC 的模拟信号采集板，用于训练模拟前端、滤波、参考电压、ADC 采样和模拟 PCB 布局能力。

## 第一版功能

- STM32 主控
- 运放缓冲 / 放大电路
- RC 低通滤波
- ADC 采样
- 参考电压
- 串口输出采样数据
- 关键测试点

## 设计重点

- 运放供电范围
- 输入共模范围
- 输出摆幅
- ADC 输入范围
- 参考电压稳定性
- 模拟区域 PCB 布局
- 噪声与采样稳定性测试
