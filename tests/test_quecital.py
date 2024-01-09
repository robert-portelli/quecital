# test_quecital.py
"""
Test module for quecital.py functionality.

This module contains unit tests for functions in the quecital.py module.

"""

from pathlib import Path
import pytest
#from click.testing import CliRunner
from quecital.quecital import quecital, find_quecital_toml


@pytest.fixture
def temp_directory(tmpdir):
    """
    Fixture to create a temporary directory for testing.

    Args:
        tmpdir (py.path.local): Pytest fixture for a temporary directory.

    Yields:
        py.path.local: Path to the temporary directory.
    """
    with tmpdir.as_cwd():
        yield tmpdir


def test_find_quecital_toml_exists(temp_directory):
    """
    Test case for find_quecital_toml when quecital.toml exists.

    This function checks if find_quecital_toml correctly identifies the
    existence of quecital.toml in the specified temporary directory.

    Args:
        temp_directory (py.path.local): Pytest fixture for the temporary directory.

    """
    # Create quecital.toml in the temporary directory
    Path("quecital.toml").write_text("content", encoding="utf-8")

    # Check if find_quecital_toml finds quecital.toml
    expected_path = Path(temp_directory) / "quecital.toml"
    actual_path = find_quecital_toml()

    assert actual_path is not None
    assert actual_path.resolve() == expected_path.resolve()


def test_find_quecital_toml_not_exists(temp_directory):
    """
    Test case for find_quecital_toml when quecital.toml does not exist.

    This function checks if find_quecital_toml correctly returns None when
    quecital.toml is not found in the specified temporary directory.

    Args:
        temp_directory (py.path.local): Pytest fixture for the temporary directory.

    """
    # Check if find_quecital_toml returns None when quecital.toml is not found
    assert find_quecital_toml() is None



""" # Test to ensure 'quecital start' command handles different user actions correctly
def test_start_command_actions(temp_directory):
    # Create quecital.toml in the temporary directory
    Path("quecital.toml").write_text("content", encoding='utf-8')

    # Set up CliRunner
    runner = CliRunner()

    # Define user inputs for the test
    user_inputs = [str(action) for action in [1, 2, 3, "invalid"]]

    # Use CliRunner to simulate user input during the test
    with runner.isolated_filesystem():
        with temp_directory.as_cwd():
            quecital_result = runner.invoke(quecital, ["start"], input='\n'.join(user_inputs))

    # Check the output and exit code for each action
    assert "Found quecital.toml at:" in quecital_result.output
    assert "Starting quiz..." in quecital_result.output
    assert "Adding a question..." in quecital_result.output
    assert "Exiting Quecital. Goodbye!" in quecital_result.output
    assert "Invalid choice. Exiting." in quecital_result.output

    # Ensure the exit code is 0 for all valid actions
    assert quecital_result.exit_code == 0 """
