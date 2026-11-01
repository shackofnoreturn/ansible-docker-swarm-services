# Docker Stack Validate

*A pre-flight validation role that parses global and stack manifests, merges multi-tier environment variables, and validates Docker Compose configurations prior to Swarm deployment.*

---

## What

Deploying unvalidated compose files or stacks with missing/unset environment variables to Docker Swarm can lead to broken services or runtime failures.

This role acts as a pre-flight validation gate on target nodes prior to deployment:

1. **Manifest Parsing:** Ingests and decodes both the global manifest (`global.yml`) and the stack-specific manifest (`stack.yml`).
2. **Environment Variable Merging:** Compiles the runtime environment (`stack_environment`) across a three-tier hierarchy:
   - Global defaults (`global_definition.environment`)
   - Stack-specific definitions (`stack_definition.environment`)
   - Inventory/group-level overrides (`docker_stack_environment`)
3. **Compose File Discovery & Path Resolution:** Determines Compose files defined in `stack.yml` (`compose_file` or `compose_files`), merges optional inventory overrides (`docker_stack_compose_overrides`), and constructs absolute file paths.
4. **Pre-flight Assertion & Syntax Validation:**
   - Verifies that all referenced compose files exist on the host filesystem.
   - Executes `docker compose config` against the assembled environment to guarantee structural validity and catch any unset environment variables before deployment.

---

## Inputs

This role is designed to run against target Docker nodes (e.g., `hosts: docker_online`).

### Role Variables (`defaults/main.yml`)

| Variable | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `stack_name` | string | `""` | Name of the stack to validate (required). |
| `docker_root` | string | `"/opt/docker"` | Base directory where the stack repository and `global.yml` reside. |
| `stack_path` | string | `"{{ docker_stacks_root }}/{{ stack_name }}"` | Absolute path to the stack directory containing `stack.yml` and compose files. |

### Inventory / Group Variables

These variables are typically provided via inventory `group_vars` (e.g., `group_vars/docker.yml`):

| Variable | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `docker_stacks_root` | string | *None* | Root path for the environment's stacks (e.g., `/opt/docker/stacks/development`). |
| `docker_stack_environment` | dictionary | `{}` | Inventory-level environment key-value pairs merged with highest precedence. |
| `docker_stack_compose_overrides` | dictionary | `{}` | Mapping of stack names to lists of additional compose files to include. |

---

## Outputs

1. **Validated Compose Configuration:**
   Guarantees that compose definitions and syntax are structurally valid and that all required environment variables are populated.
2. **Exposed Facts (for Downstream Roles):**
   Sets facts available for downstream roles (such as `docker-stack-deploy`):
   - `stack_environment`: Combined dictionary of global, stack, and inventory environment variables.
   - `stack_compose_files`: List of resolved compose filenames.
   - `stack_compose_paths`: List of absolute paths to all compose files.
   - `global_definition`: Parsed data structure from `global.yml`.
   - `stack_definition`: Parsed data structure from `stack.yml` (e.g., `runtime_directories`).

---

## Examples

```yaml
---
- name: Validate Docker Stack Configuration
  hosts: docker_online
  become: true
  gather_facts: false

  roles:
    - role: docker-stack-validate
      vars:
        stack_name: "traefik"
```

### Full Deployment Workflow Example

```yaml
---
# Step 1: Filter online hosts
- name: Gather Reachable Nodes
  hosts: localhost
  gather_facts: false

  roles:
    - gather-reachable-hosts

# Step 2: Sync, Validate, and Deploy
- name: Deploy Docker Stack
  hosts: docker_online
  become: true
  gather_facts: false

  roles:
    - docker-stack-sync
    - role: docker-stack-validate
      vars:
        stack_name: "traefik"
    - role: docker-stack-deploy
      vars:
        stack_name: "traefik"
```

