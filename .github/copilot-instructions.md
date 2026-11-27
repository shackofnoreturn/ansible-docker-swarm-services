# Copilot Agent Instructions

You are an autonomous development agent operating within this repository.

## Primary Workflow

When asked to work on TODO items, follow this process:

1. Read TODO.md.
2. Locate the first unchecked task (`- [ ]`).
3. Understand the task, acceptance criteria, and any related context.
4. Analyze the codebase before making changes.
5. Determine which files are affected.
6. Create a new feature branch.
7. Implement the requested functionality.
8. Add or update tests.
9. Run relevant validation commands.
10. Commit changes.
11. Present a summary of the work completed.

## Branching Rules

Never work directly on:
- main
- master
- production

Create a new branch using:

```text
agent/<short-task-name>
```

Examples:

```text
agent/add-calculator-api
agent/fix-login-timeout
agent/update-docker-image
```

If a branch already exists for the task, continue using that branch.

## TODO Selection Rules

Always process tasks in order.

Select the first unchecked item:

```markdown
- [ ] Task A
- [ ] Task B
- [ ] Task C
```

Work only on Task A.

Do not begin multiple TODO items in one session unless explicitly instructed.

## Code Quality Requirements

Before making changes:

- Examine existing patterns in the repository.
- Follow existing naming conventions.
- Reuse existing components where possible.
- Avoid introducing duplicate logic.
- Keep changes minimal and focused.

## Testing Requirements

Whenever possible:

- Add new tests.
- Update affected tests.
- Run the relevant test suite.
- Fix any failures introduced by the changes.

Do not ignore failing tests without explanation.

## Commit Requirements

Create a commit after successful validation.

Use commit messages such as:

```text
feat: add calculator API endpoint
fix: resolve login timeout issue
refactor: simplify user validation logic
```

Avoid vague commit messages.

## Safety Rules

Never:

- Delete large parts of the codebase without justification.
- Remove tests simply to make builds succeed.
- Commit secrets, credentials, tokens, certificates, or passwords.
- Modify CI/CD pipelines unless required by the task.
- Push directly to protected branches.

If the requested task is unclear, inspect the codebase and TODO context before making assumptions.

## Completion Checklist

Before finishing:

- Task implemented.
- Tests added or updated.
- Validation completed.
- Changes committed.
- Summary prepared.

The final summary must include:

- TODO item completed.
- Branch name.
- Files modified.
- Tests executed.
- Commit message.
- Any remaining concerns or follow-up work.
