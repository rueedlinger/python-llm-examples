.PHONY: install test format lint typecheck clean

install:
	poetry install

test:
	poetry run pytest tests/ -v

test-cov:
	poetry run pytest tests/ -v --cov=src --cov-report=term-missing

format:
	poetry run black .
	poetry run isort .

lint:
	poetry run flake8 .

typecheck:
	poetry run mypy .

check: format lint typecheck test

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	find . -type f -name "*.pyd" -delete
	find . -type f -name ".coverage" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} +
	find . -type d -name "*.egg" -exec rm -rf {} +
	find . -type d -name ".pytest_cache" -exec rm -rf {} +
	find . -type d -name ".mypy_cache" -exec rm -rf {} + 

notebook:
	poetry run jupyter lab