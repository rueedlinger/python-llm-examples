# Python LLM Examples

A collection of Python examples demonstrating various Large Language Model (LLM) applications and integrations.

## Overview

This repository contains practical examples and implementations of LLM-based applications using Python. The examples cover different use cases, architectures, and integration patterns with various LLM providers.

### Examples

#### Text-to-Text
- [LangChain with Ollama (Llama)](notebooks/LangChain_Ollama.ipynb)
- [Pydantic AI with Ollama](notebooks/PydanticAI_Ollama.ipynb)

#### Text-to-Image
- [Stable Diffusion 2 Models with Diffusers (Hugging Face)](notebooks/StableDiffusion2.ipynb)
- [Stable Diffusion 3 Models with Diffusers (Hugging Face)](notebooks/StableDiffusion3.ipynb)

#### Image-to-Text
- [LLaVA with Ollama for Image Descriptions](notebooks/LLaVA_Ollama.ipynb)



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
See [Poetry's official documentation](https://python-poetry.org/).

3. Install dependencies:
```bash
poetry install
```

4. Run Jupyter:
```bash
poetry run jupyter lab
```

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

# Run Jupyter Lab
make notebook
```