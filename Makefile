dev:
	poetry run uvicorn src.api:app --log-level=info --reload

test:
	poetry run python -m pytest tests
cq:
	poetry run black .
	poetry run isort .
	poetry run flake8 .
	poetry run bandit .
	poetry run safety check
