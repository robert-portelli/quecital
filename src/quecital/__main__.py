# __main__.py
import click
from . import quecital


@click.group()
def cli():
    pass


cli.add_command(quecital.start)
#cli.add_command(quecital.find_quecital_toml)
