# Design Notes

Status: Draft — synthetic fixture decisions

## Board-level Intent

Not applicable。本 fixture 没有 board-level hardware intent；其目的仅是保持一个 minimal、readable、validator-valid 的 Project structure example。

## Current Decisions

| Decision | Current Position | Basis | Status |
| --- | --- | --- | --- |
| Content model | 只保留 Required files | Project Structure Contract | Confirmed for fixture |
| Hardware content | 不创建 EDA、BOM、outputs 或 evidence | Reference Project boundary | Confirmed for fixture |
| Lifecycle | 保持 Bootstrap / Development Bootstrap | 不推进真实 Hardware Stage | Confirmed for fixture |

## Power and Interfaces

Not applicable；本 fixture 不声明任何电源、接口、网络或电气边界。

## Pin and Connection Planning

Not applicable；不创建 Pin Map、Project network name 或器件连接。

## PCB Inputs

- Mechanical constraints：Not applicable。
- Sensitive or high-risk areas：Not applicable。
- Power and thermal constraints：Not applicable。
- Required official layout sources：Not applicable。

## Open Decisions

| ID | Decision Needed | Affected Stage | Resolution Source | Status |
| --- | --- | --- | --- | --- |
| REF-DN-001 | Rename 后 Framework identity 如何更新 | Final Candidate preparation | Approved Repository Rename transaction | Open |
