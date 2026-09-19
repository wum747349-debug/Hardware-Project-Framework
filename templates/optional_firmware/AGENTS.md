# Firmware Local Rules

## Scope / Inheritance

本文件只适用于本 Project 的 `firmware/**`，并继承 Project 根 `AGENTS.md`、`FRAMEWORK.md` 与 `PROJECT_RULES.md`。Project 根 `AGENTS.md` 仍是启动入口；本文件不改变其七步路由，不建立第二套 Framework binding、Runtime Contract、Stage / Gate、Authority、Release 或 Migration 规则。

复制本模板前，Project 应已确认需要持续性 Firmware 开发。复制后按本项目事实删改示例性提示；已有 `firmware/AGENTS.md` 时不得用本模板覆盖。

## Bound Framework Firmware Method

完成根启动路由后，从 `FRAMEWORK.md` 绑定的 immutable Framework snapshot 读取：

```text
skills/hardware-firmware-development/SKILL.md
```

不要读取或依赖 Framework `main`。当前 Firmware 任务的最小路由为：Project root rules → 本 local rules → bound Firmware Skill → relevant Project hardware facts → Firmware implementation / evidence。

## Project Technology Route

以下内容由本 Project 维护；没有确认的事实保留 `TBD`，不得从模板猜测：

- Target MCU / device / memory model：TBD
- Driver route（HAL / LL / register-level / other）：TBD
- Scheduler（bare-metal / RTOS / other）：TBD
- Toolchain / IDE / compiler / linker：TBD
- Official SDK / device support / middleware sources and versions：TBD
- Reproducible build entry：TBD
- Flash / debug entry：TBD
- Generated-code ownership and regeneration boundary（如适用）：TBD

## Local Directory Responsibilities

按实际工程填写当前目录与依赖方向。可使用 Core / BSP / App / SYSTEM / Platform / Middleware 等名称，也可映射到现有等价结构；不要求创建全部目录。

- Entry / initialization owner：TBD
- Board-level hardware access and safety control owner：TBD
- Application / state / data owner：TBD
- Optional shared platform / middleware owner：TBD
- Build projects, scripts and generated outputs：TBD

## Hardware Facts Reference

列出本 Firmware 实现所依赖的 Project owning records 或 authoritative hardware evidence，不在此复制第二份竞争权威：

- MCU、pin / alternate function、clock 与 memory：TBD
- Power-up、reset、GPIO safe state 与 fault boundary：TBD
- Peripheral mapping、timing、data rate 与 protocol：TBD
- Hardware revision / schematic / interface evidence：TBD

若 Firmware prototype 或测试否定上述假设，保留证据并反馈对应 owning record；不得只在代码中静默改变硬件接口。

## Project-specific Constraints

只记录本项目特有且长期适用的规则，例如 ISR latency / priority、buffer ownership、memory budget、coding / generated-code boundary、safety action、protocol compatibility、fault recovery 或 prohibited dependency。不要复制完整 Framework Skill，也不要把未采用的 DMA、queue、RTOS 或 dynamic-memory policy 写成强制规则。

- Constraint / rationale / owner：TBD

## Build / Validation Entry

分别维护并报告实际证据：

- Source / static review：TBD
- Build / linker / map：TBD
- Flash / verify：Pending
- Runtime / debugger / trace：Pending
- Hardware interface / functional / performance validation：Pending

Build PASS 不等于 Flash、Runtime 或 Hardware Validation。每项实际结果应关联 Firmware identity、Hardware Revision、toolchain / configuration、test condition 与 limitation；未执行项保持 `Pending`。
