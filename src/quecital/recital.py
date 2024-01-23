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
    prompt = "\nFrom which topic will you perform a random recital\n\n"
    for index, topic in enumerate(topics, start=1):
        prompt += f"\n{index}: {topic}"
    prompt += '\n\nEnter one of the following ->'
    valid_choices = list(map(str, range(1, len(topics) + 1)))
    selected_index = click.prompt(prompt, type=click.Choice(valid_choices))
    topic = topics[int(selected_index) - 1]
    return random.choice(quecital_data[topic]["recitals"])


if __name__ == '__main__':
    quecital_path = Path("quecital.toml")
    data = tomllib.loads(quecital_path.read_text(encoding="utf-8"))
    main(data)