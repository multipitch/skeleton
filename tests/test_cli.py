"""
test_cli.py
"""

import pytest

from skeleton.cli import cli


def test_cli_stdout(capsys: pytest.CaptureFixture[str]) -> None:
    """Test stdout of cli function."""
    cli()
    captured = capsys.readouterr()
    out = "skeleton 0.2.0.dev0+g52d46ec.d20221123\nhello, world!\n"
    assert captured.out == out
