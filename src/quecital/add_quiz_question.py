"""
add_questions.py

This script allows users to add new questions to a TOML file containing
trivia questions.

The questions are organized by topics, and each question is represented
as a dictionary.

Usage:
    - Run the script to add a new question to the specified topic in the
        QUESTIONS.toml file.

Dependencies:
    - pathlib: For working with file paths.
    - tomllib: For parsing and manipulating TOML data.
    - tomli_w: For writing TOML data.
    - quiz: Contains the main_loop function used for selecting the topic.

Author:
    [Your Name]
"""

import pathlib
import tomllib
from tomli_w import dump
from quecital.quiz import main_loop

QUESTIONS_PATH = pathlib.Path("quecital.toml")
TRIVIA_TOML = tomllib.loads(QUESTIONS_PATH.read_text())


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
    questions_list = path_to_list_of_dicts()
    new_question_dict = create_question()
    questions_list.append(new_question_dict)
    with open(QUESTIONS_PATH, "wb") as f:
        dump(TRIVIA_TOML, f)


def path_to_list_of_dicts():
    """
    Return the list of dictionaries representing questions for the
        selected topic.

    Returns:
        List[Dict]: A list of dictionaries where each dictionary represents
            a question.
    """
    topic_label = main_loop(
        question="Which topic do you want to add a question to",
        alternatives=TRIVIA_TOML.keys(),
    )[0]
    return TRIVIA_TOML[topic_label]["questions"]


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


if __name__ == "__main__":
    main()
