import click


@click.group()
def main():
    """Command-line utility for Django code generation."""
    pass


@main.command(short_help='Generate common templates.')
@click.argument('directory')
def templates(directory):
    """
    Generate templates for common Index and CRUD Class-Based Views.

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
    click.echo(f'Templates generated into {directory} directory.')
