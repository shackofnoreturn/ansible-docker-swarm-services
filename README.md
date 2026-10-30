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
config --format json` on the active Swarm manager, checks any declared
`required_directories`, and checks that all Compose-declared external networks
and secrets exist in the target Swarm. `required_directories` are paths that
must already exist, such as external mounts. `runtime_directories` are created
by the deploy role and are not preflight prerequisites. For every service with placement
constraints, it also verifies that at least one Ready and Active node has the
required role and labels. Placement constraints must use `node.role == <role>`
or `node.labels.<label> == <value>`. The active manager must have Docker and the
Docker Compose plugin installed. Create missing external networks or secrets,
or correct node labels and availability, before running
`playbook-stack-deploy.yml`.

In Semaphore, select the matching environment inventory, set `stack_name`, and
run `playbook-stack-validate.yml` as the pre-deploy step.

After deploying, the role waits for every stack service's current replica count
to match its desired count. The default timeout is five minutes
(`docker_stack_convergence_retries: 30`,
`docker_stack_convergence_delay: 10`). Override either variable in the inventory
for stacks that legitimately need a longer startup. If convergence times out,
the final service and task states are included in the Ansible failure output.

Stacks can declare public endpoint checks in `stack.yml` under `smoke_tests`.
After convergence, the deploy role checks each hostname resolves from the active
manager and that its URL returns the declared HTTP status. HTTPS checks also
verify the certificate chain and hostname by default; set
`docker_stack_smoke_test_validate_certs: false` in development or testing
inventories when those environments use staging or self-signed certificates.
Endpoint checks retry up to six times with a five-second delay by default;
`docker_stack_smoke_test_retries` and `docker_stack_smoke_test_delay` can tune
that window.
