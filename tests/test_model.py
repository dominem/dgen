import unittest
from click.testing import CliRunner
from dgen import cli

COMMAND = 'model'

RESULT = """class MyModel(models.Model):
    class Meta:
        verbose_name = _('MyModel')
        verbose_name_plural = _('MyModels')
        ordering = ['id']

    def __str__(self):
        return f'MyModel{self.id}'
"""


class TestCommand(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.runner = CliRunner()

    def test_output(self):
        result = self.runner.invoke(cli.main, [COMMAND])
        assert result.exit_code == 0
        assert result.output == RESULT
