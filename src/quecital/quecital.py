# quecital.py

from pathlib import Path
import tomllib
import click
from tomli_w import dump
from quecital import quiz, add_quiz_question, add_recital


@click.group()
def quecital():
    """Quecital - Your Quiz App."""
    pass


def find_quecital_toml(quecital_storage):
    quecital_path = Path(quecital_storage)
    return quecital_path if quecital_path.is_file() else None


def new_topic():
    topic = input("Enter topic name: ").lower()
    label = topic.capitalize()
    return {topic: {"label": label, "questions": [], "recitals": []}}


def add_new_topic(topic, quecital_toml_path):
    quecital_toml = tomllib.loads(quecital_toml_path.read_text(encoding="utf-8"))
    quecital_toml.update(topic)
    with open(quecital_toml_path, "wb") as f:
        dump(quecital_toml, f)


def create_quecital_file(file_name):
    # Open the file in write mode, creating it if it doesn't exist
    with open(file_name, "wb") as f:
        dump(new_topic(), f)

    click.echo("A new quecital.toml was created.")


@quecital.command()
def start():
    # Check for quecital.toml in the cwd
    quecital_toml_path = find_quecital_toml("quecital.toml")

    if quecital_toml_path:
        quecital_data = tomllib.loads(quecital_toml_path.read_text(encoding="utf-8"))
        click.echo(
            f"""
                    Welcome to Quecital!
                    Found quecital.toml at: {quecital_toml_path}
                    What would you like to do?
            """
        )
        # Perform actions based on the existence of quecital.toml
        action = click.prompt(
            "1. Take a quiz\n2. Add a question\n3. Add a recital\n4. Start a recital\n5. Add a topic\n6. Exit",
            type=int,
        )

        match action:
            case 1:
                # Logic to start quiz
                click.echo("Starting quiz...")
                quiz.main(quecital_data)
            case 2:
                # Logic to add a question
                try:
                    while True:
                        click.echo("Adding a question...")
                        add_quiz_question.main(quecital_toml_path, quecital_data)
                        user_wants_to_add = click.confirm(
                            "Do you want to add another question?", default=True
                        )

                        if not user_wants_to_add:
                            break

                except KeyboardInterrupt:
                    click.echo("\nExiting the application.")
            case 3:
                # Logic to add a recital
                try:
                    while True:
                        click.echo("Adding a recital...")
                        add_recital.main(quecital_toml_path, quecital_data)
                        user_wants_to_add = click.confirm(
                            "Do you want to add another recital?", default=True
                        )

                        if not user_wants_to_add:
                            break

                except KeyboardInterrupt:
                    click.echo("\nExiting the application.")
            case 4:
                # Logic to start a recital
                pass
            case 5:
                # logic to add a topic to quecital.toml
                click.echo("Adding a topic to quecital.toml")
                add_new_topic(new_topic(), quecital_toml_path)
            case 6:
                click.echo("Exiting Quecital. Goodbye!")
            case _:
                click.echo("Invalid choice. Exiting.")

    else:
        click.echo("quecital.toml not found in the current working directory.")
        # Perform actions when quecital.toml is not found
        create_file = click.confirm(
            "Do you want to create a new quecital file?", default=True
        )

        if create_file:
            create_quecital_file("quecital.toml")
