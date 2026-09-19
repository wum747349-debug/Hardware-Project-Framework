# Framework Maintenance and Release Guide

> 职责：Framework Repository 自身的 normal maintenance、Semantic Versioning、candidate validation 与 release publication
>
> 不负责：Standalone Project 是否以及如何采用某个 Framework Release

Project 采用已发布版本时读取 [Framework Migration Guide](Framework_Migration_Guide.md)。若一次变更既发布 breaking Framework version，又要求既有 Project 采用该版本，应分别读取两份 Guide：本 Guide 负责“Framework publishes a version”，Migration Guide 负责“Project decides whether and how to adopt that version”。

## 1. 长期工作模型

Framework `main` 的普通 commit 不自动要求创建 Release；新 RC、Final Release 或 `main` commit 也不自动修改任何 Standalone Project binding。

```text
Framework Maintenance
        ↓
Validate + commit + push
        ↓
Unreleased
        ↓
optional Pinned Project Evaluation
        ↓
Release Assessment
  (Patch / Minor / Major? target version? RC required?)
        ↓
Candidate Validation
        ↓
READY?
        ↓
current task contains explicit Publication authorization?
   no  → report READY and STOP
   yes → Publication
        ↓
Automatic Verification
        ↓
DONE
```

Routine validation、CI、diff inspection、technical review、documentation review、evidence collection 与普通授权范围内的 commit / push 都不建立额外 Human Gate。Candidate Validation 只输出 `READY` 或 `NOT READY`；`READY` 本身不授权 Publication。Read-only publication review 只报告 readiness 并停止；当前用户任务中的 Explicit Publication request 已经构成 Publication Authorization 时，Candidate Validation 通过后不再请求第二次 approval round-trip。

### Framework Evolution / Improvement Tracking

真实 Project 发现先判断是 Project-specific 还是具有 cross-project 价值。Project-specific issue 留在对应 Project；可复用问题进入 Framework improvement assessment，按以下稳定流程处理：

```text
Real Project Finding
    ↓
Project-specific or Cross-project
    ↓
Framework Improvement Issue
    ↓
Architecture Review
    ↓
Implementation → Validation → Commit
    ↓
Release Assessment
    ↓
Optional Publication
```

GitHub Issues 维护尚未完成且值得跟踪的改进需求，不要求每个普通文档修正都先建 Issue；本 Guide 维护稳定流程；Changelog 记录已实施并纳入发布的 release-level changes；Git commit / tag / Release 分别证明实际实现和发布身份。Workspace-Hub 只提供导航，不成为 Framework contract、current state、backlog 或 release identity 的第二权威源。

## 2. Release Assessment

Release Assessment 在一次评估中回答：`Patch / Minor / Major?`、`target version?`、`RC required?`。它合并高层表达，不删除 Change Classification、Semantic Versioning 或 risk assessment 的安全检查。

先按实际 Contract 影响分类，再决定版本号，不能仅凭文件类型判断：

| 版本 | 长期定义 | 典型变化 |
| --- | --- | --- |
| Patch | compatible bugfix / docs / validator / CI fix | 不改变 Runtime / Structural Contract 的错误修复、澄清和兼容工具修复 |
| Minor | backward-compatible Framework capability improvement | 保持既有 Project 兼容的新能力、Guide、Skill、Checklist 或工具增强 |
| Major | breaking Runtime / Structural Contract change | schema、结构职责、Runtime Rules、Stage / Gate、authority 或其他不兼容 Contract 变化 |

若分类证据不足，先判定 `NOT READY` 并停止发布准备。Project Structure Version、Hardware Revision、Git tag / commit 与 Framework Release 是不同身份，不得混用；仅在 Structural Contract 实际变化时调整 Project Structure Version。

## 3. RC 是风险驱动的可选 prerelease

RC 是 `risk-driven optional prerelease`，不是所有 Release 的 mandatory gate。以下情形可考虑 RC：breaking change、影响面大或难以穷尽验证的 capability、需要真实 prerelease evaluation，或发布风险值得冻结 candidate 进行额外反馈。

低风险 compatible Patch、充分覆盖且向后兼容的 Minor 通常可直接进入 Final Candidate。是否需要 RC 必须记录风险理由；不得因为 `main` 有新 commit、文档有变化或旧流程曾使用 RC 就自动要求 RC。

每个新目标版本的 RC 从 `rc1` 重新编号。例如 `v1.3.0-rc1`、`v1.3.0-rc2`；下一个 `v1.4.0` 重新从 `v1.4.0-rc1` 开始。Final 发布后不得继续该版本的 RC：

```text
v1.2.0 published
→ compatible bugfix uses v1.2.1
→ do NOT create v1.2.0-rc3
```

## 4. Immutable Candidate 与 Candidate Validation

RC Candidate 和 Final Candidate 都必须锁定一个 immutable full Commit SHA。Candidate Validation 至少确认：

