"""
cli.py
"""

import argparse
from importlib.metadata import version

from .main import hello


def cli() -> None:
    """Command line interface."""
    pkg_name = "skeleton"
    version_number = version(pkg_name)
    version_string = f"{pkg_name} {version_number}"
    parser = argparse.ArgumentParser(add_help=True, description=version_string)
    parser.add_argument(
        "-v", "--version", action="version", version=version_string
    )
    _ = parser.parse_args()
    print(version_string)
    hello()
