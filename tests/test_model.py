import unittest
from click.testing import CliRunner
from dgen import cli


COMMAND = 'model'


class TestCommand(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.runner = CliRunner()

    def test_output(self):
        result = self.runner.invoke(cli.main, [COMMAND])
        assert result.exit_code == 0
        assert 'class MyModel(models.Model)' in result.output


class TestNameOption(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.runner = CliRunner()

    def test_option(self):
        result = self.runner.invoke(cli.main, [COMMAND, '--name=Recipe'])
        assert result.exit_code == 0
        assert 'class Recipe(models.Model)' in result.output

    def test_option_short(self):
        result = self.runner.invoke(cli.main, [COMMAND, '-nCompany'])
        assert result.exit_code == 0
        assert 'class Company(models.Model)' in result.output
