from typing import Union, List
import click
from prompt_toolkit import prompt
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.history import InMemoryHistory
from prompt_toolkit.styles import Style


# Constants
INPUT_BELOW_MARKER = "# ---- Your Input Below ----\n"
MULTI_FLAG = "MULTI_FLAG"


def get_default_content(garnish):
    header = f"{garnish}\n\n{INPUT_BELOW_MARKER}"
    return header


def extract_user_input(user_input: str, multi_flag=False) -> str | List[str]:
    below_marker_position = user_input.find(INPUT_BELOW_MARKER)

    # user_input is one multiline asset from one window
    # return a string
    if multi_flag is False and below_marker_position != -1:
        return user_input[below_marker_position + len(INPUT_BELOW_MARKER) :].strip()

    # user_input are multiple single line assets from one window
    # return a list of strings
    if multi_flag is True and below_marker_position != -1:
        user_input = user_input[
            below_marker_position + len(INPUT_BELOW_MARKER) :
        ].strip()
        return user_input.split("\n")

    click.echo("No changes were made.")
    return ""


def bottom_toolbar():
    # use a list of style/text tuples
    return [
        ("class:bottom-toolbar-translucent", ""),
        ("class:bottom-toolbar-opaque", "\n Ctrl+C to quit, alt+enter to proceed "),
        ("class:bottom-toolbar-opaque", "F2 to save one as one asset entry per line"),
    ]


def inject_multi_flag(prompt_output):
    return MULTI_FLAG + prompt_output


def get_multiline_edit(garnish: str) -> str | List[str]:
    default_content = get_default_content(garnish)

    history = InMemoryHistory()

    style = Style.from_dict(
        {
            "bottom-toolbar-translucent": "#ffffff bg:#444400",
            "bottom-toolbar-opaque": "#ffffff bg:#333333",
        }
    )
    kb = KeyBindings()

    @kb.add("f2")
    def _(event):
        event.app.exit(inject_multi_flag(event.app.current_buffer.text))

    try:
        user_input: str = prompt(
            default=default_content,
            multiline=True,
            history=history,
            bottom_toolbar=bottom_toolbar,
            style=style,
            key_bindings=kb,
        )
    except (EOFError, KeyboardInterrupt):
        user_input = ""

    if MULTI_FLAG in user_input:
        return extract_user_input(user_input, multi_flag=True)
    return extract_user_input(user_input)


if __name__ == "__main__":
    code_input = get_multiline_edit("Enter your code:")

    if code_input:
        click.echo("\nYou entered:")
        click.echo(code_input)
    else:
        click.echo("\nNo input received.")
