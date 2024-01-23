# quiz.py
from string import ascii_lowercase
import random

from pathlib import Path
import tomllib
from quecital.multiline_text_editor import get_multiline_edit
path = Path('quecital.toml')
data = tomllib.loads(path.read_text(encoding='utf-8'))
NUM_QUESTIONS_PER_QUIZ = 5


def main(quecital_data):
    """
    Main function to run the quiz game.
    """
    choice = choose_recital(quecital_data)
    prompt = choice['question']
    attempt = get_multiline_edit(prompt, hint=True) if choice['hint'] else get_multiline_edit(prompt)
    attempt_with_hint = check_attempt_for_absent_hint_marker(choice, attempt, )
    answer = choice['answers']
    if not attempt_with_hint:
        print(answer, '\n', f"attempt without hint{attempt}")
    else:
        print(answer, '\n', f"attempt with hint{attempt}")


def check_attempt_for_absent_hint_marker(choice, attempt):
    if attempt == 'show_hint':
        prompt = choice['question'] + '\n' + choice['hint']
        return get_multiline_edit(prompt, hint=False)
    else:
        return None


def choose_recital(quecital_data):
    topic_label = main_loop(
        question="From which topic will you perform a random recital",
        alternatives=quecital_data.keys(),
    )[0]
    return random.choice(quecital_data[topic_label]["recitals"])


def main_process(question):
    """
    Process a single question and get the user's response.

    Parameters:
    - question (dict): The question dictionary.

    Returns:
    int: 1 if the answer is correct, 0 otherwise.
    """
    correct_answers = question["answers"]
    #alternatives = question["answers"] + question["alternatives"]
    #shuffled_alternatives = random.sample(alternatives, k=len(alternatives))

    answers = main_loop(
        question=question["recital"],
        #alternatives=shuffled_alternatives,
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
        if any((invalid := answer) not in labeled_alternatives for answer in answers):
            print(
                f"{invalid!r} is not a valid choice. "
                f"Please use {', '.join(labeled_alternatives)}"
            )
            continue

        return [labeled_alternatives[answer] for answer in answers]