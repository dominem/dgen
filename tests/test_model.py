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


class TestFieldOption(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.runner = CliRunner()

    def test_option(self):
        result = self.runner.invoke(cli.main, [COMMAND, '--field=t:name'])
        assert result.exit_code == 0

    def test_option_short(self):
        result = self.runner.invoke(cli.main, [COMMAND, '-ft:name'])
        assert result.exit_code == 0

    def test_text_field(self):
        result = self.runner.invoke(cli.main, [COMMAND, '-ft:name'])
        assert 'name = models.TextField(' in result.output
        assert "verbose_name=_('Name')" in result.output

    def test_spaced_verbose_name(self):
        result = self.runner.invoke(cli.main, [COMMAND, '-ft:company_name'])
        assert "verbose_name=_('Company name')" in result.output

    def test_integer_field(self):
        result = self.runner.invoke(cli.main, [COMMAND, '-fi:employee_count'])
        assert 'employee_count = models.IntegerField(' in result.output
        assert "verbose_name=_('Employee count')" in result.output

    def test_boolean_field(self):
        result = self.runner.invoke(cli.main, [COMMAND, '-fb:is_active'])
        assert 'is_active = models.BooleanField(' in result.output
        assert 'default=False,' in result.output
        assert "verbose_name=_('Is active')" in result.output

    def test_multiple_fields(self):
        result = self.runner.invoke(cli.main, [COMMAND, '-ft:company_name', '-fi:employee_count'])
        assert 'company_name = models.TextField(' in result.output
        assert "verbose_name=_('Company name')" in result.output
        assert 'employee_count = models.IntegerField(' in result.output
        assert "verbose_name=_('Employee count')" in result.output

    def test_fail_without_field_name(self):
        result = self.runner.invoke(cli.main, [COMMAND, '-ft'])
        assert result.exit_code == 2
        assert 'field needs to be in format <type:name>, e.g. t:body' in result.output
