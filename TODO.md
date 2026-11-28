# Todo

- [ ] Question of need for playbook per environment/inventory
- [ ] Set up roles in semaphore
- [ ] Test all new backup/restore/move roles



Another error:
TASK [docker-stack-validate : Validate Compose configuration] ******************
9:23:01 AM
[ERROR]: Task failed: Module failed: non-zero return code
9:23:01 AM
Origin: /tmp/semaphore/project_1/repository_12_template_41/roles/docker-stack-validate/tasks/validate.yml:26:3
9:23:01 AM
9:23:01 AM
24
9:23:01 AM
25 # Compose configuration
9:23:01 AM
26 - name: Validate Compose configuration
9:23:01 AM
     ^ column 3
9:23:01 AM
9:23:01 AM
fatal: [shack-app-d001]: FAILED! => {"changed": false, "cmd": ["docker", "compose", "-f", "/opt/docker/stacks/development/traefik/compose.yml", "config", "--format", "json"], "delta": "0:00:01.090407", "end": "2026-11-28 09:23:01.700345", "msg": "non-zero return code", "rc": 1, "start": "2026-11-28 09:23:00.609938", "stderr": "yaml: line 78: mapping values are not allowed in this context", "stderr_lines": ["yaml: line 78: mapping values are not allowed in this context"], "stdout": "", "stdout_lines": []}
9:23:01 AM



Probably because of this role:
---
# Compose files
- name: Compose files configured
  assert:
    that:
      - stack_compose_files | length > 0
    fail_msg: "Stack {{ stack_name }} must define compose_file or compose_files"

- name: Check Compose exist
  stat:
    path: "{{ item }}"
  loop: "{{ stack_compose_paths }}"
  register: compose_files

- name: Validate files exist
  assert:
    that:
      - compose_files.results | selectattr('stat.exists') | list | length == stack_compose_paths | length
    fail_msg:
      >
      One or more Compose files are missing for stack {{ stack_name }}:
      {{ stack_compose_paths }}


# Compose configuration
- name: Validate Compose configuration
  command:
    cmd: >-
      docker compose
      {{ stack_compose_paths | map('regex_replace', '^', '-f ') | join(' ') }}
      config --format json
  environment: "{{ stack_environment }}"
  register: compose_validation
  changed_when: false
  run_once: true

- name: Fail on invalid
  assert:
    that:
      - compose_validation.rc == 0
      - compose_validation.stderr | regex_search('(?i)variable .+ is not set') is none
    fail_msg: >-
      Compose validation failed for stack {{ stack_name }}.
      Return code: {{ compose_validation.rc }}.
      Diagnostics: {{ compose_validation.stderr | default('') }}
  run_once: true
