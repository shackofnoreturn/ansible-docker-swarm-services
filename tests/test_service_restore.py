from pathlib import Path
import unittest

import yaml


ROOT = Path(__file__).resolve().parents[1]


def load_yaml(path):
    with (ROOT / path).open(encoding="utf-8") as source:
        return yaml.safe_load(source)


class ServiceRestoreTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.defaults = load_yaml("roles/docker-service-restore/defaults/main.yml")
        cls.tasks = load_yaml("roles/docker-service-restore/tasks/main.yml")
        cls.playbook = load_yaml("playbook-service-restore.yml")

    def test_restore_paths_match_backup_layout(self):
        self.assertEqual(
            self.defaults["service_backup_path"],
            "{{ service_backup_root }}/{{ env }}/{{ stack_name }}/{{ service_name }}",
        )
        self.assertEqual(
            self.defaults["service_restore_pattern"],
            "data_{{ env }}_{{ stack_name }}_{{ service_name }}_*.zip",
        )

    def test_restore_selects_latest_or_explicit_archive(self):
        tasks = {task["name"]: task for task in self.tasks}
        self.assertEqual(
            tasks["Find matching service backups"]["ansible.builtin.find"]["patterns"],
            "{{ service_restore_pattern }}",
        )
        self.assertIn("sort(attribute='mtime') | last", tasks["Select the newest service backup"]["ansible.builtin.set_fact"]["service_restore_selected_archive"])
        self.assertEqual(
            tasks["Select the requested service backup"]["ansible.builtin.set_fact"]["service_restore_selected_archive"],
            "{{ service_restore_file }}",
        )

    def test_restore_overwrites_into_service_data_directory(self):
        restore = next(task["ansible.builtin.unarchive"] for task in self.tasks if task["name"] == "Restore service data")
        self.assertEqual(restore["dest"], "{{ service_data_path }}")
        self.assertTrue(restore["remote_src"])
        self.assertFalse(restore["keep_newer"])

    def test_playbook_targets_the_service_labeled_host(self):
        locate = next(play for play in self.playbook if play["name"] == "Locate Service Host")
        find_hosts = next(task for task in locate["tasks"] if task["name"] == "Find hosts labeled for the service")
        self.assertEqual(find_hosts["loop"], "{{ groups['docker_online'] | default([]) }}")
        self.assertIn("hostvars[item][service_name]", find_hosts["when"])

        restore = next(play for play in self.playbook if play["name"] == "Restore Docker Service Data")
        self.assertEqual(restore["hosts"], "docker_service_restore")
        self.assertEqual(restore["roles"], ["docker-service-restore"])


if __name__ == "__main__":
    unittest.main()

