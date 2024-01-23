import click
from pathlib import Path
import tomllib
import random


def main(data):
    assets = preprocess(data)
    attempt = "Not yet implemented. Coming never"
    display = f"\nThe answer is:\n{assets['answers']}\n\nYour attempt was:\n{attempt}"
    if "explanation" in assets and assets["explanation"]:
        display += f"\n{assets['explanation']}"
    click.echo(display)


def preprocess(quecital_data):
    topics = list(quecital_data.keys())
    topic_label = click.prompt(
        "From which topic will you perform a random recital\n\n",
        type=click.Choice(topics),
        show_choices=True,
    )
    return random.choice(quecital_data[topic_label]["recitals"])

if __name__ == '__main__':
    quecital_path = Path("quecital.toml")
    data = tomllib.loads(quecital_path.read_text(encoding="utf-8"))
    main(data)