# Docker Stack Remove

*An Ansible role that removes a Docker Swarm stack from the active manager and optionally cleans up stack resources and runtime data.*

---

## What

1. **Validates Inputs:** Requires a non-empty `stack_name` and a configured `docker_active_manager`.
2. **Removes the Stack:** Calls `community.docker.docker_stack` with `state: absent` on the active manager.
3. **Waits for Service Removal:** Checks Swarm until no services remain with the stack namespace label.
4. **Optional Resource Cleanup:** Removes explicitly listed Docker configs and secrets only when their corresponding cleanup flags are enabled.
5. **Optional Runtime Cleanup:** Deletes the stack runtime data directory only when `remove_runtime_data` is enabled.

## Inputs

This role is designed to run against target Docker nodes (e.g., `hosts: docker_online`).

### Variables (`defaults/main.yml`)

| Variable | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `stack_name` | string | `""` | Required name of the Docker stack to remove. |
| `docker_active_manager` | string | Required | Inventory host for the active Swarm manager. |
| `remove_configs` | boolean | `false` | Remove configs listed in `docker_configs_to_remove`. |
| `docker_configs_to_remove` | list | `[]` | Exact Docker config names to remove after the stack. |
| `remove_secrets` | boolean | `false` | Remove secrets listed in `docker_secrets_to_remove`. |
| `docker_secrets_to_remove` | list | `[]` | Exact Docker secret names to remove after the stack. |
| `stack_remove_retries` | integer | `30` | Number of checks while waiting for stack services to disappear. |
| `stack_remove_delay` | integer | `2` | Seconds between service-removal checks. |
| `remove_runtime_data` | boolean | `false` | Delete `{{ docker_data_root }}/{{ stack_name }}` after the stack is removed. |
| `docker_root` | string | `"/opt/docker"` | Root path used to derive `docker_data_root`. |
| `environment` | string | `""` | Environment directory below `docker_root/data`. |
| `docker_data_root` | string | `"{{ docker_root }}/data/{{ env }}"` | Root directory for runtime data; can be overridden. |

### Safety Notes

- Config and secret cleanup is disabled by default. Only exact names provided in the corresponding list are considered.
- Runtime data is retained by default. Enabling `remove_runtime_data` permanently deletes the stack's data directory.
- Configs or secrets still used by another stack may fail to remove; only list resources dedicated to this stack.

## Outputs

1. **Removed Stack:** The named Docker Swarm stack is absent from the active manager.
2. **Service Cleanup Confirmed:** The role proceeds only after Swarm reports no services for the stack.
3. **Optional Resource Cleanup:** Selected configs, secrets, or runtime data are removed when explicitly enabled.

## Examples

```yaml
---
- name: Remove Docker Stack
  hosts: docker_online
  become: true
  gather_facts: false
  vars:
    stack_name: traefik
    docker_active_manager: swarm-manager

  roles:
    - docker-stack-remove
```

### Enabling Cleanup Example

```yaml
- name: Remove Stack and Dedicated Resources
  hosts: docker_online
  become: true
  gather_facts: false
  vars:
    stack_name: traefik
    docker_active_manager: swarm-manager
    remove_configs: true
    docker_configs_to_remove:
      - traefik_traefik.yml
    remove_secrets: true
    docker_secrets_to_remove:
      - cloudflare_api_token
      - traefik_dashboard_users
    remove_runtime_data: true
    environment: development

  roles:
    - docker-stack-remove
```