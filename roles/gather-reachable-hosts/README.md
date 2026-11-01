# Gather Reachable Hosts

*A lightweight pre-flight role that checks host connectivity from the control node and dynamically groups only reachable hosts, preventing Ansible and CI tools (like Semaphore) from failing on offline nodes.*

---

## What

In clusters where nodes can dynamically go offline (e.g. Docker Swarm), targeting offline hosts directly causes Ansible SSH connection timeouts and marks them as `UNREACHABLE`, resulting in an exit code `4` and failed CI jobs.

This role runs locally on the control node (`localhost`) and performs a rapid TCP socket check (port 22) against target nodes. Only responsive hosts are added to a new in-memory group, allowing all subsequent plays to run cleanly with zero unreachable failures.

---

## Inputs

This role is designed to run against **`hosts: localhost`**

### Variables (`defaults/main.yml`)

| Variable | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `target_group` | string | `"docker"` | Inventory group name to test. |
| `online_group` | string | `"docker_online"` | Name of the dynamic in-memory group to create. |
| `reachability_port` | integer | `22` | Port to test connectivity against (SSH). |
| `reachability_timeout` | integer | `3` | Socket connection timeout in seconds per host. |
| `fail_if_none_reachable` | boolean | `true` | Abort playbook if 0 hosts in `target_group` are reachable. |
| `fail_message` | string | `"..."` | Custom error message when no hosts respond. |

---

## Outputs

1. **Dynamic Host Group (`docker_online`):**
   An in-memory host group containing only responsive hosts, ready to be targeted by subsequent plays:
   ```yaml
   hosts: docker_online
   ```
2. **Clean Execution Recap:**
   Because probe failures occur locally on `localhost` without attempting an SSH session, offline nodes are never marked as `UNREACHABLE` in Ansible's summary recap, ensuring the playbook finishes with exit code `0`.

---

## Examples

```yaml
---
# Step 1: Filter online hosts
- name: Gather Reachable Nodes
  hosts: localhost
  gather_facts: false

  roles:
    - gather-reachable-hosts

# Step 2: Run workload on online hosts only
- name: Synchronize or Deploy Workloads
  hosts: docker_online
  become: true

  roles:
    - docker-stack-sync
```

### Custom Group Example

```yaml
- name: Gather Reachable Swarm Managers
  hosts: localhost
  gather_facts: false

  roles:
    - role: gather-reachable-hosts
      vars:
        target_group: "managers"
        online_group: "managers_online"
        reachability_timeout: 2
```

