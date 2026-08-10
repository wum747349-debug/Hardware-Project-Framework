# Block Diagram

Status: Draft — synthetic fixture boundary

## System Boundary

```text
Framework Contract + Template
        ↓
Synthetic Required-file Fixture
        ↓
Project Validator + Final-mode Regression
```

该图描述 documentation / regression flow，不是硬件能量流、信号流或 EDA block diagram。

## Modules

| Module | Responsibility | Inputs | Outputs | Power Domain | Open Risk |
| --- | --- | --- | --- | --- | --- |
| Binding entry | 固定 Framework identity / snapshot | Release + Commit | `FRAMEWORK.md` | N/A | Rename 后需显式 identity adjustment |
| Required docs | 演示职责与中文可读性 | Current Contract | Synthetic fixture content | N/A | 不得演变为真实 Project facts |
| Validator snapshot | 独立结构验证 | Fixture tree | PASS / FAIL | N/A | 必须与 Framework 开发源同步 |

## Cross-module Flows

- Energy flow（能量流）：Not applicable。
- Signal flow（信号流）：Not applicable。
- Control and feedback boundaries：Framework Validator 调用 Project Validator 并报告结构结果。
