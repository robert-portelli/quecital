import click
from pathlib import Path
import tomllib
import random
from quecital.multiline_text_editor import get_multiline_edit


def main(data):
    assets = preprocess(data)
    attempt = get_attempt(assets)
    display = f"\
        \nThe prompt was:\
        \n{assets['question']}\n\
        \nThe attempt was:\
        \n{attempt}\n\
        \nThe correct answer is:\
        \n{assets['answers']}\n"
    if "explanation" in assets and assets["explanation"]:
        display += f"\n\nExplanation: {assets['explanation']}"
    click.echo(display)

def compose_prompt(assets, show_hint=False):
    hint = "Hint not provided"
    if "hint" in assets and assets["hint"] and show_hint is False:
        hint = "<DELETE FOR HINT>"
    if "hint" in assets and assets["hint"] and show_hint is True:
        hint = assets['hint']
    prompt = f'The prompt is:\n\n{assets["question"]}\n\n{hint}'
    return prompt


def get_attempt(assets):
    prompt = compose_prompt(assets)
    attempt = get_multiline_edit(prompt)
    if attempt == 'show_hint':
        prompt = compose_prompt(assets, show_hint=True)
        attempt = get_multiline_edit(prompt)

    return attempt


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