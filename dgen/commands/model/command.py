import click
from jinja2 import PackageLoader
from dgen import jinja


env = jinja.create_env(PackageLoader(package_name=__package__))


def model():
    template = env.get_template('model.py')
    click.echo(template.render())
