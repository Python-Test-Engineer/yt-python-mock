"""Test File Reading"""

from unittest.mock import Mock, MagicMock
from rich.console import Console

console = Console()
import pytest
from linereader import read_from_file
from pytest import raises

# console.print(globals())


# works with Mock rather than MagicMock in original example
@pytest.fixture()
def mock_open_fixture(monkeypatch):
    """Monkeypatch"""
    mock_file = Mock()
    mock_file.readline = Mock()  # optional
    mock_file.readline.return_value = "test line"
    mock_open = Mock(return_value=mock_file)
    monkeypatch.setattr("builtins.open", mock_open)
    return mock_open


def test_returns_correct_string(mock_open_fixture, monkeypatch):
    """Test"""
    mock_exists = Mock(return_value=True)
    monkeypatch.setattr("os.path.exists", mock_exists)
    result = read_from_file("mocked_file.txt")
    mock_open_fixture.assert_called_once_with("mocked_file.txt", "r", encoding="utf-8")
    assert result == "test line"


def test_throws_exception_with_bad_file(mock_open_fixture, monkeypatch):
    """test"""
    mock_exists = Mock(return_value=False)
    monkeypatch.setattr("os.path.exists", mock_exists)
    with raises(Exception):
        result = read_from_file("mocked_file.txt")
        return result
