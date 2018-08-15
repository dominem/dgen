import click
from jinja2 import PackageLoader
from dgen import jinja


env = jinja.create_env(PackageLoader(package_name=__package__))


TEXT_FIELD = """
    %s = models.TextField(
        verbose_name=_('%s')
    )"""

INTEGER_FIELD = """
    %s = models.IntegerField(
        verbose_name=_('%s')
    )"""

BOOLEAN_FIELD = """
    %s = models.BooleanField(
        default=False,
        verbose_name=_('%s')
    )"""

DATE_FIELD = """
    %s = models.DateField(
        verbose_name=_('%s')
    )"""

DATETIME_FIELD = """
    %s = models.DateTimeField(
        verbose_name=_('%s')
    )"""

FIELDS = {
    't': TEXT_FIELD,
    'i': INTEGER_FIELD,
    'b': BOOLEAN_FIELD,
    'd': DATE_FIELD,
    'dt': DATETIME_FIELD,
}


def get_field(ftype, name):
    verbose_name = name.replace('_', ' ').capitalize()
    return FIELDS[ftype] % (name, verbose_name)


def parse_fields(fields):
    parsed_fields = []
    for field in fields:
        parsed_field = get_field(ftype=field[0], name=field[1])
        parsed_fields.append(parsed_field)
    return parsed_fields


def model(name, fields):
    template = env.get_template('model.py')
    fields = parse_fields(fields)
    context = {'name': name, 'fields': fields}
    click.echo(template.render(context))
