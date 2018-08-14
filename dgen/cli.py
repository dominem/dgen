import click
from . import commands


@click.group()
def main():
    """Command-line utility for Django code generation."""
    pass


@main.command(short_help='Generate CMS-like templates.')
@click.argument('directory')
@click.option('--title', default='My Project', help='Project title.')
def templates(directory, title):
    """
    Generate CMS-like generic templates for Index and CRUD Class-Based Views.

    \b
    Includes:
        - base.html
        - index.html
        - list.html
        - form.html
        - confirm_delete.html
        - breadcrumb.html

    \b
    WARNING:
    Please, note that the command will overwrite files
    in the given DIRECTORY if such files already exist.
    If this is the case, make sure that you have a backup.
    """
    commands.templates(directory, title)


@main.command(short_help='Generate Model template.')
def model():
    """Generate common Model template with Meta class and overridden __str__ method."""
    commands.model()
