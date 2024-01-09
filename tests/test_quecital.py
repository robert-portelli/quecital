# test_quecital.py
"""
Test module for quecital.py functionality.

This module contains unit tests for functions in the quecital.py module.

"""

# from pathlib import Path
import pytest

# from click.testing import CliRunner
from quecital.quecital import quecital


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

    # def test_find_quecital_toml_exists(temp_directory):
    """
    Test case for find_quecital_toml when quecital.toml exists.

    This function checks if find_quecital_toml correctly identifies the
    existence of quecital.toml in the specified temporary directory.

    Args:
        temp_directory (py.path.local): Pytest fixture for the temporary directory.

    """


"""     # Create quecital.toml in the temporary directory
    Path("quecital.toml").write_text("content", encoding="utf-8")

    # Check if find_quecital_toml finds quecital.toml
    expected_path = Path(temp_directory) / "quecital.toml"
    actual_path = find_quecital_toml()

    assert actual_path is not None
    assert actual_path.resolve() == expected_path.resolve() """


# def test_find_quecital_toml_not_exists(temp_directory):
"""
    Test case for find_quecital_toml when quecital.toml does not exist.

    This function checks if find_quecital_toml correctly returns None when
    quecital.toml is not found in the specified temporary directory.

    Args:
        temp_directory (py.path.local): Pytest fixture for the temporary directory.

    """
# Check if find_quecital_toml returns None when quecital.toml is not found
# assert find_quecital_toml() is None
