.PHONY: black
black:
	poetry run black "${PWD}"

.PHONY: install
install:
 	brew install -U poetry && poetry install

.PHONY: update
update:
	poetry update

.PHONY: lint
lint:
	poetry run pre-commit install && poetry run pre-commit run
