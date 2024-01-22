# add_quiz_question.py
import click
from tomli_w import dump
from quecital.quiz import main_loop
from quecital.multiline_text_editor import get_multiline_edit


def main(quecital_toml_path, quecital_data):
    questions_list = path_to_list_of_dicts(quecital_data)
    new_question_dict = form_toml_entry()
    questions_list.append(new_question_dict)
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


def form_toml_entry():
    question = get_multiline_edit("Enter your question prompt: ")

    answers = answer()

    alternatives = alternative()

    hint = get_multiline_edit("Offer a hint? -enter to skip ")

    explanation = get_multiline_edit("Offer an explanation? - enter to skip ")

    return {
        "question": question,
        "answers": list(answers),
        "alternatives": list(alternatives),
        "hint": hint,
        "explanation": explanation,
    }


def answer():
    prompt = "Enter a correct answer: "
    answers = []  # to support questions with more than one required answer
    while True:
        answers.append(get_multiline_edit(prompt))
        add_another_answer = click.confirm(
            "Add a second required answer for this question?", default=False
        )
        if not add_another_answer:
            break
    return answers


def alternative():
    prompt = "Enter an alternative, i.e., an incorrect answer"
    alternatives = []
    while True:
        alternatives.append(get_multiline_edit(prompt))
        add_another_alternative = click.confirm(
            "Add another alternative?", default=True
        )
        if not add_another_alternative:
            break
    return alternatives
