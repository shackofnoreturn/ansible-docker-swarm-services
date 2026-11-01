# Docker Stack Sync

*An Ansible role that synchronizes a private Docker stack repository across cluster nodes using a temporary SSH deploy key, ensuring credentials are removed immediately after cloning.*

---

## What

1. **Ensures Prerequisites:** Verifies that `git` is installed and the root target directory (`docker_root`) exists on the host.
2. **Secure Key Delivery:** Reads the deploy key from the controller environment (`docker_stacks_deploy_key`) and writes it to a temporary secured file (`0600`) with `no_log: true` to prevent leaking keys into CI/Semaphore logs.
3. **Repository Synchronization:** Clones or fast-forwards the stacks repository on the `main` branch with `force: true` to guarantee alignment with remote.
4. **Guaranteed Cleanup:** Uses an `always` block to securely delete the temporary deploy key from the host immediately after synchronization, regardless of whether the git step succeeded or failed.

---

## Inputs

This role is designed to run against target Docker nodes (e.g., `hosts: docker_online`).

### Role Variables (`defaults/main.yml`)

| Variable | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `docker_root` | string | `"/opt/docker"` | Target path on the node where the stacks repo is cloned. |
| `docker_stacks_repo` | string | `""` | SSH URL of the stack definitions Git repository. |
| `docker_stacks_deploy_key_path` | string | `"/tmp/docker_services_deploy_key"` | Temporary location on the target node to store the deploy key during sync. |

### Environment Variables / Secrets

| Variable | Source | Description |
| :--- | :--- | :--- |
| `docker_stacks_deploy_key` | Semaphore Environment / Controller Env | Private SSH deploy key for cloning the private stacks repository. |

---

## Outputs

1. **Synchronized Stack Directory (`docker_root`):**
   The target host filesystem has the latest stack definitions ready for deployment.
2. **Clean Credential State:**
   No deploy keys or credentials remain stored on the target nodes (`docker_stacks_deploy_key_path` is removed).

---

## Examples

```yaml
---
- name: Synchronize Stack Repository
  hosts: docker_online
  become: true
  gather_facts: false
  vars:
    ansible_python_interpreter: auto_silent

  roles:
    - docker-stack-sync
```

### Overriding Defaults Example

```yaml
- name: Synchronize to Custom Path
  hosts: docker_online
  become: true
  roles:
    - role: docker-stack-sync
      vars:
        docker_root: "/srv/docker-stacks"
        docker_stacks_repo: "git@github.com:shackofnoreturn/shackhq-docker-stacks.git"
```

