# Todo

- [ ] Question of need for playbook per environment/inventory
- [ ] Set up roles in semaphore
- [ ] Test all new backup/restore/move roles
- [ ] Error in semaphore:  
Task Stack Deploy (Development) added to queue
Started task #869 of template 'Stack Deploy (Development)'

Preparing: 869
Updating Repository https://github.com/shackofnoreturn/ansible-docker-swarm-services.git
From https://github.com/shackofnoreturn/ansible-docker-swarm-services
 * branch            main       -> FETCH_HEAD
Already up to date.
Get current commit hash
Get current commit message
cloning inventory repository
Warning: Permanently added 'github.com' (ED25519) to the list of known hosts.
Updating Repository git@github.com:shackofnoreturn/shackhq-ansible-infrastructure.git
Warning: Permanently added 'github.com' (ED25519) to the list of known hosts.
From github.com:shackofnoreturn/shackhq-ansible-infrastructure
 * branch            main       -> FETCH_HEAD
Already up to date.
No /tmp/semaphore/project_1/repository_12_template_41/collections/requirements.yml file found. Skip galaxy install process.

/tmp/semaphore/project_1/repository_12_template_41/requirements.yml has no changes. Skip galaxy install process.

No /tmp/semaphore/project_1/repository_12_template_41/collections/requirements.yml file found. Skip galaxy install process.

/tmp/semaphore/project_1/repository_12_template_41/requirements.yml has no changes. Skip galaxy install process.

No /tmp/semaphore/project_1/repository_12_template_41/roles/requirements.yml file found. Skip galaxy install process.

/tmp/semaphore/project_1/repository_12_template_41/requirements.yml has no changes. Skip galaxy install process.

No /tmp/semaphore/project_1/repository_12_template_41/roles/requirements.yml file found. Skip galaxy install process.

/tmp/semaphore/project_1/repository_12_template_41/requirements.yml has no changes. Skip galaxy install process.


PLAY [Gather Reachable Nodes] **************************************************

TASK [gather-reachable-hosts : Check SSH reachability] *************************
ok: [localhost] => (item=shack-app-d001)
ok: [localhost] => (item=shack-app-d002)
[ERROR]: Task failed: Module failed: Timeout when waiting for 10.0.0.33:22
Origin: /tmp/semaphore/project_1/repository_12_template_41/roles/gather-reachable-hosts/tasks/main.yml:2:3

1 ---
2 - name: Check SSH reachability
    ^ column 3

failed: [localhost] (item=shack-app-d003) => {"ansible_loop_var": "item", "changed": false, "elapsed": 4, "item": "shack-app-d003", "msg": "Timeout when waiting for 10.0.0.33:22"}
ok: [localhost] => (item=shack-app-d004)
...ignoring

TASK [gather-reachable-hosts : Create online group] ****************************
skipping: [localhost] => (item={'elapsed': 4, 'failed': True, 'msg': 'Timeout when waiting for 10.0.0.33:22', 'invocation': {'module_args': {'host': '10.0.0.33', 'port': 22, 'state': 'started', 'timeout': 3, 'connect_timeout': 5, 'delay': 0, 'active_connection_states': ['ESTABLISHED', 'FIN_WAIT1', 'FIN_WAIT2', 'SYN_RECV', 'SYN_SENT', 'TIME_WAIT'], 'sleep': 1, 'path': None, 'search_regex': None, 'exclude_hosts': None, 'msg': None}}, 'changed': False, 'exception': '(traceback unavailable)', 'item': 'shack-app-d003', 'ansible_loop_var': 'item'}) 
changed: [localhost] => (item={'state': 'started', 'port': 22, 'search_regex': None, 'match_groups': [], 'match_groupdict': {}, 'path': None, 'elapsed': 0, 'invocation': {'module_args': {'host': '10.0.0.31', 'port': 22, 'state': 'started', 'timeout': 3, 'connect_timeout': 5, 'delay': 0, 'active_connection_states': ['ESTABLISHED', 'FIN_WAIT1', 'FIN_WAIT2', 'SYN_RECV', 'SYN_SENT', 'TIME_WAIT'], 'sleep': 1, 'path': None, 'search_regex': None, 'exclude_hosts': None, 'msg': None}}, 'failed': False, 'changed': False, 'item': 'shack-app-d001', 'ansible_loop_var': 'item'})
changed: [localhost] => (item={'state': 'started', 'port': 22, 'search_regex': None, 'match_groups': [], 'match_groupdict': {}, 'path': None, 'elapsed': 0, 'invocation': {'module_args': {'host': '10.0.0.32', 'port': 22, 'state': 'started', 'timeout': 3, 'connect_timeout': 5, 'delay': 0, 'active_connection_states': ['ESTABLISHED', 'FIN_WAIT1', 'FIN_WAIT2', 'SYN_RECV', 'SYN_SENT', 'TIME_WAIT'], 'sleep': 1, 'path': None, 'search_regex': None, 'exclude_hosts': None, 'msg': None}}, 'failed': False, 'changed': False, 'item': 'shack-app-d002', 'ansible_loop_var': 'item'})
changed: [localhost] => (item={'state': 'started', 'port': 22, 'search_regex': None, 'match_groups': [], 'match_groupdict': {}, 'path': None, 'elapsed': 0, 'invocation': {'module_args': {'host': '10.0.0.34', 'port': 22, 'state': 'started', 'timeout': 3, 'connect_timeout': 5, 'delay': 0, 'active_connection_states': ['ESTABLISHED', 'FIN_WAIT1', 'FIN_WAIT2', 'SYN_RECV', 'SYN_SENT', 'TIME_WAIT'], 'sleep': 1, 'path': None, 'search_regex': None, 'exclude_hosts': None, 'msg': None}}, 'failed': False, 'changed': False, 'item': 'shack-app-d004', 'ansible_loop_var': 'item'})

