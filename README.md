# Python LLM Examples

A collection of Python examples for working with Large Language Models.

## Project Setup

1. Install Python using pyenv:
```bash
pyenv install 3.11.0
pyenv local 3.11.0
```

2. Create and activate a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate
```

3. Install pip-tools:
```bash
pip install pip-tools
```

4. Compile and install requirements:
```bash
pip-compile requirements.in
pip-sync requirements.txt
```

## Project Structure

```
.
├── src/                    # Source code
│   └── python_llm_examples/
├── tests/                  # Test files
├── docs/                   # Documentation
├── requirements.in         # Direct dependencies
└── requirements.txt        # Compiled dependencies (generated)
```

## Development

- Run tests: `pytest`
- Format code: `black .`
- Sort imports: `isort .`
- Lint code: `flake8`
- Type checking: `mypy .` 