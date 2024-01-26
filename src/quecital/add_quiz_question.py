# add_quiz_question.py
from typing import List, Optional
import click
from tomli_w import dump
from quecital.quiz import main_loop
from quecital.multiline_text_editor import get_multiline_edit


def main(quecital_toml_path, quecital_data):
    topic_question_assets = path_to_list_of_dicts(quecital_data)
    new_quiz_asset: dict = form_toml_entry()
    topic_question_assets.append(new_quiz_asset)
    with open(quecital_toml_path, "wb") as f:
        dump(quecital_data, f)


def path_to_list_of_dicts(quecital_data):
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
    question: str = get_multiline_edit("Enter your question prompt: ")

    answers: List[str] = answer()

    alternatives: List[str] = alternative()

    hint: Optional[str] = get_multiline_edit("Offer a hint? -enter to skip ")

    explanation: Optional[str] = get_multiline_edit(
        "Offer an explanation? - enter to skip "
    )

    return {
        "question": question,
        "answers": answers,
        "alternatives": list(alternatives),
        "hint": hint,
        "explanation": explanation,
    }


def answer() -> List:
    garnish = "Enter a correct answer: "
    answers = []  # to support questions with more than one required answer
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
        alternatives.append(get_multiline_edit(garnish))
        add_another_alternative = click.confirm(
            "Add another alternative?", default=True
        )
        if not add_another_alternative:
            break
    return alternatives
