from pathlib import Path
import unittest

import yaml


ROOT = Path(__file__).resolve().parents[1]


def load_yaml(path):
    with (ROOT / path).open(encoding="utf-8") as source:
        return yaml.safe_load(source)


class ServiceMoveTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.defaults = load_yaml("roles/docker-service-move/defaults/main.yml")
        cls.tasks = load_yaml("roles/docker-service-move/tasks/main.yml")
        cls.playbook = load_yaml("playbook-service-move.yml")

    def test_move_requires_service_target_and_manager(self):
        requirements = self.tasks[0]["ansible.builtin.assert"]["that"]
        self.assertIn("service_name | length > 0", requirements)
        self.assertIn("service_target_host | length > 0", requirements)
        self.assertIn("docker_swarm_manager_host | length > 0", requirements)

    def test_target_must_be_reachable_and_distinct(self):
        target_check = self.tasks[1]["ansible.builtin.assert"]["that"]
        self.assertEqual(
            target_check,
            ["service_target_host in groups[service_move_target_group] | default([])"],
        )
        distinct_check = self.tasks[4]["ansible.builtin.assert"]["that"]
        self.assertEqual(distinct_check, ["service_target_host != service_move_source_hosts[0]"])

    def test_destination_is_labeled_before_source_label_is_removed(self):
        add_label = self.tasks[6]
        remove_label = self.tasks[7]
        self.assertEqual(add_label["ansible.builtin.command"]["argv"][3], "--label-add")
        self.assertEqual(remove_label["ansible.builtin.command"]["argv"][3], "--label-rm")
        self.assertEqual(add_label["delegate_to"], "{{ docker_swarm_manager_host }}")
        self.assertEqual(remove_label["delegate_to"], "{{ docker_swarm_manager_host }}")

    def test_playbook_gathers_reachable_hosts_then_runs_move_role(self):
        self.assertEqual(self.playbook[0]["roles"], ["gather-reachable-hosts"])
        self.assertEqual(self.playbook[1]["hosts"], "localhost")
        self.assertEqual(self.playbook[1]["roles"], ["docker-service-move"])
        self.assertEqual(self.defaults["service_move_target_group"], "docker_online")


if __name__ == "__main__":
    unittest.main()

