# Docker Service Restore

Restores a service data ZIP from the NFS backup location to the service's data directory on the reachable inventory host whose variable named after `service_name` is `true`. Existing files are overwritten. By default, the newest matching archive is selected.

## Variables

| Variable | Default | Description |
| --- | --- | --- |
| `service_name` | `""` | Service name and inventory host label to locate. Required. |
| `stack_name` | `""` | Stack name used to locate the backup. Required. |
| `env` | `""` | Environment name used to locate the backup and construct the default data path. Required. |
| `docker_root` | `"/opt/docker"` | Docker data root. |
| `docker_data_root` | `"{{ docker_root }}/data/{{ env }}"` | Environment-specific root for service data. |
| `service_data_path` | `"{{ docker_data_root }}/{{ service_name }}"` | Destination directory; override when service data uses another layout. |
| `service_backup_root` | `"/mnt/nfs/fil-p001/backups/docker/data"` | Root of the mounted NFS backup share. |
| `service_backup_path` | `"{{ service_backup_root }}/{{ env }}/{{ stack_name }}/{{ service_name }}"` | Directory containing service backup archives. |
| `service_restore_file` | `""` | Optional exact archive path. When empty, the newest matching archive is restored. |
| `service_restore_pattern` | `"data_{{ env }}_{{ stack_name }}_{{ service_name }}_*.zip"` | Filename pattern used when selecting the newest archive. |

## Playbook

Run `playbook-service-restore.yml` with `service_name`, `stack_name`, and `env` supplied through inventory or extra variables. Set `service_restore_file` to restore a specific archive instead of the newest matching one.

```sh
ansible-playbook playbook-service-restore.yml -e "service_name=database stack_name=app env=production"
```

