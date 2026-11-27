# Docker Service Move

Moves a service's Swarm placement label from its current reachable inventory host to a requested reachable host. Both Docker node updates run on the configured Swarm manager. The target label is applied before the old label is removed.

## Variables

| Variable | Default | Description |
| --- | --- | --- |
| `service_name` | `""` | Service label key. Exactly one reachable host must have an inventory variable of this name set to `true`. |
| `service_target_host` | `""` | Inventory hostname of the reachable destination. |
| `docker_swarm_manager_host` | `""` | Inventory hostname of a reachable Swarm manager used to run `docker node update`. |
| `service_move_target_group` | `"docker_online"` | Inventory group containing reachable source and destination nodes. |
| `docker_swarm_node_name` | inventory hostname | Optional per-host variable containing the Docker Swarm node name when it differs from the inventory hostname. |

## Playbook

Set `service_name` and `docker_swarm_manager_host` in inventory or extra variables, and pass the destination host:

```sh
ansible-playbook playbook-service-move.yml -e "service_name=database service_target_host=swarm-worker-02 docker_swarm_manager_host=swarm-manager-01"
```

