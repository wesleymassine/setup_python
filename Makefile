.PHONY: help install install-dev test lint format clean

help:  ## Mostra esta mensagem de ajuda
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

install:  ## Instala dependências de produção
	pip install -r requirements.txt

install-dev:  ## Instala dependências de desenvolvimento
	pip install -r requirements-dev.txt
	pre-commit install

test:  ## Executa testes com cobertura
	pytest --cov=src --cov-report=term-missing --cov-report=html

lint:  ## Verifica qualidade do código
	flake8 src tests
	pylint src
	mypy src

format:  ## Formata código com black
	black src tests run.py

clean:  ## Remove arquivos temporários
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	rm -rf .pytest_cache
	rm -rf htmlcov
	rm -rf .coverage
	rm -rf *.egg-info
	rm -rf dist
	rm -rf build

run:  ## Executa o script principal
	python run.py