- target version、candidate SHA、预期 tag / release name 唯一且一致；
- working tree、candidate diff、Contract classification 与 SemVer decision 已核对；
- canonical Framework validation 通过；该入口聚合 Framework contract、Markdown links、Template / snapshot、clean Bootstrap / Gate 1.5、binding / Stage-enabled / migration regressions、Reference Project 与 final-state checks；
- `git diff --check`、Markdown link、CI、release notes 与文档状态一致；
- Runtime / Structural Contract 的变化与声明一致；若声称 compatible，则 Project Structure Version、`FRAMEWORK.md` schema、Project `AGENTS.md` routing、Required / Conditional / Stage-enabled、Stage / Gate、facts authority 与 repository authority 均未发生 breaking change；
- publication plan、automatic verification 与 recovery handling 已确定。

任何 required check 失败、candidate SHA 漂移、版本已存在或 classification 不明确，都输出 `NOT READY` 并 `STOP`。修改 candidate 后必须针对新 SHA 重新验证；不得沿用旧 candidate 的结果。

## 5. Publication Authorization Boundary

Candidate Validation 为 `READY` 后，先检查当前用户任务是否已经明确授权 Publication。

- Read-only publication review，例如“检查能不能发布”“做 Final Publication Review”“判断是否 READY”，只输出 `READY` / `NOT READY`；即使 `READY` 也必须停止，不得创建 tag 或 GitHub Release。
- Explicit Publication request，例如“正式发布 vX.Y.Z”“检查全部通过后直接发布”“执行 Final Publication，失败就停止”，该请求本身已经构成 Publication Authorization。Candidate Validation 通过后不再追加一次独立 Human Publish Approval。
- Publication Authorization 必须明确覆盖 exact target version 与 release type（RC / Final）。Publication 前必须锁定 immutable candidate SHA，并确认它仍位于当前授权任务的 bounded candidate scope；若版本、release type、candidate scope 或用户意图发生实质漂移，必须 `STOP` 并重新取得明确授权。

不存在独立的 RC Gate、Release Readiness Approval、Technical Approval、Documentation Gate、Maintenance Gate 或 Final Closeout Approval。普通 review 与验证结论合并进 Candidate Validation evidence，不拆成额外批准。该模型删除的是重复 approval round-trip，不是用户对 Publication 的控制权，也绝不允许 `Candidate Validation PASS → 自动发布`。

## 6. Atomic Publication

已存在有效 Publication Authorization 后，在一个 bounded publication transaction 中：

1. 再次确认远端默认分支、candidate SHA、目标 tag / Release 不存在且 authorization scope 未漂移；
2. 创建目标 tag 时遵循仓库既定命名，并确保 tag 指向该 immutable candidate SHA；
3. 推送 tag；
4. 发布对应 GitHub prerelease（RC）或 final Release；
5. 不执行 Project rebinding、Repository Rename、Authority Cutover 或其他未包含动作。

这里的 atomic 表示一个有顺序、有边界并有恢复方案的 logical transaction，不声称 Git 与 GitHub Release API 之间存在 ACID transaction。

## 7. Automatic Post-Publish Verification

Publication 后自动核对：

- remote tag 存在且精确指向获授权的 candidate SHA；
- GitHub Release 存在，RC / Final 属性、版本名、target 与 release notes 正确；
- 默认分支及关联 GitHub Actions 状态符合发布要求；
- 未创建额外 tag / Release，未修改任何 Standalone Project binding；
- Changelog 与导航不存在把已发布版本描述为“尚未发布”的 current-state wording。

全部通过后状态为 `DONE`。Automatic Verification 是执行后的检查，不是第二次 Human Approval。

## 8. Failure / STOP / Recovery

出现 validation failure、non-fast-forward、认证或权限异常、tag 冲突、Release metadata 错误、远端 SHA 不匹配、partial publication 或 verification failure 时立即 `STOP`，不得宣告 `DONE`，也不得用 force push、移动既有 tag、history rewrite 或删除同名资源来掩盖问题。

报告已经成功和失败的步骤、远端真实状态、影响范围与安全恢复选项。任何会删除、移动或重建已发布 tag / Release 的恢复动作都需要新的明确授权。修复后若 candidate 内容或 SHA 改变，重新执行 Candidate Validation；若 Final 已成功发布，后续修复使用新的 SemVer 版本。

## 9. Project Binding 边界

```text
Framework main
!=
Project bound Framework
```

Framework 发布只提供一个 immutable adoption target，不代表任何 Project 已采用它。Existing Project 的兼容升级使用 Compatible Framework Sync；breaking Contract 的采用使用 Framework Contract Migration。Authority Cutover 只用于 Legacy / previous authority 到 Standalone Project Repository 的事实源切换，不用于普通 Framework version upgrade。具体流程见 [Framework Migration Guide](Framework_Migration_Guide.md)。
