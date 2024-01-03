# quecital.py

from pathlib import Path
import click
# import tomllib


@click.group()
def quecital():
    """Quecital - Your Quiz App."""
    pass


def find_quecital_toml():
    """Find quecital.toml in the current working directory."""
    quecital_path = Path("quecital.toml")
    return quecital_path if quecital_path.is_file() else None



@quecital.command()
def start():
    # Check for quecital.toml in the cwd
    quecital_toml_path = find_quecital_toml()

    if quecital_toml_path:
        click.echo(f"Found quecital.toml at: {quecital_toml_path}")
        # Perform actions based on the existence of quecital.toml
        # ...

    else:
        click.echo("quecital.toml not found in the current working directory.")
        # Perform actions when quecital.toml is not found
        # ...
