# Docker Service Backup

Backs up one service's data directory as a ZIP archive on the NFS backup share. The service runs on the reachable inventory host whose variable named after `service_name` is set to `true`.

## Variables

| Variable | Default | Description |
| --- | --- | --- |
| `service_name` | `""` | Service name and inventory host label to locate. Required. |
| `stack_name` | `""` | Stack name used in the backup directory and filename. Required. |
| `env` | `""` | Environment name used in the source path, backup directory, and filename. Required. |
| `docker_root` | `"/opt/docker"` | Docker data root. |
| `docker_data_root` | `"{{ docker_root }}/data/{{ env }}"` | Environment-specific root for service data. |
| `service_data_path` | `"{{ docker_data_root }}/{{ service_name }}"` | Source directory to archive; override when service data uses another layout. |
| `service_backup_root` | `"/mnt/nfs/fil-p001/backups/docker/data"` | Root of the mounted NFS backup share. |

The role writes `data_<env>_<stack>_<service>_<UTC timestamp>.zip` under `<service_backup_root>/<env>/<stack>/<service>`.

## Playbook

Run `playbook-service-backup.yml` with `service_name`, `stack_name`, and `env` supplied through inventory or extra variables. For example:

```sh
ansible-playbook playbook-service-backup.yml -e "service_name=database stack_name=app env=production"
```