TASK [gather-reachable-hosts : Verify host reachability] ***********************
skipping: [localhost]

PLAY [Deploy Docker Stack] *****************************************************

TASK [docker-stack-sync : Ensure git installed] ********************************
ok: [shack-app-d004]
ok: [shack-app-d002]
ok: [shack-app-d001]

TASK [docker-stack-sync : Ensure root directory] *******************************
ok: [shack-app-d004]
ok: [shack-app-d002]
ok: [shack-app-d001]

TASK [docker-stack-sync : Set deploy key] **************************************
ok: [shack-app-d001]
ok: [shack-app-d002]
ok: [shack-app-d004]

TASK [docker-stack-sync : Write deploy key] ************************************
changed: [shack-app-d004]
changed: [shack-app-d002]
changed: [shack-app-d001]

TASK [docker-stack-sync : Clone repository] ************************************
changed: [shack-app-d004]
changed: [shack-app-d002]
changed: [shack-app-d001]

TASK [docker-stack-sync : Remove deploy key] ***********************************
changed: [shack-app-d004]
changed: [shack-app-d002]
changed: [shack-app-d001]

TASK [docker-stack-template : Find Jinja templates] ****************************
ok: [shack-app-d004]
ok: [shack-app-d002]
ok: [shack-app-d001]

TASK [docker-stack-template : Create temporary directory] **********************
changed: [shack-app-d004]
changed: [shack-app-d002]
changed: [shack-app-d001]

TASK [docker-stack-template : Fetch stack templates] ***************************
changed: [shack-app-d004] => (item=/opt/docker/stacks/development/traefik/compose.yml.j2)
changed: [shack-app-d002] => (item=/opt/docker/stacks/development/traefik/compose.yml.j2)
changed: [shack-app-d004] => (item=/opt/docker/stacks/development/traefik/configs/traefik/traefik.yml.j2)
changed: [shack-app-d002] => (item=/opt/docker/stacks/development/traefik/configs/traefik/traefik.yml.j2)
changed: [shack-app-d001] => (item=/opt/docker/stacks/development/traefik/compose.yml.j2)
changed: [shack-app-d001] => (item=/opt/docker/stacks/development/traefik/configs/traefik/traefik.yml.j2)

TASK [docker-stack-template : Render templates] ********************************
[ERROR]: Task failed: Error rendering template: ../../templates/common/logging.yml.j2

Task failed.
Origin: /tmp/semaphore/project_1/repository_12_template_41/roles/docker-stack-template/tasks/main.yml:37:7

35
36
37     - name: Render templates
         ^ column 7

<<< caused by >>>

Error rendering template: ../../templates/common/logging.yml.j2
Origin: /tmp/ansible-stack-template-fdaoyhdu/0.j2

