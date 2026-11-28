from pathlib import Path
import os
import tempfile
import unittest

from jinja2 import Environment, FileSystemLoader
import yaml


ROOT = Path(__file__).resolve().parents[1]


def load_yaml(path):
    with (ROOT / path).open(encoding="utf-8") as source:
        return yaml.safe_load(source)


class StackTemplateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tasks = load_yaml("roles/docker-stack-template/tasks/main.yml")

    def test_shared_templates_are_found_under_repository_root(self):
        shared_find = next(task for task in self.tasks if task["name"] == "Find shared Jinja templates")
        self.assertEqual(shared_find["ansible.builtin.find"]["paths"], "{{ docker_root }}/templates")
        self.assertEqual(shared_find["when"], "stack_jinja_shared_template_directory.stat.isdir | default(false)")

    def test_fetch_and_render_keep_repository_relative_paths(self):
        block = self.tasks[4]["block"]
        fetch = next(task for task in block if task["name"] == "Fetch stack and shared templates")
        include_directory = next(task for task in block if task["name"] == "Create shared include directories beside stack templates")
        stage = next(task for task in block if task["name"] == "Stage shared templates beside stack templates")
        source = next(task for task in block if task["name"] == "Render templates")
        self.assertEqual(fetch["loop"], "{{ stack_jinja_all_templates }}")
        self.assertIn("replace(docker_root ~ '/', '', 1)", fetch["ansible.builtin.fetch"]["dest"])
        self.assertIn("replace(docker_root ~ '/', '', 1)", source["ansible.builtin.template"]["src"])
        self.assertEqual(source["loop"], "{{ stack_jinja_templates.files }}")
        self.assertIn("/templates/", stage["ansible.builtin.copy"]["dest"])
        self.assertEqual(stage["delegate_to"], "localhost")
        self.assertIn("product(stack_jinja_shared_templates.files", stage["loop"])
        path_environment = Environment()
        path_environment.filters["dirname"] = os.path.dirname
        include_directory_path = path_environment.from_string(
            include_directory["ansible.builtin.file"]["path"]
        ).render(
            stack_jinja_temporary_directory={"path": "/tmp/render"},
            item=(
                {"path": "/opt/docker/stacks/development/traefik/compose.yml.j2"},
                {"path": "/opt/docker/templates/common/logging.yml.j2"},
            ),
            docker_root="/opt/docker",
        )
        self.assertEqual(
            include_directory_path,
            "/tmp/render/stacks/development/traefik/templates/common",
        )
        staged_path = path_environment.from_string(stage["ansible.builtin.copy"]["dest"]).render(
            stack_jinja_temporary_directory={"path": "/tmp/render"},
            item=(
                {"path": "/opt/docker/stacks/development/traefik/compose.yml.j2"},
                {"path": "/opt/docker/templates/common/logging.yml.j2"},
            ),
            docker_root="/opt/docker",
        )
        self.assertEqual(
            staged_path,
            "/tmp/render/stacks/development/traefik/templates/common/logging.yml.j2",
        )
        fetched_path = Environment().from_string(fetch["ansible.builtin.fetch"]["dest"]).render(
            stack_jinja_temporary_directory={"path": "/tmp/render"},
            item={"path": "/opt/docker/stacks/dev/app/compose.yml.j2"},
            docker_root="/opt/docker",
        )
        self.assertEqual(fetched_path, "/tmp/render/stacks/dev/app/compose.yml.j2")

    def test_jinja_resolves_repo_root_include_from_search_path(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            repository_root = Path(temporary_directory)
            stack_template = repository_root / "stacks/development/traefik/compose.yml.j2"
            shared_template = repository_root / "templates/common/logging.yml.j2"
            staged_shared_template = stack_template.parent / "templates/common/logging.yml.j2"
            stack_template.parent.mkdir(parents=True)
            shared_template.parent.mkdir(parents=True)
            staged_shared_template.parent.mkdir(parents=True)
            stack_template.write_text(
                "{% include 'templates/common/logging.yml.j2' %}",
                encoding="utf-8",
            )
            shared_template.write_text("logging: local", encoding="utf-8")
            staged_shared_template.write_text(shared_template.read_text(encoding="utf-8"), encoding="utf-8")

            environment = Environment(loader=FileSystemLoader(str(stack_template.parent)))
            rendered = environment.get_template(stack_template.name).render()

        self.assertEqual(rendered, "logging: local")


if __name__ == "__main__":
    unittest.main()

