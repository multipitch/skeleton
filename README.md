[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
![GitHub](https://img.shields.io/github/license/multipitch/skeleton)
![GitHub release (latest SemVer)](https://img.shields.io/github/v/release/multipitch/skeleton)

# skeleton

An example project layout.

## Build

Assumes you have the following packages and  their dependencies installed and correctly configured
- python
- pyenv

```
$ git clone https://github.com/multipitch/skeleton.git
$ cd skeleton
$ SKELETON_PY_VERSION=3.10 # pick a valid version
$ pyenv install --skip-existing $SKELETON_PY_VERSION
$ pyenv local $SKELETON_PY_VERSION
$ python -m venv venv
$ . venv/bin/activate
$ python -m pip install build
$ python -m build
```
