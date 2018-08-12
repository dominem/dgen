import os
import click
from jinja2 import PackageLoader
from dgen import jinja
from dgen.tempdir import tempdir


jinja.env.loader = PackageLoader(package_name=__package__)


def templates(directory):
    context = {'title': 'dgen'}
    template_names = jinja.env.list_templates()
    generate(template_names, context)
    dst_path = os.path.abspath(directory)
    tempdir.copy_files(template_names, dst_path)
    success_message(dst_path)


def generate(template_names, context):
    for template_name in template_names:
        path = os.path.join(tempdir.path, template_name)
        template = jinja.env.get_template(template_name)
        template.stream(**context).dump(path)


def success_message(dst_path):
    click.secho('Templates have been generated to the ', fg='green', nl=False)
    click.secho(dst_path, fg='green', bold=True, nl=False)
    click.secho(' directory.', fg='green')
