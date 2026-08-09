# Framework User Guide

> Audience: Human users of Hardware Project Framework
>
> Runtime Contract: No
>
> Purpose: Explain navigation and usage. This guide does not create new rules.

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

README
→ Framework User Guide
→ Project Initialization Guide
→ Project Structure Standard
→ Workflow

Typical flow:

1. Create a Standalone Project Repository.
2. Initialize from a fixed Framework Release template.
3. Complete Bootstrap and Stage 1 requirements.
4. Pass Gate 1.5 before Stage 2.

Unknown facts should remain TBD or pending confirmation. Do not create false engineering facts to satisfy structure checks.

## 4. Continuing an Existing Project

For an existing project:

1. Read the project's `README.md` for current stage and facts.
2. Read `FRAMEWORK.md` for current Framework binding.
3. Read project `PROJECT_RULES.md`.
4. Use the required Stage Method from the bound Framework snapshot.

The project repository remains the source of project-specific truth.

## 5. AI and Human Responsibilities

AI can help with:

- documentation preparation;
- structure checks;
- impact analysis;
- engineering reasoning.

Human approval remains required for high-impact state changes:

- hardware Stage advancement;
- Framework Contract Migration;
- Authority Cutover;
- RC / Final publication;
- Repository Rename;
- destructive cleanup.

Routine documentation, validation, and authorized compatible maintenance do not require repeated approval gates.

## 6. Framework Updates

Two categories exist:

### Compatible Framework Sync

Used when Runtime and Structural Contract semantics remain unchanged.

### Framework Contract Migration

Used when contracts such as schema, structure, lifecycle, authority model, or validator-required structure change.

For details see `Framework_Migration_Guide.md`.

## 7. Where to Find Facts

| Question | Source |
| --- | --- |
| Current Framework binding | Project `FRAMEWORK.md` |
| Current project stage | Project `README.md` |
| Repository structure rules | `Project_Structure_Standard.md` |
| Stage lifecycle | `08_Project_Workflow.md` |
| AI routing | `AI_Context_Guide.md` |
| Migration process | `Framework_Migration_Guide.md` |

## 8. Recommended Reading by Role

Project User:

- README
- Framework User Guide
- Project Initialization Guide

Project Creator:

- Framework User Guide
- Project Structure Standard
- Workflow
- Template Guide

Framework Maintainer:

- PROJECT_RULES.md
- Contract documents
- Migration Guide
- Validator documentation
