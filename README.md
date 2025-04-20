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

### 1. LangChain with Ollama
This example demonstrates how to use LangChain with Ollama to run different LLM models locally. It supports various Llama models including llama3.2:1b, llama3.2:3b, and llama3.3.

To run this example:
```bash
poetry run python src/examples/example_LangChain_Ollama.py
```

Prerequisites:
- Ollama must be installed and running locally
- The desired Llama models must be pulled using Ollama (e.g., `ollama pull llama3.3`)

Jupyter Notebook:
- [LangChain with Ollama](notebooks/LangChain_Ollama.ipynb)

### 2. Stable Diffusion 3 Image Generation
This example shows how to generate images using Stable Diffusion 3. It supports both the medium and large models.

To run this example:
```bash
poetry run python src/examples/example_StableDiffusion3.py
```

Prerequisites:
- PyTorch installed with CUDA or MPS support
- Sufficient GPU memory (recommended 8GB+ for medium model, 16GB+ for large model)
- The first run will download the model weights (several GB)

The example will generate images using both the medium and large models and save them as PNG files.

Jupyter Notebook:
- [Stable Diffusion 3 Models with Diffusers (Hugging Face)](notebooks/StableDiffusion3.ipynb)
