import click
from prompt_toolkit import prompt
from prompt_toolkit.keys import Keys
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.history import InMemoryHistory
from prompt_toolkit.styles import Style


# Constants
INPUT_BELOW_MARKER = "# ---- Your Input Below ----\n"


def get_default_content(garnish):
    header = f"{garnish}\n\n{INPUT_BELOW_MARKER}"
    return header


def extract_user_input(user_input):
    below_marker_position = user_input.find(INPUT_BELOW_MARKER)

    if below_marker_position != -1:
        return user_input[below_marker_position + len(INPUT_BELOW_MARKER) :].strip()
    else:
        click.echo("No changes were made.")
        return ""


def bottom_toolbar():
    # use a list of style/text tuples
    return [
        ("class:bottom-toolbar-translucent", ""),
        ("class:bottom-toolbar-opaque", "\n Ctrl+C to quit, alt+enter to proceed "),
    ]


def get_multiline_edit(garnish):
    default_content = get_default_content(garnish)

    history = InMemoryHistory()

    style = Style.from_dict(
        {
            "bottom-toolbar-translucent": "#ffffff bg:#444400",
            "bottom-toolbar-opaque": "#ffffff bg:#333333",
        }
    )
    try:
        user_input = prompt(
            default=default_content,
            multiline=True,
            history=history,
            bottom_toolbar=bottom_toolbar,
            style=style,
        )
    except (EOFError, KeyboardInterrupt):
        user_input = ""

    return extract_user_input(user_input)


if __name__ == "__main__":
    code_input = get_multiline_edit("Enter your code:")

    if code_input:
        click.echo("\nYou entered:")
        click.echo(code_input)
    else:
        click.echo("\nNo input received.")
