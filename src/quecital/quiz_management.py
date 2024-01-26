# add_quiz_question.py
from typing import Dict, List, Optional
import click
from tomli_w import dump
from quecital.quiz import main_loop
from quecital.multiline_text_editor import get_multiline_edit


def main(quecital_toml_path, quecital_data):
    """
    Add a new question to the quiz.

    Args:
        quecital_toml_path (str): Path to the quiz TOML file.
        quecital_data (dict): Dictionary containing quiz data.
    """
    topic_question_assets = get_questions_for_topic(quecital_data)
    new_question_asset: dict = form_toml_entry()
    topic_question_assets.append(new_question_asset)
    with open(quecital_toml_path, "wb") as f:
        dump(quecital_data, f)


def get_questions_for_topic(quecital_data) -> List[Dict]:
    """
    Return the list of questions for the selected topic.

    Args:
        quecital_data (dict): Dictionary containing quiz data.

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


def form_toml_entry() -> Dict[str, str | List | Optional[str]]:
    """
    Gather information to form a new quiz entry.

    Returns:
        Dict: A dictionary representing a new quiz question.
    """
    question: str = rigid_receiver("question")

    answers: List[str] = flexible_receiver("answers")

    alternatives: List[str] = flexible_receiver("alternatives")

    hint: Optional[str] = rigid_receiver("hint")

    explanation: Optional[str] = rigid_receiver("explanation")

    return {
        "question": question,
        "answers": answers,
        "alternatives": alternatives,
        "hint": hint,
        "explanation": explanation,
    }


def rigid_receiver(config: str) -> str:
    """
    Receive input for quiz assets that don't support multiple lines.

    Args:
        config (str): Key representing the type of input.

    Returns:
        str: The received input.
    """

    configs = {
        "question": {
            "garnish": "Enter a question prompt",
        },
        "hint": {
            "garnish": "Offer a hint? - enter to skip",
        },
        "explanation": {
            "garnish": "Offer an explanation? - enter to skip",
        },
    }

    if config in configs:
        user_input: str | List = get_multiline_edit(configs[config]["garnish"])
        if isinstance(user_input, str):
            return str(user_input)
        raise TypeError("User input is not a string")
    raise KeyError("config not in configs")


def flexible_receiver(config) -> List:
    """
    Receive input for quiz assets that support multiple lines.

    Args:
        config: Key representing the type of input.

    Returns:
        List: List of received inputs.
    """
    configs: Dict[str, Dict[str, str | bool]] = {
        "answers": {
            "garnish": "Enter a correct answer",
            "helpings": "Add a second required answer for this question?",
            "default_boolean": False,
        },
        "alternatives": {
            "garnish": "Enter an alternative, i.e., an incorrect answer",
            "helpings": "Add another alternative?",
            "default_boolean": True,
        },
    }
    assets: List = []
    if config in configs:
        while True:
            user_input: str | List = get_multiline_edit(
                # str() makes the static typer chill
                str(configs[config]["garnish"])
            )
            match user_input:
                case str(user_input):
                    assets.append(user_input)
                case list(user_input):
                    assets.extend(user_input)
                case _:
                    raise TypeError("Unsupported datatype entered for answer.")

            another_helping = click.confirm(
                # str() and bool() needed to soothe the static typer
                text=str(configs[config]["helpings"]),
                default=bool(configs[config]["default_boolean"]),
            )
            if not another_helping:
                break
    return assets
