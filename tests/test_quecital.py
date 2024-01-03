# test_quecital.py
"""
Test module for quecital.py functionality.

This module contains unit tests for functions in the quecital.py module.

"""

from pathlib import Path
import pytest
from click.testing import CliRunner
from src.quecital.quecital import quecital, find_quecital_toml


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


def test_start_with_quecital_toml(capsys, temp_directory):
    """
    Test case for starting quecital with quecital.toml present.

    This function tests the behavior of the 'start' command when quecital.toml
    is present in the specified temporary directory.

    Args:
        capsys (_pytest.capture.CaptureFixture): Pytest fixture for capturing stdout and stderr.
        temp_directory (py.path.local): Pytest fixture for the temporary directory.

    """
    # Create quecital.toml in the temporary directory
    Path("quecital.toml").write_text("content", encoding="utf-8")

    # Run the 'start' command and check the output
    with CliRunner().isolated_filesystem():
        with temp_directory.as_cwd():
            quecital_result = CliRunner().invoke(quecital, ["start"])

    # Check the output and exit code
    assert quecital_result.exit_code == 0
    assert "Found quecital.toml at:" in quecital_result.output


def test_start_without_quecital_toml(capsys, temp_directory):
    """
    Test case for starting quecital without quecital.toml.

    This function tests the behavior of the 'start' command when quecital.toml
    is not present in the specified temporary directory.

    Args:
        capsys (_pytest.capture.CaptureFixture): Pytest fixture for capturing stdout and stderr.
        temp_directory (py.path.local): Pytest fixture for the temporary directory.

    """
    # Run the 'start' command without quecital.toml and check the output
    with CliRunner().isolated_filesystem():
        with temp_directory.as_cwd():
            quecital_result = CliRunner().invoke(quecital, ["start"])

    # Check the output and exit code
    assert quecital_result.exit_code == 0
    assert (
        "quecital.toml not found in the current working directory."
        in quecital_result.output
    )