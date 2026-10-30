# Ansible Docker Swarm Services
*Roles to help you manage services in an existing Docker Swarm*


## What

Ansible playbooks for synchronizing, validating, deploying, inspecting, and
removing Docker Swarm stacks from `shackhq-docker-stacks`.

## How

Run pre-deploy validation before deploying a stack. Use the inventory for the
target environment and the same `stack_name` you would pass to deployment:

```bash
ansible-playbook \
	-i /path/to/shackhq-ansible-infrastructure/inventories/development/inventory.yml \
	playbook-stack-validate.yml \
	--limit development \
	--extra-vars stack_name=traefik
```

Validation synchronizes the selected stack revision, checks its manifest and
Compose files, validates the merged Compose configuration with `docker compose
config --format json` on the active Swarm manager, confirms declared runtime
directories exist, and checks that all Compose-declared external networks and
secrets exist in the target Swarm. For every service with placement
constraints, it also verifies that at least one Ready and Active node has the
required role and labels. Placement constraints must use `node.role == <role>`
or `node.labels.<label> == <value>`. The active manager must have Docker and the
Docker Compose plugin installed. Create missing external networks or secrets,
or correct node labels and availability, before running
`playbook-stack-deploy.yml`.

In Semaphore, select the matching environment inventory, set `stack_name`, and
run `playbook-stack-validate.yml` as the pre-deploy step.

## Todo
- Move stacks folder to actual stacks repo