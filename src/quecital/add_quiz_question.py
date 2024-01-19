# add_quiz_question.py
import click
from tomli_w import dump
#from quecital.quiz import main_loop
import importlib



def main(quecital_toml_path, quecital_data):
    questions_list = path_to_list_of_dicts(quecital_data)
    new_question_dict = create_question()
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
    quiz_module = importlib.import_module('quecital.quiz')
    main_loop = getattr(quiz_module, 'main_loop')
    topic_label = main_loop(
        question="Which topic do you want to add a question to",
        alternatives=quecital_data.keys(),
    )[0]
    return quecital_data[topic_label]["questions"]
#  TODO handle the key error if ["questions"] not in quecital_data[topic_label]


def create_question():
    """
    Create a dictionary representing a new trivia question.

    Returns:
        Dict: A dictionary with the following items:
            - 'question': str,
            - 'answers': List,
            - 'alternatives': List,
            - 'hint': None,
            - 'explanation': None
    """

    multiline_text_editor = importlib.import_module('quecital.multiline_text_editor')
    editor_multiline = getattr(multiline_text_editor, 'get_multiline_edit')

    question = editor_multiline("Enter your question prompt: ")

    answers = editor_multiline("Enter one correct answer at a time: ")

    alternatives = editor_multiline("Enter one alternative at a time: ")

    hint = editor_multiline("Offer a hint? -enter to skip ")

    explanation = editor_multiline("Offer an explanation? - enter to skip ")
    return {
        "question": question,
        "answers": list([answers]),
        "alternatives": list([alternatives]),
        "hint": hint,
        "explanation": explanation,
    }
