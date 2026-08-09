# Framework User Guide

> Audience: Human User
>
> Runtime Contract: No
>
> Purpose: Explanatory / Navigation Guide

This guide lowers the entry barrier by explaining and linking to existing authority. It does not create a Framework Contract, Project Runtime Rule, Stage Rule, or Human Approval Rule.

## 1. What is Framework?

Hardware Project Framework provides reusable engineering methods, repository structure rules, templates, validators, and AI context guidance for hardware projects.

Framework Repository defines:

- project methods and contracts;
- templates and validation tools;
- workflow and stage guidance.

A Standalone Project Repository stores the actual project facts:

- requirements;
- design decisions;
- EDA source files;
- evidence and test records;
- project history.

Framework is not the active fact source for a real project.

## 2. Framework Repository vs Project Repository

```text
Framework Repository
Contract → Template → Validator → Guide

Standalone Project Repository
Binding → Runtime Rules → Project Facts → Evidence
```

A project uses a fixed Framework Release and immutable Commit recorded in `FRAMEWORK.md`. It does not automatically follow Framework `main`.

## 3. Starting a Project

Recommended path:

```text
README
→ Framework User Guide
→ the Contract or Guide required by the current task
```

Typical flow:

1. Create a Standalone Project Repository.
2. Initialize from a fixed Framework Release template.
3. Complete Bootstrap and Stage 1 requirements.
4. Pass Gate 1.5 before Stage 2.

Unknown facts should remain TBD or pending confirmation. Do not create false engineering facts to satisfy structure checks.

Use the [Project Initialization Guide](Project_Initialization_Guide.md) for the operating sequence, the [Project Template Guide](Project_Template_Guide.md) for template boundaries, the [Project Structure Standard](Project_Structure_Standard.md) for structure and binding, and the [Project Workflow](08_Project_Workflow.md) for lifecycle and gates.

## 4. Continuing an Existing Project

For an existing project:

1. Read the project's `README.md` for current stage and facts.
2. Read `FRAMEWORK.md` for current Framework binding.
3. Read project `PROJECT_RULES.md`.
4. Use the required Stage Method from the bound Framework snapshot.

The project repository remains the source of project-specific truth. Follow the bound snapshot's [AI Context Guide](AI_Context_Guide.md) to load only the Project Facts, Stage Method, and evidence needed for the current task; do not default to Framework `main` or another Project.

## 5. AI and Human Responsibilities

Within an authorized task, AI can routinely help with:

- documentation preparation;
- read-only review, evidence organization, and engineering analysis;
- structure, link, validator, and CI checks;
- scoped documentation, validator, and tooling maintenance;
- explicit staging, ordinary commits, and pushes when requested.

These routine actions do not authorize AI to invent Project facts, claim unperformed EDA or physical work, or make a high-impact state change.

Human approval remains required for high-impact state changes:

- hardware Stage advancement;
- Gate 1.5 Human PASS;
- Framework Contract Migration;
- Authority Cutover;
- RC / Final publication;
- Repository Rename;
- destructive cleanup.

Routine documentation, validation, review, and explicitly authorized compatible maintenance do not require repeated approval gates. The authoritative responsibility and approval boundaries are in [Framework Rules](../PROJECT_RULES.md), [Project Workflow](08_Project_Workflow.md), and [Framework Migration Guide](Framework_Migration_Guide.md).

## 6. Framework Updates

Two categories exist:

### Compatible Framework Sync

Used for a fixed target Framework Release + immutable Commit when Runtime and Structural Contract semantics remain unchanged. It still requires an explicit user task and validation, but no separate repeated approval gate.

### Framework Contract Migration

Used when contracts such as schema, structure, lifecycle, Project fact responsibility, authority model, or validator-required structure change. It requires the full impact review, Project adaptation, validation, rollback plan, and Human Approval defined by the authoritative guide.

For the complete classification and process, see the [Framework Migration Guide](Framework_Migration_Guide.md). This summary does not replace it.

## 7. Where to Find Facts

| Question | Source |
| --- | --- |
| Current Framework binding | Project `FRAMEWORK.md` |
| Current project stage | Project `README.md` |
| Current requirements | Project `requirements.md` |
| Project facts and evidence | The current Project's fact files and evidence, routed from its `README.md` |
| Repository structure and fact responsibilities | [Project Structure Standard](Project_Structure_Standard.md) |
| Bootstrap and Gate 1.5 operating steps | [Project Initialization Guide](Project_Initialization_Guide.md) |
| Stage lifecycle | [Project Workflow](08_Project_Workflow.md) |
| AI context routing | [AI Context Guide](AI_Context_Guide.md) |
| Framework update classification and approval | [Framework Migration Guide](Framework_Migration_Guide.md) |

## 8. Recommended Reading by Role

Human User:

- the repository `README.md` and this Framework User Guide;
- the current Project's `README.md`, `FRAMEWORK.md`, requirements, and task-specific facts when continuing a Project;
- the [Project Initialization Guide](Project_Initialization_Guide.md) when creating a Project.

Project Creator:

- this guide;
- the [Project Initialization Guide](Project_Initialization_Guide.md);
- the [Project Structure Standard](Project_Structure_Standard.md);
- the [Project Workflow](08_Project_Workflow.md);
- the [Project Template Guide](Project_Template_Guide.md).

Framework Maintainer:

- [Framework Rules](../PROJECT_RULES.md);
- the [Project Structure Standard](Project_Structure_Standard.md), [Project Workflow](08_Project_Workflow.md), and [AI Context Guide](AI_Context_Guide.md);
- the [Project Template Guide](Project_Template_Guide.md), [Project Initialization Guide](Project_Initialization_Guide.md), and [Framework Migration Guide](Framework_Migration_Guide.md);
- affected validator, skill, checklist, and CI documentation only as required by the task.

## 9. One-time Repository Architecture Migration

Framework maintainers working on the repository-wide transition can use the [Repository Architecture Migration Master Plan](Repository_Architecture_Migration_Master_Plan.md) for the human roadmap and the [Repository Architecture Migration AI Runbook](Repository_Architecture_Migration_AI_Runbook.md) for migration-only execution routing.

These two documents are not Standalone Project Runtime Contract and are not the default reading path for ordinary Project work.
