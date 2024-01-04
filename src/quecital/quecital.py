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

def create_quecital_file():
    file_name = 'quecital.toml'
    # Open the file in write mode, creating it if it doesn't exist
    open(file_name, 'w', encoding='utf-8').close()
    # The file is open and immediately closed, creating an empty file

    click.echo(f"Empty file '{file_name}' created.")


@quecital.command()
def start():
    # Check for quecital.toml in the cwd
    quecital_toml_path = find_quecital_toml()

    if quecital_toml_path:
        click.echo(f"""
                    Welcome to Quecital!
                    Found quecital.toml at: {quecital_toml_path}
                    What would you like to do?
            """)
        # Perform actions based on the existence of quecital.toml
        action = click.prompt(
            "1. Take a quiz\n2. Add a question\n3. Exit", type=int)

        match action:
            case 1:
                # Logic to start quiz
                click.echo("Starting quiz...")
            case 2:
                # Logic to add a question
                click.echo("Adding a question...")
            case 3:
                click.echo("Exiting Quecital. Goodbye!")
            case _:
                click.echo("Invalid choice. Exiting.")

    else:
        click.echo("quecital.toml not found in the current working directory.")
        # Perform actions when quecital.toml is not found
        create_file = click.confirm("Do you want to create a new quiz file?", default=True)

        if create_file:
            create_quecital_file()
