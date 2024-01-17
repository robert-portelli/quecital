# add_recitals.py


from tomli_w import dump
from quecital.quiz import main_loop


def main(quecital_toml_path, quecital_data):
    """


    Steps:
        1.
    """
    questions_list = path_to_list_of_dicts(quecital_data)
    new_question_dict = create_recital()
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
        question="Which topic do you want to add a recital to",
        alternatives=trivia_toml.keys(),
    )[0]
    return trivia_toml[topic_label]["recitals"]


def create_recital():
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
    prompt = input("Enter your prompt: ")
    recital = input("Enter your recital: ")
    alternatives = input("Enter one alternative at a time: ")  # TODO a string to be parsed
    hint = input("Offer a hint? -enter to skip")
    explanation = input("Offer an explanation? - enter to skip")
    return {
        "prompt": prompt,
        "recital": list([recital]),
        "alternatives": list([alternatives]),
        "hint": hint,
        "explanation": explanation,
    }
