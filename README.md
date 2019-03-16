# flake8-fixme

[![PyPI](https://img.shields.io/pypi/v/flake8-fixme.svg)](https://pypi.python.org/pypi/flake8-fixme)
[![PyPI](https://img.shields.io/pypi/pyversions/flake8-fixme.svg)](https://pypi.python.org/pypi/flake8-fixme)
[![codecov](https://codecov.io/gh/tommilligan/flake8-fixme/branch/master/graph/badge.svg)](https://codecov.io/gh/tommilligan/flake8-fixme/branch/master)
![CircleCI branch](https://img.shields.io/circleci/project/github/tommilligan/flake8-fixme/master.svg)

Check for FIXME and other temporary comment notes.

This module provides a plugin for `flake8`, the Python code checker.

> This module was inspired by [flake8-todo](https://github.com/schlamar/flake8-todo)

## Installation

Install with pip:

```bash
pip install flake8-fixme
```

The plugin officially supports Python `>= 3.6` and `flake8 >= 3`.
You may find other Python 3 versions work as well.

## Usage

The plugin finds temporary comments you may not want to commit:

```python
def my_function():
    # FIXME actual implementation here!
    pass
```

```log
./my_file.py:2:7: T100 Fixme found (FIXME)
```

Each word has a seperate warning so you can adjust your workflow. We like to allow committing `TODO`s, but deny committing `FIXME`s.

## Changelog

### 1.0.1

#### Bugfixes

- fixed pypi packaging not picking up source files
- fixed setup.py not loading markdown readme correctly

### 1.0.0

#### Breaking changes

Upgrading to `flake8-fixme` from `flake8-todo` has the following breaking changes:

- error codes have been changed as follows:
  - `T100`: line contains `FIXME`
  - `T101`: line contains `TODO`
  - `T102`: line contains `XXX`
- a line containing multiple words will raise an error for each word
- drop support for Python `2.7`
