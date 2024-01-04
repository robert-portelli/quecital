# quiz.py
"""
A simple command-line quiz game.

This script reads questions from a TOML file, allows the user to choose a topic,
and quizzes the user with a set number of random questions from that topic.

Requirements:
- Python 3.7 or later
- The `tomllib` library for TOML parsing

Install `tomllib` with:
$ pip install toml
"""
from string import ascii_lowercase
import random
import pathlib
import tomllib

NUM_QUESTIONS_PER_QUIZ = 5
QUESTIONS_PATH = pathlib.Path("quecital.toml")
# QUESTIONS_PATH = pathlib.Path(__file__).parent / "quecital.toml"


def main():
    """
    Main function to run the quiz game.
    """
    questions = preprocess(
        QUESTIONS_PATH,
        num_questions=NUM_QUESTIONS_PER_QUIZ
        )

    num_correct = 0
    for index_label, question in enumerate(questions, start=1):
        print(f"\nQuestion {index_label}:")
        num_correct += main_process(question)

    print(f"\nYou got {num_correct} correct out of {len(questions)} questions")


def preprocess(path, num_questions):
    """
    Preprocess questions by loading from the TOML file and selecting a topic.

    Parameters:
    - path (pathlib.Path): The path to the TOML file containing questions.
    - num_questions (int): The number of questions to select for the quiz.

    Returns:
    List[dict]: A list of selected questions.
    """
    trivia_toml = tomllib.loads(path.read_text())
    topics = {
        topic["label"]: topic["questions"] for topic in trivia_toml.values()
    }
    topic_label = main_loop(
        question="Which topic do you want to be quizzed about",
        alternatives=sorted(topics),
    )[0]

    questions = topics[topic_label]
    num_questions = min(num_questions, len(questions))
    return random.sample(questions, k=num_questions)


def main_process(question):
    """
    Process a single question and get the user's response.

    Parameters:
    - question (dict): The question dictionary.

    Returns:
    int: 1 if the answer is correct, 0 otherwise.
    """
    correct_answers = question["answers"]
    alternatives = question["answers"] + question["alternatives"]
    shuffled_alternatives = random.sample(alternatives, k=len(alternatives))

    answers = main_loop(
        question=question["question"],
        alternatives=shuffled_alternatives,
        num_choices=len(correct_answers),
        hint=question.get("hint"),
    )

    if correct := (set(answers) == set(correct_answers)):
        print("⭐ Correct! ⭐")
    else:
        # adjust error message grammar based on number of expected correct
        # answers
        is_or_are = " is" if len(correct_answers) == 1 else "s are"
        print("\n- ".join([f"No, the answer{is_or_are}:"] + correct_answers))

    # display a message after the input answer is judged
    if "explanation" in question:
        print(f"\nEXPLANATION:\n{question['explanation']}")

    # performing an action after judging answer regardless of correctness
    # means you can't return inside the if ...  else block any longer.
    return 1 if correct else 0


def main_loop(question, alternatives, num_choices=1, hint=None):
    """
    Display the question and handle the user's input.

    Parameters:
    - question (str): The question to display.
    - alternatives (List[str]): List of answer alternatives.
    - num_choices (int): Number of choices the user needs to make.
    - hint (str): Optional hint to display.

    Returns:
    List[str]: A list of user's selected choices.
    """
    print(f"{question}?")
    labeled_alternatives = dict(zip(ascii_lowercase, alternatives))
    # check if hint not None, assign a label "?" to the value "Hint"
    if hint:
        labeled_alternatives["?"] = "Hint"

    for labeled_index, alternative in labeled_alternatives.items():
        print(f"  {labeled_index}) {alternative}")

    # rerun input prompt loop until return statement reached
    while True:
        plural_s = "" if num_choices == 1 else f"s (choose {num_choices})"
        answer = input(f"\nChoice{plural_s}? ")
        answers = set(answer.replace(",", " ").split())

        # Handle hint not None and "?" given as answer,
        #  i.e user wants to see hint
        if hint and "?" in answers:
            print(f"\nHINT: {hint}")
            continue

        # Handle incorrect quantity of answers input
        if len(answers) != num_choices:
            plural_s = "" if num_choices == 1 else "s, separated by comma"
            print(f"Please answer {num_choices} alternative{plural_s}")
            continue

        # Handle incorrect character(s) given as answer
        if any(
            (invalid := answer)
            not in labeled_alternatives
            for answer in answers
        ):
            print(
                f"{invalid!r} is not a valid choice. "
                f"Please use {', '.join(labeled_alternatives)}"
            )
            continue

        return [labeled_alternatives[answer] for answer in answers]


if __name__ == "__main__":
    main()
