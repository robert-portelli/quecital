import click
import os
import toml


QUIZ_FILE = "QUIZ.toml"

@click.group()
def quecital():
    """Quecital - Your Quiz App."""
    pass


@quecital.command()
def start():
    """Start Quecital."""
    if os.path.exists(QUIZ_FILE):
        click.echo("Welcome to Quecital! What would you like to do?")
        action = click.prompt("1. Take a quiz\n2. Add a question\n3. Exit", type=int)

        if action == 1:
            # Logic to start quiz
            click.echo("Starting quiz...")
        elif action == 2:
            # Logic to add a question
            click.echo("Adding a question...")
        elif action == 3:
            click.echo("Exiting Quecital. Goodbye!")
        else:
            click.echo("Invalid choice. Exiting.")

    else:
        click.echo(f"No {QUIZ_FILE} found in the current directory.")
        create_file = click.confirm("Do you want to create a new quiz file?", default=True)

        if create_file:
            create_quiz_file()


@quecital.command()
def create_quiz_file():
    """Create a new QUIZ.toml file."""
    click.echo("Creating a new QUIZ.toml file...")
    # Logic to create a new QUIZ.toml file


if __name__ == "__main__":
    quecital()
