code-quality:
	poetry run black .
	poetry run isort .
	poetry run flake8 .
	poetry run bandit .
	poetry run safety check
