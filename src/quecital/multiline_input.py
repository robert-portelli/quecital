import click

def get_multiline_input():
    """
    Capture multiline input from the user.

    The function prompts the user to enter multiple lines, allowing them to edit
    previous lines or add new ones. Pressing Ctrl+C or entering 'done' confirms
    the input unless the user decides to finish by typing 'done' and confirming.

    Returns:
        str: A string representing the concatenated multiline input.
    """
    lines = []

    try:
        # Display initial message to the user
        click.echo("Enter multiple lines. Press Ctrl+C to exit.")

        # Main loop for capturing multiline input
        while True:
            # Display previously entered lines, if any
            if lines:
                click.echo("Previously entered lines:")
                for idx, line in enumerate(lines, start=1):
                    click.echo(f"{idx}. {line}")

                # Prompt user to edit a specific line or add a new one
                # TODO click.choice() here?
                edit_choice = input("Enter the number of a line to edit, or press Enter to add a new line ('done' to finish): ")
                if edit_choice.lower() == 'done':
                    # Break out of the loop if the user decides to finish
                    break
                elif edit_choice.isdigit() and 1 <= int(edit_choice) <= len(lines):
                    # Allow the user to edit a specific line
                    line_to_edit = int(edit_choice) - 1
                    lines[line_to_edit] = input(f"Edit line #{edit_choice}: ")
                    continue

            # If no lines or user chooses to add a new line
            line = input(f"Enter line #{len(lines) + 1} ('done' to finish): ")
            if line.lower() == 'done':
                # Use click.confirm() to confirm finishing
                if click.confirm("Do you want to finish?", default=False):
                    break
                else:
                    continue

            # Append the entered line to the list
            lines.append(line)
    except KeyboardInterrupt:
        pass  # Handle Ctrl+C to exit gracefully

    # Concatenate the lines into a single string and return
    # return '\n'.join(lines)
    return lines

if __name__ == "__main__":
    # Test the function and display the result
    multiline_input = get_multiline_input()
    click.echo("\nYou entered:")
    click.echo(multiline_input)
