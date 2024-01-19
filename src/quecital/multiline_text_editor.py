import click


def get_multiline_edit(prompt):
    """
    Capture multiline input from the user using an interactive editor.

    The function opens an interactive editor (specified by the user or the default)
    for multiline input. The user can edit the content and save the changes.

    Args:
        prompt (str): The prompt to display to the user.

    Returns:
        List[str]: A list of strings representing the multiline input.
    """
    # Custom marker to separate prompt text from user's input
    custom_marker = "# ---- Your Input Below ----\n"

    default_content = f"{prompt}\n\n{custom_marker}"

    edited_content = click.edit(
        text=default_content,
        editor=None,
    )  # Let Click choose the default editor
    # keep_open=False,  # Close the editor immediately after the user exits

    if edited_content:
        # Find the position of the custom marker and extract user's input
        marker_position = edited_content.find(custom_marker)
        user_input = edited_content[marker_position + len(custom_marker):].strip()

        # Split the user input into lines
        lines = user_input.split("\n")
        return lines
    else:
        click.echo("No changes were made.")
        return []


if __name__ == "__main__":
    # Example of using get_multiline_edit()
    code_input = get_multiline_edit("Enter your code:")

    if code_input:
        click.echo("\nYou entered:")
        for line in code_input:
            click.echo(line)
