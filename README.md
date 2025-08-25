# mdformat-hallmark

[![Build Status](https://github.com/calgray/mdformat-hallmark/actions/workflows/tests.yml/badge.svg?branch=master)](https://github.com/calgray/mdformat-hallmark/actions?query=workflow%3ATests+branch%3Amaster+event%3Apush)
[![codecov.io](https://codecov.io/gh/calgray/mdformat-hallmark/branch/master/graph/badge.svg)](https://codecov.io/gh/calgray/mdformat-hallmark)
[![PyPI version](https://badge.fury.io/py/mdformat-hallmark.svg)](https://badge.fury.io/py/mdformat-hallmark)

An [mdformat](https://github.com/executablebooks/mdformat) plugin for compatibility with [hallmark](https://github.com/vweevers/hallmark), [MarkdownStyleGuide](https://cirosantilli.com/markdown-style-guide) and [Common Changelog](https://common-changelog.org/) that allows both formatters and linters to simultaneously pass for quality assurance.

## Features

- `remark-preset-lint-markdown-style-guide` style compatibility.
- `hallmark` style formatting of definitions at end of the document with:
  - blank line seperators
  - keep label casing
  - sort first by semantic version labels
  - sort second by alphanumeric labels

## Install

Install with:

```sh
pip install mdformat-hallmark
```

## CLI Usage

After installing the plugin, run `mdformat` for Markdown files including Common Changelog files.

```sh
# with extension detected automatically
mdformat README.md CHANGELOG.md

# with extension explicitly required
mdformat --extensions hallmark --extensions tables README.md CHANGELOG.md
```

## Pre-Commit Usage

```yaml
repos:
  - repo: https://github.com/executablebooks/mdformat
    rev: 0.7.19
    hooks:
      - id: mdformat
        additional_dependencies:
          - mdformat-hallmark
```

for latest developement version:

```yaml
repos:
  - repo: https://github.com/calgray/mdformat-hallmark
    rev: master
    hooks:
      - id: mdformat
```

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
