# add_quiz_question.py
from typing import List, Optional
import click
from tomli_w import dump
from quecital.quiz import main_loop
from quecital.multiline_text_editor import get_multiline_edit


def main(quecital_toml_path, quecital_data):
    topic_question_assets = one_topics_questions(quecital_data)
    new_question_asset: dict = form_toml_entry()
    topic_question_assets.append(new_question_asset)
    with open(quecital_toml_path, "wb") as f:
        dump(quecital_data, f)


def one_topics_questions(quecital_data):
    """
    Return the list of dictionaries representing questions for the
        selected topic.

    Returns:
        List[Dict]: A list of dictionaries where each dictionary represents
            a question.
    """
    topic_label = main_loop(
        question="Which topic do you want to add a question to",
        alternatives=quecital_data.keys(),
    )[0]
    return quecital_data[topic_label]["questions"]


#  TODO handle the key error if ["questions"] not in quecital_data[topic_label]


def form_toml_entry() -> dict:
    question: str = rigid_receiver('question')

    answers: List[str] = answer()

    alternatives: List[str] = alternative()

    hint: Optional[str] = rigid_receiver('hint')

    explanation: Optional[str] = rigid_receiver('explanation')

    return {
        "question": question,
        "answers": answers,
        "alternatives": alternatives,
        "hint": hint,
        "explanation": explanation,
    }

def rigid_receiver(config: str) -> str:

    configs = {
        'question': {
            'garnish': 'Enter a question prompt',
        },
        'hint': {
            'garnish': 'Offer a hint? - enter to skip',
        },
        'explanation': {
            'garnish': 'Offer an explanation? - enter to skip',
        },
    }

    if config in configs:
        user_input = get_multiline_edit(configs[config]['garnish'])
        if isinstance(user_input, str):
            return str(user_input)
        raise TypeError("User input is not a string")
    raise KeyError("config not in configs")

def answer() -> List:
    """Support the user submitting a prompt with
    multiple correct answers as one correct answer per line or
    one correct multiline answer.

    Multiple sequential prompts can be submitted.

    The functionality for one correct answer per line is available
    via ptk keybinding in multiline_text_editor.get_multiline_edit()
    """
    garnish = "Enter a correct answer: "
    answers = []
    while True:
        user_input = get_multiline_edit(garnish)
        match user_input:
            case str(user_input):
                answers.append(user_input)
            case list(user_input):
                answers.extend(user_input)
            case _:
                raise TypeError("Unsupported datatype entered for answer.")

        add_another_of_the_same = click.confirm(
            "Add a second required answer for this question?", default=False
        )
        if not add_another_of_the_same:
            break
    return answers



def alternative() -> List:
    garnish = "Enter an alternative, i.e., an incorrect answer"
    alternatives = []
    while True:
        user_input = get_multiline_edit(garnish)
        match user_input:
            case str(user_input):
                alternatives.append(user_input)
            case list(user_input):
                alternatives.extend(user_input)
            case _:
                raise TypeError("Unsupported datatype entered for answer.")

        add_another_of_the_same = click.confirm(
            "Add another alternative?", default=True
        )
        if not add_another_of_the_same:
            break
    return alternatives
