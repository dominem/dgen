import click
from jinja2 import PackageLoader
from dgen import jinja


env = jinja.create_env(PackageLoader(package_name=__package__))


def model(name):
    template = env.get_template('model.py')
    context = {'name': name}
    click.echo(template.render(context))
