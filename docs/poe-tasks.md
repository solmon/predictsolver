# Using Poe Tasks in PredictSolver

This document explains how Poe tasks are configured in the PredictSolver project.

## Task Types

There are two main ways to define Poe tasks:

1. **`cmd` tasks**: Simple commands that run directly, without shell interpretation.
   ```toml
   task-name = { cmd = "command arg1 arg2" }
   ```

2. **`shell` tasks**: Commands that require shell features like `cd`, environment variables, or `&&` chaining.
   ```toml
   task-name = { shell = "cd dir && command arg1 arg2" }
   ```

## Task Examples

### Python Tasks
```toml
run-sample = { cmd = "python apps/sample_app.py" }
test = { cmd = "pytest" }
```

### NestJS Tasks (requiring directory changes)
```toml
run-dataapi = { shell = "cd apps/dataapi && pnpm run start" }
```

### Combined Tasks
```toml
setup-all = { sequence = ["setup", "install", "install-dev"] }
```

## Troubleshooting

If you see errors like:
```
Error: executable 'cd' could not be found using virtualenv '/path/to/venv'
```

This means you're using `cmd` for a command that requires shell interpretation. Change it to use `shell` instead.

## Reference

For more information about Poe, visit the [official documentation](https://github.com/nat-n/poethepoet).
