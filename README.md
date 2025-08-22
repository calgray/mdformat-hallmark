# mdformat-hallmark

[![Build Status](https://github.com/calgray/mdformat-hallmark/actions/workflows/tests.yml/badge.svg?branch=master)](<https://github.com/calgray/mdformat-hallmark/actions?query=workflow%3ATests+branch%3Amaster+event%3Apush>)
[![codecov.io](https://codecov.io/gh/calgray/mdformat-hallmark/branch/main/graph/badge.svg)](https://codecov.io/gh/xarray-contrib/astropy-xarray)
[![PyPI version](https://badge.fury.io/py/mdformat-hallmark.svg)](<https://badge.fury.io/py/mdformat-hallmark>)

An [mdformat](https://github.com/executablebooks/mdformat) plugin for compatibility with [hallmark](https://github.com/vweevers/hallmark) formatted Markdown and [Common Changelog](https://common-changelog.org/).

## Development

This package utilises [flit](https://flit.readthedocs.io) as the build engine, and [tox](https://tox.readthedocs.io) for test automation.

To install these development dependencies:

```bash
pip install tox
```

To run the tests:

```bash
tox
```

and with test coverage:

```bash
tox -e py37-cov
```

The easiest way to write tests, is to edit tests/fixtures.md

To run the code formatting and style checks:

```bash
tox -e py37-pre-commit
```

or directly

```bash
pip install pre-commit
pre-commit run --all
```

To run the pre-commit hook test:

```bash
tox -e py37-hook
```

## Publish to PyPi

Either use flit directly:

```bash
pip install flit
flit publish
```

or trigger the GitHub Action job, by creating a release with a tag equal to the version, e.g. `v0.0.1`.

Note, this requires generating an API key on PyPi and adding it to the repository `Settings/Secrets`, under the name `PYPI_KEY`.

[ci-badge]: https://github.com/executablebooks/mdformat-hallmark/workflows/CI/badge.svg?branch=master
[ci-link]: https://github.com/executablebooks/mdformat/actions?query=workflow%3ACI+branch%3Amaster+event%3Apush
[cov-badge]: https://codecov.io/gh/executablebooks/mdformat-hallmark/branch/master/graph/badge.svg
[cov-link]: https://codecov.io/gh/executablebooks/mdformat-hallmark
[pypi-badge]: https://img.shields.io/pypi/v/mdformat-hallmark.svg
[pypi-link]: https://pypi.org/project/mdformat-hallmark
