def answer() -> List:
    """Support the user submitting a prompt with
    multiple correct answers as one correct answer per line or
    one correct multiline answer.

    Multiple sequential prompts can be submitted.

    The functionality for one correct answer per line is available
    via ptk keybinding in multiline_text_editor.get_multiline_edit()
    """
    garnish = "Enter a correct answer: "
    answers = []
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
        user_input = get_multiline_edit(garnish)
        match user_input:
            case str(user_input):
                alternatives.append(user_input)
            case list(user_input):
                alternatives.extend(user_input)
            case _:
                raise TypeError("Unsupported datatype entered for answer.")

        add_another_of_the_same = click.confirm(
            "Add another alternative?", default=True
        )
        if not add_another_of_the_same:
            break
    return alternatives