failed: [shack-app-d002] (item=/opt/docker/stacks/development/traefik/compose.yml.j2) => {"ansible_index_var": "stack_jinja_index", "ansible_loop_var": "item", "changed": false, "item": {"atime": 1795844639.3583293, "ctime": 1795844630.924231, "dev": 64519, "gid": 0, "gr_name": "root", "inode": 655374, "isblk": false, "ischr": false, "isdir": false, "isfifo": false, "isgid": false, "islnk": false, "isreg": true, "issock": false, "isuid": false, "mode": "0644", "mtime": 1795844630.924231, "nlink": 1, "path": "/opt/docker/stacks/development/traefik/compose.yml.j2", "pw_name": "root", "rgrp": true, "roth": true, "rusr": true, "size": 3496, "uid": 0, "wgrp": false, "woth": false, "wusr": true, "xgrp": false, "xoth": false, "xusr": false}, "msg": "Task failed: Error rendering template: ../../templates/common/logging.yml.j2", "stack_jinja_index": 0}
[ERROR]: Task failed: Error rendering template: ../../templates/common/logging.yml.j2

Task failed.
Origin: /tmp/semaphore/project_1/repository_12_template_41/roles/docker-stack-template/tasks/main.yml:37:7

35
36
37     - name: Render templates
         ^ column 7

<<< caused by >>>

Error rendering template: ../../templates/common/logging.yml.j2
Origin: /tmp/ansible-stack-template-gudcy5l3/0.j2

failed: [shack-app-d004] (item=/opt/docker/stacks/development/traefik/compose.yml.j2) => {"ansible_index_var": "stack_jinja_index", "ansible_loop_var": "item", "changed": false, "item": {"atime": 1795844639.1953118, "ctime": 1795844630.3232343, "dev": 65024, "gid": 0, "gr_name": "root", "inode": 654582, "isblk": false, "ischr": false, "isdir": false, "isfifo": false, "isgid": false, "islnk": false, "isreg": true, "issock": false, "isuid": false, "mode": "0644", "mtime": 1795844630.3232343, "nlink": 1, "path": "/opt/docker/stacks/development/traefik/compose.yml.j2", "pw_name": "root", "rgrp": true, "roth": true, "rusr": true, "size": 3496, "uid": 0, "wgrp": false, "woth": false, "wusr": true, "xgrp": false, "xoth": false, "xusr": false}, "msg": "Task failed: Error rendering template: ../../templates/common/logging.yml.j2", "stack_jinja_index": 0}
[ERROR]: Task failed: Error rendering template: ../../templates/common/logging.yml.j2

Task failed.
Origin: /tmp/semaphore/project_1/repository_12_template_41/roles/docker-stack-template/tasks/main.yml:37:7

35
36
37     - name: Render templates
         ^ column 7

<<< caused by >>>

Error rendering template: ../../templates/common/logging.yml.j2
Origin: /tmp/ansible-stack-template-2myxaq8c/0.j2

failed: [shack-app-d001] (item=/opt/docker/stacks/development/traefik/compose.yml.j2) => {"ansible_index_var": "stack_jinja_index", "ansible_loop_var": "item", "changed": false, "item": {"atime": 1795844640.5060043, "ctime": 1795844633.113912, "dev": 64519, "gid": 0, "gr_name": "root", "inode": 269385, "isblk": false, "ischr": false, "isdir": false, "isfifo": false, "isgid": false, "islnk": false, "isreg": true, "issock": false, "isuid": false, "mode": "0644", "mtime": 1795844633.113912, "nlink": 1, "path": "/opt/docker/stacks/development/traefik/compose.yml.j2", "pw_name": "root", "rgrp": true, "roth": true, "rusr": true, "size": 3496, "uid": 0, "wgrp": false, "woth": false, "wusr": true, "xgrp": false, "xoth": false, "xusr": false}, "msg": "Task failed: Error rendering template: ../../templates/common/logging.yml.j2", "stack_jinja_index": 0}
changed: [shack-app-d004] => (item=/opt/docker/stacks/development/traefik/configs/traefik/traefik.yml.j2)
changed: [shack-app-d002] => (item=/opt/docker/stacks/development/traefik/configs/traefik/traefik.yml.j2)
changed: [shack-app-d001] => (item=/opt/docker/stacks/development/traefik/configs/traefik/traefik.yml.j2)

TASK [docker-stack-template : Remove temporary directory] **********************
changed: [shack-app-d004]
changed: [shack-app-d002]
changed: [shack-app-d001]

PLAY RECAP *********************************************************************
localhost                  : ok=2    changed=1    unreachable=0    failed=0    skipped=1    rescued=0    ignored=1   
shack-app-d001             : ok=10   changed=6    unreachable=0    failed=1    skipped=0    rescued=0    ignored=0   
shack-app-d002             : ok=10   changed=6    unreachable=0    failed=1    skipped=0    rescued=0    ignored=0   
shack-app-d004             : ok=10   changed=6    unreachable=0    failed=1    skipped=0    rescued=0    ignored=0   

Failed to run task: exit status 2

