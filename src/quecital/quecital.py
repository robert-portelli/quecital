# quecital.py

from pathlib import Path
import click
import tomllib
from quecital import quiz, add_quiz_question, add_recital
from tomli_w import dump

@click.group()
def quecital():
    """Quecital - Your Quiz App."""
    pass


def find_quecital_toml():
    """Find quecital.toml in the current working directory."""
    quecital_path = Path("quecital.toml")
    return quecital_path if quecital_path.is_file() else None

def new_topic():
    topic = input("Enter topic name: ").lower()
    label = topic.capitalize()
    return {
        topic: {
            'label': label,
            'questions': [],
            'recitals': []
            }
        }

def add_new_topic(topic):
    questions_path = Path("quecital.toml")
    trivia_toml = tomllib.loads(questions_path.read_text())
    trivia_toml.update(topic)
    with open(questions_path, "wb") as f:
        dump(trivia_toml, f)




def create_quecital_file():
    file_name = 'quecital.toml'
    # Open the file in write mode, creating it if it doesn't exist
    with open(file_name, 'wb') as f:
        dump(new_topic(), f)

    click.echo(f"A new quecital.toml was created.")


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
            "1. Take a quiz\n2. Add a question\n3. Add a recital\n4. Start a recital\n5. Add a topic\n6. Exit", type=int)

        match action:
            case 1:
                # Logic to start quiz
                click.echo("Starting quiz...")
                quiz.main()
            case 2:
                # Logic to add a question
                click.echo("Adding a question...")
                add_quiz_question.main()
            case 3:
                # Logic to add a recital
                click.echo("Adding a recital...")
                add_recital.main()
            case 4:
                # Logic to start a recital
                pass
            case 5:
                # logic to add a topic to quecital.toml
                click.echo("Adding a topic to quecital.toml")
                add_new_topic(new_topic())
            case 6:
                click.echo("Exiting Quecital. Goodbye!")
            case _:
                click.echo("Invalid choice. Exiting.")

    else:
        click.echo("quecital.toml not found in the current working directory.")
        # Perform actions when quecital.toml is not found
        create_file = click.confirm("Do you want to create a new quiz file?", default=True)

        if create_file:
            create_quecital_file()
