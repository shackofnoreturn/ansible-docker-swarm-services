# Todo

- [ ] Question of need for playbook per environment/inventory
- [ ] Set up roles in semaphore
- [ ] Test all new backup/restore/move roles
- [ ] Error in semaphore:  
8:21:56 AM
TASK [docker-stack-template : Render templates] ********************************
8:21:56 AM
[ERROR]: Task failed: Error rendering template: 'templates/common/logging.yml.j2' not found in search paths: '/tmp/semaphore/project_1/repository_12_template_41/roles/docker-stack-template/templates', '/tmp/semaphore/project_1/repository_12_template_41/roles/docker-stack-template', '/tmp/semaphore/project_1/repository_12_template_41/roles/docker-stack-template/tasks/templates', '/tmp/semaphore/project_1/repository_12_template_41/roles/docker-stack-template/tasks', '/tmp/semaphore/project_1/repository_12_template_41/templates', '/tmp/semaphore/project_1/repository_12_template_41', '/tmp/semaphore/project_1/repository_12_template_41/templates', '/tmp/semaphore/project_1/repository_12_template_41', '/tmp/ansible-stack-template-qkm7_04a/stacks/development/traefik/templates', '/tmp/ansible-stack-template-qkm7_04a/stacks/development/traefik'
8:21:56 AM
8:21:56 AM
Task failed.
8:21:56 AM
Origin: /tmp/semaphore/project_1/repository_12_template_41/roles/docker-stack-template/tasks/main.yml:70:7
8:21:56 AM
8:21:56 AM
68
8:21:56 AM
69
8:21:56 AM
70     - name: Render templates
8:21:56 AM
         ^ column 7
8:21:56 AM
8:21:56 AM
<<< caused by >>>
8:21:56 AM
8:21:56 AM
Error rendering template: 'templates/common/logging.yml.j2' not found in search paths: '/tmp/semaphore/project_1/repository_12_template_41/roles/docker-stack-template/templates', '/tmp/semaphore/project_1/repository_12_template_41/roles/docker-stack-template', '/tmp/semaphore/project_1/repository_12_template_41/roles/docker-stack-template/tasks/templates', '/tmp/semaphore/project_1/repository_12_template_41/roles/docker-stack-template/tasks', '/tmp/semaphore/project_1/repository_12_template_41/templates', '/tmp/semaphore/project_1/repository_12_template_41', '/tmp/semaphore/project_1/repository_12_template_41/templates', '/tmp/semaphore/project_1/repository_12_template_41', '/tmp/ansible-stack-template-qkm7_04a/stacks/development/traefik/templates', '/tmp/ansible-stack-template-qkm7_04a/stacks/development/traefik'
8:21:56 AM
Origin: /tmp/ansible-stack-template-qkm7_04a/stacks/development/traefik/compose.yml.j2
8:21:56 AM
8:21:56 AM
failed: [shack-app-d002] (item=/opt/docker/stacks/development/traefik/compose.yml.j2) => {"ansible_loop_var": "item", "changed": false, "item": {"atime": 1795850459.7286422, "ctime": 1795850459.7296422, "dev": 64519, "gid": 0, "gr_name": "root", "inode": 655374, "isblk": false, "ischr": false, "isdir": false, "isfifo": false, "isgid": false, "islnk": false, "isreg": true, "issock": false, "isuid": false, "mode": "0644", "mtime": 1795850459.7296422, "nlink": 1, "path": "/opt/docker/stacks/development/traefik/compose.yml.j2", "pw_name": "root", "rgrp": true, "roth": true, "rusr": true, "size": 3460, "uid": 0, "wgrp": false, "woth": false, "wusr": true, "xgrp": false, "xoth": false, "xusr": false}, "msg": "Task failed: Error rendering template: 'templates/common/logging.yml.j2' not found in search paths: '/tmp/semaphore/project_1/repository_12_template_41/roles/docker-stack-template/templates', '/tmp/semaphore/project_1/repository_12_template_41/roles/docker-stack-template', '/tmp/semaphore/project_1/repository_12_template_41/roles/docker-stack-template/tasks/templates', '/tmp/semaphore/project_1/repository_12_template_41/roles/docker-stack-template/tasks', '/tmp/semaphore/project_1/repository_12_template_41/templates', '/tmp/semaphore/project_1/repository_12_template_41', '/tmp/semaphore/project_1/repository_12_template_41/templates', '/tmp/semaphore/project_1/repository_12_template_41', '/tmp/ansible-stack-template-qkm7_04a/stacks/development/traefik/templates', '/tmp/ansible-stack-template-qkm7_04a/stacks/development/traefik'"}
8:21:56 AM
[ERROR]: Task failed: Error rendering template: 'templates/common/logging.yml.j2' not found in search paths: '/tmp/semaphore/project_1/repository_12_template_41/roles/docker-stack-template/templates', '/tmp/semaphore/project_1/repository_12_template_41/roles/docker-stack-template', '/tmp/semaphore/project_1/repository_12_template_41/roles/docker-stack-template/tasks/templates', '/tmp/semaphore/project_1/repository_12_template_41/roles/docker-stack-template/tasks', '/tmp/semaphore/project_1/repository_12_template_41/templates', '/tmp/semaphore/project_1/repository_12_template_41', '/tmp/semaphore/project_1/repository_12_template_41/templates', '/tmp/semaphore/project_1/repository_12_template_41', '/tmp/ansible-stack-template-8z74ql0g/stacks/development/traefik/templates', '/tmp/ansible-stack-template-8z74ql0g/stacks/development/traefik'
8:21:56 AM
8:21:56 AM
Task failed.
8:21:56 AM
Origin: /tmp/semaphore/project_1/repository_12_template_41/roles/docker-stack-template/tasks/main.yml:70:7
8:21:56 AM
8:21:56 AM
68
8:21:56 AM
69
8:21:56 AM
70     - name: Render templates
8:21:56 AM
         ^ column 7
