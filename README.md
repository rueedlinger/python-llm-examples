# Python LLM Examples

A collection of Python examples demonstrating various Large Language Model (LLM) applications and integrations.

## Overview

This repository contains practical examples and implementations of LLM-based applications using Python. The examples cover different use cases, architectures, and integration patterns with various LLM providers.

## Prerequisites

- Python 3.11 or higher
- Poetry for dependency management

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/python-llm-examples.git
cd python-llm-examples
```

2. Install Poetry (if not already installed):
see https://python-poetry.org/

3. Install dependencies:
```bash
make install
```

## Development

### Code Quality Tools

The project uses several tools to maintain code quality:

- **black**: Code formatting
- **isort**: Import sorting
- **flake8**: Linting
- **mypy**: Static type checking
- **pytest**: Testing framework

### Make Commands

The project includes a Makefile with common development commands:

```bash
# Install dependencies
make install

# Run tests
make test

# Run tests with coverage
make test-cov

# Format code
make format

# Run linter
make lint

# Run type checker
make typecheck

# Run all checks (format, lint, typecheck, test)
make check

# Clean up cache files and build artifacts
make clean
```

## Project Structure

```
python-llm-examples/
├── src/               # Source code
├── tests/            # Test files
├── pyproject.toml    # Project configuration
├── Makefile         # Development commands
└── README.md        # This file
```

## Examples

tbd
