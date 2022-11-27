.PHONY: all \
		setup \
		lint \
		unittest \
		pytest \
		run

venv/bin/activate: ## alias for virtual environment
	python3 -m venv .venv

setup_dev: ## project setup
	. .venv/bin/activate; pip install --upgrade pip
	. .venv/bin/activate; pip install wheel setuptools
	. .venv/bin/activate; pip install -r dev_requirements.txt

setup_prod: ## project setup
	. .venv/bin/activate; pip install --upgrade pip
	. .venv/bin/activate; pip install wheel setuptools
	. .venv/bin/activate; pip install -r prod_requirements.txt

lint: ## Check code quality
	. .venv/bin/activate; black ./
	. .venv/bin/activate; flake8

unittest: ## Check code quality
	. .venv/bin/activate; python -m unittest

pytest: ## Start testing with pytest
	. .venv/bin/activate; pytest tests_pytest.py

run: ## Run
	. .venv/bin/activate; python main.py
