# Docker Swarm Services
*Roles to help you manage services in an existing Docker Swarm*

The stack deployment playbook syncs the stack repository, renders `.j2`, `.jinja`, and `.jinja2` files found recursively under the selected stack directory, then validates and deploys the rendered stack. Each template is written beside its source with the template suffix removed.

## Stack Data Backup and Restore

`playbook-stack-backup.yml` archives each Compose service's data directory, and `playbook-stack-restore.yml` restores the newest matching archive for each service. Both playbooks derive service names from the validated Compose configuration and require exactly one reachable inventory host per service, labeled with that service name set to `true`.

Set `stack_name` and `env` through inventory or extra variables, and ensure the `community.general` collection from `requirements.yml` is installed:

```sh
ansible-galaxy collection install -r requirements.yml
ansible-playbook playbook-stack-backup.yml -e "stack_name=app env=production"
ansible-playbook playbook-stack-restore.yml -e "stack_name=app env=production"
```

