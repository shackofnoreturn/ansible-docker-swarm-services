from pathlib import Path
import unittest

import yaml


ROOT = Path(__file__).resolve().parents[1]


def load_yaml(path):
    with (ROOT / path).open(encoding="utf-8") as source:
        return yaml.safe_load(source)


class StackDataPlaybookTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.backup = load_yaml("playbook-stack-backup.yml")
        cls.restore = load_yaml("playbook-stack-restore.yml")

    def test_both_playbooks_derive_service_names_from_compose_config(self):
        for playbook in (self.backup, self.restore):
            prepare = next(play for play in playbook if play["name"] == "Prepare Docker Stack Services")
            expose_services = prepare["tasks"][0]["ansible.builtin.set_fact"]["stack_service_names"]
            self.assertIn("(compose_validation.stdout | from_json).services", expose_services)
            self.assertIn("map(attribute='key') | list", expose_services)

    def test_both_playbooks_validate_one_reachable_owner_per_service(self):
        for playbook in (self.backup, self.restore):
            placement = next(play for play in playbook if play["name"] == "Validate Stack Service Placement")
            owner_check = placement["tasks"][1]
            self.assertEqual(owner_check["loop"], "{{ stack_service_names }}")
            condition = owner_check["ansible.builtin.assert"]["that"][0]
            self.assertIn("groups['docker_online']", condition)
            self.assertIn("selectattr(item, 'truthy')", condition)
            self.assertIn("length == 1", condition)

    def test_backup_and_restore_loop_existing_service_roles_by_host_label(self):
        cases = (
            (self.backup, "Backup Docker Stack Services", "docker-service-backup"),
            (self.restore, "Restore Docker Stack Services", "docker-service-restore"),
        )
        for playbook, play_name, role_name in cases:
            service_play = next(play for play in playbook if play["name"] == play_name)
            task = service_play["tasks"][0]
            self.assertEqual(task["ansible.builtin.include_role"]["name"], role_name)
            self.assertEqual(task["loop"], "{{ hostvars['localhost'].stack_service_names }}")
            self.assertIn("hostvars[inventory_hostname][stack_service_name]", task["when"])


if __name__ == "__main__":
    unittest.main()