8:21:56 AM
8:21:56 AM
<<< caused by >>>
8:21:56 AM
8:21:56 AM
Error rendering template: 'templates/common/logging.yml.j2' not found in search paths: '/tmp/semaphore/project_1/repository_12_template_41/roles/docker-stack-template/templates', '/tmp/semaphore/project_1/repository_12_template_41/roles/docker-stack-template', '/tmp/semaphore/project_1/repository_12_template_41/roles/docker-stack-template/tasks/templates', '/tmp/semaphore/project_1/repository_12_template_41/roles/docker-stack-template/tasks', '/tmp/semaphore/project_1/repository_12_template_41/templates', '/tmp/semaphore/project_1/repository_12_template_41', '/tmp/semaphore/project_1/repository_12_template_41/templates', '/tmp/semaphore/project_1/repository_12_template_41', '/tmp/ansible-stack-template-8z74ql0g/stacks/development/traefik/templates', '/tmp/ansible-stack-template-8z74ql0g/stacks/development/traefik'
8:21:56 AM
Origin: /tmp/ansible-stack-template-8z74ql0g/stacks/development/traefik/compose.yml.j2
8:21:56 AM
8:21:56 AM
failed: [shack-app-d004] (item=/opt/docker/stacks/development/traefik/compose.yml.j2) => {"ansible_loop_var": "item", "changed": false, "item": {"atime": 1795850459.5912433, "ctime": 1795850459.5912433, "dev": 65024, "gid": 0, "gr_name": "root", "inode": 654582, "isblk": false, "ischr": false, "isdir": false, "isfifo": false, "isgid": false, "islnk": false, "isreg": true, "issock": false, "isuid": false, "mode": "0644", "mtime": 1795850459.5912433, "nlink": 1, "path": "/opt/docker/stacks/development/traefik/compose.yml.j2", "pw_name": "root", "rgrp": true, "roth": true, "rusr": true, "size": 3460, "uid": 0, "wgrp": false, "woth": false, "wusr": true, "xgrp": false, "xoth": false, "xusr": false}, "msg": "Task failed: Error rendering template: 'templates/common/logging.yml.j2' not found in search paths: '/tmp/semaphore/project_1/repository_12_template_41/roles/docker-stack-template/templates', '/tmp/semaphore/project_1/repository_12_template_41/roles/docker-stack-template', '/tmp/semaphore/project_1/repository_12_template_41/roles/docker-stack-template/tasks/templates', '/tmp/semaphore/project_1/repository_12_template_41/roles/docker-stack-template/tasks', '/tmp/semaphore/project_1/repository_12_template_41/templates', '/tmp/semaphore/project_1/repository_12_template_41', '/tmp/semaphore/project_1/repository_12_template_41/templates', '/tmp/semaphore/project_1/repository_12_template_41', '/tmp/ansible-stack-template-8z74ql0g/stacks/development/traefik/templates', '/tmp/ansible-stack-template-8z74ql0g/stacks/development/traefik'"}
8:21:56 AM
[ERROR]: Task failed: Error rendering template: 'templates/common/logging.yml.j2' not found in search paths: '/tmp/semaphore/project_1/repository_12_template_41/roles/docker-stack-template/templates', '/tmp/semaphore/project_1/repository_12_template_41/roles/docker-stack-template', '/tmp/semaphore/project_1/repository_12_template_41/roles/docker-stack-template/tasks/templates', '/tmp/semaphore/project_1/repository_12_template_41/roles/docker-stack-template/tasks', '/tmp/semaphore/project_1/repository_12_template_41/templates', '/tmp/semaphore/project_1/repository_12_template_41', '/tmp/semaphore/project_1/repository_12_template_41/templates', '/tmp/semaphore/project_1/repository_12_template_41', '/tmp/ansible-stack-template-zdiq11w3/stacks/development/traefik/templates', '/tmp/ansible-stack-template-zdiq11w3/stacks/development/traefik'
8:21:56 AM
8:21:56 AM
Task failed.
8:21:56 AM
Origin: /tmp/semaphore/project_1/repository_12_template_41/roles/docker-stack-template/tasks/main.yml:70:7
8:21:56 AM
8:21:56 AM
68
8:21:56 AM
69
8:21:56 AM
70     - name: Render templates
8:21:56 AM
         ^ column 7
