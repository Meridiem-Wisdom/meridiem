black:
	poetry run black .
black-check:
	poetry run black --check .
isort:
	poetry run isort .
isort-check:
	poetry run isort . --check --diff
format:
	make black
	make isort
format-check:
	make black-check
	make isort-check
