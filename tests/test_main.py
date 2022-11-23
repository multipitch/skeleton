"""
test_main.py
"""

import pytest

from skeleton.main import hello


def test_hello_stout(capsys: pytest.CaptureFixture[str]) -> None:
    """Test output of hello function."""
    hello()
    captured = capsys.readouterr()
    out = "hello, world!\n"
    assert captured.out == out