8:21:56 AM
8:21:56 AM
<<< caused by >>>
8:21:56 AM
8:21:56 AM
Error rendering template: 'templates/common/logging.yml.j2' not found in search paths: '/tmp/semaphore/project_1/repository_12_template_41/roles/docker-stack-template/templates', '/tmp/semaphore/project_1/repository_12_template_41/roles/docker-stack-template', '/tmp/semaphore/project_1/repository_12_template_41/roles/docker-stack-template/tasks/templates', '/tmp/semaphore/project_1/repository_12_template_41/roles/docker-stack-template/tasks', '/tmp/semaphore/project_1/repository_12_template_41/templates', '/tmp/semaphore/project_1/repository_12_template_41', '/tmp/semaphore/project_1/repository_12_template_41/templates', '/tmp/semaphore/project_1/repository_12_template_41', '/tmp/ansible-stack-template-zdiq11w3/stacks/development/traefik/templates', '/tmp/ansible-stack-template-zdiq11w3/stacks/development/traefik'
8:21:56 AM
Origin: /tmp/ansible-stack-template-zdiq11w3/stacks/development/traefik/compose.yml.j2
8:21:56 AM
8:21:56 AM
failed: [shack-app-d001] (item=/opt/docker/stacks/development/traefik/compose.yml.j2) => {"ansible_loop_var": "item", "changed": false, "item": {"atime": 1795850462.7955945, "ctime": 1795850462.7955945, "dev": 64519, "gid": 0, "gr_name": "root", "inode": 269385, "isblk": false, "ischr": false, "isdir": false, "isfifo": false, "isgid": false, "islnk": false, "isreg": true, "issock": false, "isuid": false, "mode": "0644", "mtime": 1795850462.7955945, "nlink": 1, "path": "/opt/docker/stacks/development/traefik/compose.yml.j2", "pw_name": "root", "rgrp": true, "roth": true, "rusr": true, "size": 3460, "uid": 0, "wgrp": false, "woth": false, "wusr": true, "xgrp": false, "xoth": false, "xusr": false}, "msg": "Task failed: Error rendering template: 'templates/common/logging.yml.j2' not found in search paths: '/tmp/semaphore/project_1/repository_12_template_41/roles/docker-stack-template/templates', '/tmp/semaphore/project_1/repository_12_template_41/roles/docker-stack-template', '/tmp/semaphore/project_1/repository_12_template_41/roles/docker-stack-template/tasks/templates', '/tmp/semaphore/project_1/repository_12_template_41/roles/docker-stack-template/tasks', '/tmp/semaphore/project_1/repository_12_template_41/templates', '/tmp/semaphore/project_1/repository_12_template_41', '/tmp/semaphore/project_1/repository_12_template_41/templates', '/tmp/semaphore/project_1/repository_12_template_41', '/tmp/ansible-stack-template-zdiq11w3/stacks/development/traefik/templates', '/tmp/ansible-stack-template-zdiq11w3/stacks/development/traefik'"}
8:21:57 AM
changed: [shack-app-d004] => (item=/opt/docker/stacks/development/traefik/configs/traefik/traefik.yml.j2)
8:21:58 AM
changed: [shack-app-d002] => (item=/opt/docker/stacks/development/traefik/configs/traefik/traefik.yml.j2)
8:22:00 AM
changed: [shack-app-d001] => (item=/opt/docker/stacks/development/traefik/configs/traefik/traefik.yml.j2)
8:22:00 AM
8:22:00 AM
TASK [docker-stack-template : Remove temporary directory] **********************
  
  
Here is again how the other repo looks like we are deploying stacks from:  
.
├── global.yml
├── README.md
├── scripts
│   └── semaphore-run.sh
├── stacks
│   ├── development
│   │   ├── arr-media
│   │   │   ├── compose.yml
│   │   │   ├── configs
│   │   │   ├── README.md
│   │   │   ├── secrets
│   │   │   └── stack.yml
│   │   ├── downloads
│   │   │   ├── compose.yml.j2
│   │   │   ├── configs
│   │   │   ├── README.md
│   │   │   ├── secrets
│   │   │   └── stack.yml
│   │   ├── downloads_
│   │   │   ├── compose.yml
│   │   │   ├── configs
│   │   │   ├── README.md
│   │   │   ├── secrets
│   │   │   └── stack.yml
│   │   ├── files
│   │   │   ├── compose.yml
│   │   │   ├── configs
│   │   │   ├── README.md
│   │   │   ├── secrets
│   │   │   └── stack.yml
│   │   ├── monitoring
│   │   │   ├── compose.yml
│   │   │   ├── configs
│   │   │   │   └── gatus
│   │   │   │       └── config.yaml.j2
│   │   │   ├── README.md
│   │   │   ├── secrets
│   │   │   └── stack.yml
│   │   ├── stash
│   │   │   ├── compose.yml
│   │   │   ├── configs
│   │   │   ├── README.md
│   │   │   ├── secrets
│   │   │   └── stack.yml
│   │   └── traefik
│   │       ├── compose.yml.j2
│   │       ├── configs
│   │       │   └── traefik
│   │       │       ├── dynamic
│   │       │       │   ├── middlewares.yml
│   │       │       │   └── proxmox.yml
│   │       │       └── traefik.yml.j2
│   │       ├── README.md
│   │       ├── secrets
│   │       │   ├── cloudflare_api_token.age
│   │       │   └── dashboard_users.age
│   │       └── stack.yml
│   ├── management
│   │   ├── monitoring
│   │   │   ├── compose.yml
│   │   │   ├── configs
│   │   │   │   └── gatus
│   │   │   │       └── config.yaml.j2
│   │   │   ├── README.md
│   │   │   ├── secrets
│   │   │   └── stack.yml
│   │   └── traefik
│   │       ├── compose.yml
│   │       ├── configs
│   │       │   ├── dynamic
│   │       │   │   ├── middlewares.yml
│   │       │   │   └── proxmox.yml
│   │       │   └── traefik.yml.j2
│   │       ├── README.md
│   │       ├── secrets
│   │       │   ├── cloudflare_api_token.age
│   │       │   └── dashboard_users.age
│   │       └── stack.yml
│   ├── production
│   │   └── traefik
│   │       ├── compose.yml
│   │       ├── configs
│   │       │   ├── dynamic
│   │       │   │   ├── middlewares.yml
│   │       │   │   └── proxmox.yml
│   │       │   └── traefik.yml.j2
│   │       ├── README.md
│   │       ├── secrets
│   │       │   ├── cloudflare_api_token.age
│   │       │   └── dashboard_users.age
│   │       └── stack.yml
│   ├── README.md
│   ├── templates
│   │   ├── common
│   │   │   └── logging.yml.j2
│   │   ├── healthchecks
│   │   │   └── http.yml.j2
│   │   ├── labels
│   │   │   ├── homepage.yml.j2
│   │   │   └── traefik.yml.j2
│   │   ├── mounts
│   │   │   └── runtime-config.yml.j2
│   │   ├── placement
│   │   │   └── node-label.yml.j2
│   │   ├── policies
│   │   │   ├── high.yml.j2
│   │   │   ├── low.yml.j2
│   │   │   └── medium.yml.j2
│   │   └── resources
│   │       ├── high.yml.j2
│   │       ├── low.yml.j2
│   │       └── medium.yml.j2
│   └── testing
│       ├── monitoring
│       │   ├── compose.yml
│       │   ├── configs
│       │   │   └── gatus
│       │   │       └── config.yaml.j2
│       │   ├── README.md
│       │   ├── secrets
│       │   └── stack.yml
│       ├── stash
│       │   ├── compose.yml
│       │   ├── configs
│       │   ├── README.md
│       │   ├── secrets
│       │   └── stack.yml
│       └── traefik
│           ├── compose.yml.j2
│           ├── configs
│           │   └── traefik
│           │       ├── dynamic
│           │       │   ├── middlewares.yml
│           │       │   └── proxmox.yml
│           │       └── traefik.yml.j2
│           ├── README.md
│           ├── secrets
│           │   ├── cloudflare_api_token.age
│           │   └── dashboard_users.age
│           └── stack.yml
├── templates
│   ├── common
│   │   └── logging.yml.j2
│   ├── healthchecks
│   │   └── http.yml.j2
│   ├── labels
│   │   ├── homepage.yml.j2
│   │   └── traefik.yml.j2
│   ├── mounts
│   │   └── runtime-config.yml.j2
│   ├── placement
│   │   └── node-label.yml.j2
│   ├── policies
│   │   ├── high.yml.j2
│   │   ├── low.yml.j2
│   │   └── medium.yml.j2
│   └── resources
│       ├── high.yml.j2
│       ├── low.yml.j2
│       └── medium.yml.j2
└── templates_BAK
    ├── common
    │   └── logging.yml.j2
    ├── labels
    │   ├── homepage.yml.j2
    │   └── traefik.yml.j2
    ├── policies
    │   ├── high.yml.j2
    │   ├── low.yml.j2
    │   └── medium.yml.j2
    └── resources
        ├── high.yml.j2
        ├── low.yml.j2
        └── medium.yml.j2

76 directories, 99 files  
  