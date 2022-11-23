"""
cli.py
"""

import argparse
import sys

from .main import hello

if sys.version_info < (3, 8):
    from importlib_metadata import version
else:
    from importlib.metadata import version

PKG_NAME = "skeleton"


def cli() -> None:
    """Command line interface."""
    version_number = version(PKG_NAME)
    version_string = f"{PKG_NAME} {version_number}"
    parser = argparse.ArgumentParser(
        add_help=True, description=version_string, prog=PKG_NAME
    )
    parser.add_argument(
        "-V", "--version", action="version", version=version_string
    )
    _ = parser.parse_args()
    print(version_string)
    hello()
