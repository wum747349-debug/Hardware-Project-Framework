# Requirements Baseline

Status: Draft — synthetic fixture requirements only

## Project Goal

提供一个 lightweight、可重复验证的 Framework v1 Project structure 示例，证明 Required files、binding、navigation 与 human-facing wording 可以脱离真实 Project facts 工作。

## Out of Scope

- 不设计、制造、装配或测试真实硬件。
- 不选择器件，不生成 EDA、BOM、Manufacturing output 或 Hardware Evidence。
- 不复制 Project 1 / 2 / 3 facts，不成为活动 authority。

## Functional Boundary

只覆盖 documentation / regression fixture：Required structure、Framework binding、relative navigation 和 Project Validator execution。

## Module Boundary

Fixture 由 Binding / Runtime entry、Required fact-entry examples、responsibility README 与 Validator snapshot 组成；不存在真实电子模块。

## Power Requirements

Not applicable — synthetic fixture，不声明输入、电源 rail、负载或上电条件。

## Interface Requirements

Not applicable — synthetic fixture，不声明电气或通信接口。

## Safety Boundary

禁止把本 fixture 解释为实际硬件安全依据、EDA implementation 或测试证据。

## Manufacturing Baseline

Not applicable — 不包含板材、层数、装配、板厂或制造参数。

## Acceptance Criteria

| ID | Requirement | Verification Method | Expected Result | Status |
| --- | --- | --- | --- | --- |
| REF-001 | Required structure 与 binding 可验证 | 运行 Project Validator | Validator PASS | Draft |
| REF-002 | Final-mode 可发现并验证 fixture | 运行 Framework Validator `--mode final` | Validator PASS | Draft |
| REF-003 | 不包含真实 Project facts / EDA / Evidence | Repository review | 无此类内容 | Draft |

## Open Questions

| ID | Question | Impact | Owner / Source | Resolution Plan | Status |
| --- | --- | --- | --- | --- | --- |
| REF-OPEN-001 | Repository Rename 后的 identity adjustment | Final Candidate identity | Framework closeout | 在获批 Rename transaction 中显式处理 | Open |
