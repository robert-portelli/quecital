# multiline_recital_editor.py
"""This module provides a function for capturing multiline input from the user
using an interactive editor.
"""
import click


def get_multiline_edit(prompt, hint_shown=False):
    """
    Capture multiline input from the user using an interactive editor.

    The function opens an interactive editor (specified by the user or the
    default) for multiline input. The user can edit the content and save
    the changes.

    Args:
        prompt (str): The prompt to display to the user.
        hint_shown (bool, optional): A flag indicating whether a hint is
        shown to the user. Defaults to False.

    Returns:
        str: The user's multiline input or 'show_hint' if the user wants to
        see the hint.
             Returns an empty string if no changes were made.
    """
    # Custom marker to separate prompt text from user's input
    custom_marker = "# ---- Your Input Below ----\n"
    # Flags for hint behavior
    hide_hint = '<DELETE FOR HINT>'
    no_hint = 'Hint not provided'
    # the message displayed with the editor
    # the hint flags are included in the prompt decided by recital.py
    default_content = f"{prompt}\n\n{custom_marker}"
    # the interactive editor, TODO improve parameters
    edited_content = click.edit(
        text=default_content,
        editor=None,
    )

    # Now we start managing the hint behavior. Perform membership tests on
    # the interactive editor's output. Look for the hint flags. Hints are not
    # required -> "Hint not provided." Hints can be available to the user but
    # not viewed -> "<DELETE FOR HINT>". If the hint is requested, (TODO:
    # don't lose any work done before requesting the hint),

    # recital.py flips the hint_shown flag on this get_multiline_edit()
    # when the interactive editor senses a change and hint_shown flag is True,
    # the program finishes (return user)
    if edited_content and hint_shown is True:
        # Find the position of the custom marker and extract user's input
        marker_position = edited_content.find(custom_marker)
        user_input = edited_content[marker_position + len(custom_marker):].strip()
        return user_input

    # check if the user wants to see the hint
    # tell recital.get_attempt to attach the hint to the prompt and send back
    # "if (this is true) and (this is of value that)"
    if edited_content and hint_shown is False:
        if hide_hint not in edited_content and no_hint not in edited_content:
            return 'show_hint'
    # an attempt without viewing the hint
    if edited_content and hint_shown is False:
        if hide_hint in edited_content or no_hint in edited_content:
            # Find the position of the custom marker and extract user's input
            marker_position = edited_content.find(custom_marker)
            user_input = edited_content[marker_position + len(custom_marker):].strip()

            return user_input

    else:
        click.echo("No changes were made.")
        return ""


if __name__ == "__main__":
    # Example of using get_multiline_edit()
    code_input = get_multiline_edit("Enter your code:")

    if code_input:
        click.echo("\nYou entered:")
        for line in code_input:
            click.echo(line)
