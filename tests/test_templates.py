import os
from click.testing import CliRunner
from dgen import cli


COMMAND = 'templates'
TEMPLATES_DIR = 'templates_dir'
TEMPLATES = [f'{t}.html' for t in [
    'base',
    'index',
    'list',
    'form',
    'confirm_delete',
    'breadcrumb',
]]


def assert_template_files_exist(dir_path):
    for template in TEMPLATES:
        template_path = os.path.join(dir_path, template)
        assert os.path.isfile(template_path)


def assert_templates(result, templates_dir_path):
    assert result.exit_code == 0
    assert result.output == f'Templates have been generated to the {templates_dir_path} directory.\n'
    assert_template_files_exist(templates_dir_path)


def test_templates_with_not_existing_templates_dir():
    runner = CliRunner()
    with runner.isolated_filesystem():
        result = runner.invoke(cli.main, [COMMAND, TEMPLATES_DIR])
        templates_dir_path = os.path.abspath(TEMPLATES_DIR)
        assert_templates(result, templates_dir_path)


def test_templates_with_existing_templates_dir():
    runner = CliRunner()
    with runner.isolated_filesystem():
        templates_dir_path = os.path.abspath(TEMPLATES_DIR)
        os.mkdir(templates_dir_path)
        result = runner.invoke(cli.main, [COMMAND, TEMPLATES_DIR])
        assert_templates(result, templates_dir_path)
