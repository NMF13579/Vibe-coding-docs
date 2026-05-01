# Task Brief: Brief to Contract Manual Guide

## Metadata

task_id: task-20260426-brief-to-contract-manual-guide
status: APPROVED
created_at: 2026-04-26
source: spec-wizard-smoke-test
executable: false

This file is an approved Task Brief.
It is not an executable Task Contract.
To execute this task, create tasks/active-task.md from tasks/templates/task-contract.md.

## Context

AgentOS already separates task planning from execution. The project has an approved brief format and a separate executable contract format, but a non-technical user still needs a clear manual bridge between these two steps.

## User Story

As a non-technical founder using AI coding agents, I want a clear manual guide for turning an approved Task Brief into an executable Task Contract so that I can start execution without accidental automation or scope drift.

## Expected Result

The project contains clear instructions that explain how to manually go from `tasks/{task-id}/TASK.md` to `tasks/active-task.md` using the existing contract template, without introducing automatic conversion.

## Acceptance Criteria

- AC1: The manual bridge explains that `TASK.md` is not executable.
- AC2: The manual bridge points to `tasks/templates/task-contract.md` as the starting point.
- AC3: The manual bridge explains that `tasks/active-task.md` must be created manually.
- AC4: The manual bridge does not introduce automatic Brief → Contract conversion.

## Out of Scope

- Automatic generation of `tasks/active-task.md`
- Execution pipeline запуск
- Queue, agent-next, agent-complete
- Changes to validators or runtime bootstrap

## Dependencies

- `tasks/templates/task-contract.md`
- Existing Input Layer docs in `INIT.md` and `stages/spec-wizard/BOOT.md`
- Existing execution rules in `workflow/MAIN.md`

## Risks

- User may confuse approved Task Brief with executable Task Contract.
- Too much automation here could break the boundary between Input Layer and Execution Layer.
- Incomplete manual guidance could cause malformed `tasks/active-task.md`.

## Rollback / Reversal Notes

- Remove the manual guidance if it creates confusion or duplicates another canonical document.
- Remove or revise references that incorrectly imply automatic execution.
- Re-check that Input Layer and Execution Layer stay separate after rollback.

## Notes

- This smoke-test brief exists only to verify that Spec Wizard can create an approved Task Brief correctly.
- It is intentionally manual and does not trigger execution.
