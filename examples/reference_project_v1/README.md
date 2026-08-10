# Framework v1 Synthetic Reference Project

Project Identity: Framework v1 Synthetic Reference Project
Current Project Stage: Bootstrap
Hardware Revision: N/A — synthetic fixture

Fixture Type: Synthetic Framework documentation and regression fixture
Authority Status: Not an Active Project Authority

## 目的（Purpose）

本目录是 lightweight、validator-valid 的 persistent Reference Project，用于演示 Project Structure Contract、human-facing documentation 与 Final-mode regression。它不是真实硬件 Project，不保存任何活动 Project facts，也不形成新的 authority。

## 当前状态（Current Status）

- Framework binding 与初始化状态：[FRAMEWORK.md](FRAMEWORK.md)
- 只实现 Bootstrap Required structure；未进入任何真实 Hardware Stage。
- 不包含 Project 1 / 2 / 3 facts、真实 EDA、Manufacturing output 或 Hardware Evidence。
- Validator PASS 只证明结构与可自动检查规则一致，不证明硬件设计或测试结果。

## Fixture Facts

- [Fixture requirements](requirements.md)
- [Fixture boundary diagram](block_diagram.md)
- [Fixture design notes](design_notes.md)
- [Fixture reference policy](references.md)

## 仓库导航（Repository Navigation）

- [Project Runtime Rules](PROJECT_RULES.md)
- [Stage 文档职责](docs/README.md)
- [Hardware source 与 Evidence 职责](hardware/README.md)
- [本地资料职责](references/README.md)
- [Project Validator snapshot](scripts/validate_project_repository.py)

## 下一步（Next Step）

本 fixture 保持 Bootstrap。它只随 Framework 的显式 compatibility maintenance 更新，不执行 Gate PASS、Authority Cutover 或真实 Hardware Stage advancement。
