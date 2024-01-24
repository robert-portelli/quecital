import click


def get_multiline_edit(prompt, hint_shown=False):
    """
    Capture multiline input from the user using an interactive editor.

    The function opens an interactive editor (specified by the user or the default)
    for multiline input. The user can edit the content and save the changes.

    Args:
        prompt (str): The prompt to display to the user.

    Returns:
        List[str]: A list of strings representing the multiline input.
    """

    #hint_marker = "<DELETE FOR HINT>"
    # Custom marker to separate prompt text from user's input
    custom_marker = "# ---- Your Input Below ----\n"

    #if hint:
    #    prompt = prompt + '\n' + hint_marker

    default_content = f"{prompt}\n\n{custom_marker}"
    hide_hint = '<DELETE FOR HINT>'
    no_hint = 'Hint not provided'

    edited_content = click.edit(
        text=default_content,
        editor=None,
    )  # Let Click choose the default editor
    # keep_open=False,  # Close the editor immediately after the user exits

    # an attempt after viewing the hint
    if edited_content and hint_shown is True:
        # Find the position of the custom marker and extract user's input
        marker_position = edited_content.find(custom_marker)
        user_input = edited_content[marker_position + len(custom_marker):].strip()
        return user_input

    # check if the user wants to see the hint
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
