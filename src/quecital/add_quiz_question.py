# add_quiz_question.py

from tomli_w import dump
from quecital.quiz import main_loop



def main(quecital_toml_path, quecital_data):
    questions_list = path_to_list_of_dicts(quecital_data)
    new_question_dict = create_question()
    questions_list.append(new_question_dict)
    with open(quecital_toml_path, "wb") as f:
        dump(quecital_data, f)


def path_to_list_of_dicts(trivia_toml):
    """
    Return the list of dictionaries representing questions for the
        selected topic.

    Returns:
        List[Dict]: A list of dictionaries where each dictionary represents
            a question.
    """
    topic_label = main_loop(
        question="Which topic do you want to add a question to",
        alternatives=trivia_toml.keys(),
    )[0]
    return trivia_toml[topic_label]["questions"]
#  TODO handle the key error if ["questions"] not in trivia_toml[topic_label]


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
    question = input("Enter your question prompt: ")
    answers = input("Enter one correct answer at a time: ")
    alternatives = input("Enter one alternative at a time: ")
    hint = input("Offer a hint? -enter to skip")
    explanation = input("Offer an explanation? - enter to skip")
    return {
        "question": question,
        "answers": list([answers]),
        "alternatives": list([alternatives]),
        "hint": hint,
        "explanation": explanation,
    }
