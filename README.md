<div align="center">
  <h1>def_result</h1>
  <br />
  <a href="#getting-started"><strong>Getting Started »</strong></a>
  <br />
  <br />
  <a href="https://github.com/Payadel/def_result/issues/new?assignees=&labels=scope-bug&template=BUG_REPORT.md&title=bug%3A+">Report a Bug</a>
  ·
  <a href="https://github.com/Payadel/def_result/issues/new?assignees=&labels=scope-enhancement&template=FEATURE_REQUEST.md&title=feat%3A+">Request a Feature</a>
  .
  <a href="https://github.com/Payadel/def_result/issues/new?assignees=&labels=help-wanted&template=SUPPORT_QUESTION.md&title=support%3A+">Ask a Question</a>
</div>

<div align="center">
<br />

[![code with love by Payadel](https://img.shields.io/badge/%3C%2F%3E%20with%20%E2%99%A5%20by-Payadel-ff1414.svg?style=flat-square)](https://github.com/Payadel)

![GitHub](https://img.shields.io/github/license/Payadel/def_result)
[![Pull Requests welcome](https://img.shields.io/badge/PRs-welcome-ff69b4.svg?style=flat-square)](https://github.com/Payadel/def_result/issues?q=is%3Aissue+is%3Aopen)
[![PyPI Project Version][pypi-image]][pypi-project-url]

</div>

<details>
<summary>Table of Contents</summary>

- [About](#about)
    - [Purpose](#Purpose)
    - [Motivation](#Motivation)
    - [What problems are solved?](#what-problems-are-solved)
- [Getting Started](#getting-started)
- [Usage](#usage)
    - [Documentation](#documentation)
- [CHANGELOG](#changelog)
- [Features](#features)
- [Roadmap](#roadmap)
- [Support](#support)
- [FAQ](#faq)
- [Project assistance](#project-assistance)
- [Contributing](#contributing)
- [Authors & contributors](#authors--contributors)
- [Security](#security)
- [License](#license)

</details>

## About

`def_result` is a Python library for working with the results of a function to solve problem of **managing errors**.

It provides a simple way to handle and manipulate the return values of functions, with built-in support for error
handling and more.

### Purpose

`def_result` is a functional error handling library.

In functional programming, it is not always appropriate to use traditional `try-catch` blocks as they can lead to code
that is difficult to read, understand, and maintain.

The purpose of Functional Error Handling Libraries is to provide developers with a set of abstractions and tools for
managing errors in a functional way.

The goal of this library is to make error handling m**ore explicit, composable, and testable**. By using functional
error handling libraries, developers can write code that is **more robust, maintainable, and expressive**.

### Motivation

The motivation behind this library is the desire to write code that is more reliable, easier to understand, and less
prone to errors. In many cases, functional programming languages provide built-in abstractions for handling errors.
However, for languages that do not have built-in support for functional error handling, libraries like this can provide
a useful alternative.

### What problems are solved?

This library can solve several problems, including:

- Ensuring that error handling is consistent across an application.
- Making it easier to test error handling code.
- Making error handling code more readable and maintainable.
- Encouraging developers to handle errors in a more functional way, which can lead to more reliable and robust code.

By improving the way that developers handle errors, this library can make the lives of their audience easier. Developers
can spend less time debugging and more time writing code that adds value to their organization. Additionally, by using
functional programming concepts, developers can write code that is easier to reason about and understand, which can lead
to faster development cycles and better quality code.

## Getting Started

`pip install def_result`

## Usage

### Sample 1: use decorator for pure functions

In this example, def_result is used as a decorator to wrap the `divide_numbers` method.

```python
from def_result import def_result


@def_result
def divide_numbers(a: int, b: int):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


result = divide_numbers(10, 0)

if result.success:
    print(f"Operation was successful: {result.value}")
else:
    print(f"Operation failed: {str(result.detail)}")
```

### Sample 2: use `Result` in function

```python
from def_result import def_result


def divide_numbers(a: int, b: int):
    if b == 0:
        Result.fail(ValidationError(message="Cannot divide by zero"))
    return Result.ok(a / b)


result = divide_numbers(10, 0)

if result.success:
    print(f"Operation was successful: {result.value}")
else:
    print(f"Operation failed: {str(result.detail)}")
```

### Documentation

[Documentation](https://linktodocumentation)

## CHANGELOG

Please see the [CHANGELOG](CHANGELOG.md) file.

## Features

- **Easy to use:** `def_result` is designed to be simple and easy to use, with a minimal API and clear documentation.
- **Compatibility with existing code:** def_result can be easily added to existing codebases without the need for major
  refactoring.
- **Optional error handling:** You can choose to ignore the error value returned by the function, in which case the
  calling code will simply receive the result value.

## Roadmap

See the [open issues](https://github.com/Payadel/def_result/issues) for a list of proposed features (and known issues).

- [Top Feature Requests](https://github.com/Payadel/def_result/issues?q=label%3Ascope-enhancement+is%3Aopen+sort%3Areactions-%2B1-desc) (
  Add your votes using the 👍 reaction)
- [Top Bugs](https://github.com/Payadel/def_result/issues?q=is%3Aissue+is%3Aopen+label%3Ascope-bug+sort%3Areactions-%2B1-desc) (
  Add your votes using the 👍 reaction)
- [Newest Bugs](https://github.com/Payadel/def_result/issues?q=is%3Aopen+is%3Aissue+label%3Ascope-bug)

## Support

Reach out to the maintainers at one of the following places:

- [GitHub issues](https://github.com/Payadel/def_result/issues/new?assignees=&labels=question&template=SUPPORT_QUESTION.md&title=support%3A+)

## FAQ

#### Do I need to rewrite all the functions in a new way?

not necessarily. By using decorator, you can convert the output of old functions to `Result`. In this method, your code
is wrap in a `try-except` block and the final output is converted to Result.

#### I want all function exceptions to be managed.

By using decorator, your code is wrap in a `try-except` block and the final output is converted to Result. With this
method, all function exceptions are managed.

## Project assistance

If you want to say **thank you** or/and support active development of `def_result`:

- Add a [GitHub Star](https://github.com/Payadel/def_result) to the project.
- Write interesting articles about the project on [Dev.to](https://dev.to/), [Medium](https://medium.com/) or your
  personal blog.

Together, we can make `def_result` **better**!

## Contributing

First off, thanks for taking the time to contribute! Contributions are what make the free/open-source community such an
amazing place to learn, inspire, and create. Any contributions you make will benefit everybody else and are **greatly
appreciated**.

Please read [our contribution guidelines](docs/CONTRIBUTING.md), and thank you for being involved!

## Authors & contributors

The original setup of this repository is by [Payadel](https://github.com/Payadel).

For a full list of all authors and contributors,
see [the contributors page](https://github.com/Payadel/def_result/contributors).

## Security

`def_result` follows good practices of security, but 100% security cannot be assured. `def_result` is provided **"as
is"** without any **warranty**.

_For more information and to report security issues, please refer to our [security documentation](docs/SECURITY.md)._

## License

This project is licensed under the **GPLv3**.

See [LICENSE](LICENSE) for more information.


<!-- Badges: -->

[pypi-project-url]: https://pypi.org/project/def_result/
