"""
add_rectials.py

"""

import pathlib
import tomllib
from tomli_w import dump
from quecital.quiz import main_loop

def preprocess():
    questions_path = pathlib.Path("quecital.toml")
    trivia_toml = tomllib.loads(questions_path.read_text())
    return questions_path, trivia_toml

def main():
    """
    Main function to add a new question to the specified topic in the
        QUESTIONS.toml file.

    Steps:
        1. Get the list of existing questions for the selected topic.
        2. Create a new question dictionary.
        3. Append the new question to the list of existing questions.
        4. Update the QUESTIONS.toml file with the new data.
    """
    questions_path, trivia_toml = preprocess()
    questions_list = path_to_list_of_dicts(trivia_toml)
    new_question_dict = create_recital()
    questions_list.append(new_question_dict)
    with open(questions_path, "wb") as f:
        dump(trivia_toml, f)


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
    prompt = input("Enter your recital prompt: ")
    recital = input("Enter your recital: ")
    alternatives = input("Enter one alternative at a time: ")
    hint = input("Offer a hint? -enter to skip")
    explanation = input("Offer an explanation? - enter to skip")
    return {
        "prompt": prompt,
        "recital": list([recital]),
        "alternatives": list([alternatives]),
        "hint": hint,
        "explanation": explanation,
    }


if __name__ == "__main__":
    main()
