# Unit Tests - Projeto Python

Projeto de treinamento para desenvolvimento profissional em Python.

## 🚀 Setup do Ambiente

### Pré-requisitos
- Python 3.8+
- pyenv (recomendado)

### Instalação

1. **Clone o repositório** (se aplicável)
```bash
git clone <seu-repositorio>
cd unit_tests
```

2. **Crie o ambiente virtual**
```bash
python3 -m venv .venv
```

3. **Ative o ambiente virtual**
```bash
source .venv/bin/activate
```

4. **Instale as dependências**
```bash
# Dependências de produção
pip install -r requirements.txt

# Dependências de desenvolvimento
pip install -r requirements-dev.txt
```

5. **Configure o pre-commit**
```bash
pre-commit install
```

## 🏗️ Estrutura do Projeto

```
unit_tests/
├── .venv/                  # Ambiente virtual (não commitado)
├── src/                    # Código fonte
│   └── __init__.py
├── tests/                  # Testes unitários
│   └── __init__.py
├── run.py                  # Script principal
├── requirements.txt        # Dependências de produção
├── requirements-dev.txt    # Dependências de desenvolvimento
├── pyproject.toml         # Configuração do projeto
├── .flake8                # Configuração do Flake8
├── .pre-commit-config.yaml # Hooks do pre-commit
├── .gitignore             # Arquivos ignorados pelo Git
└── README.md              # Este arquivo
```

## 🧪 Testes

Execute os testes com:
```bash
pytest
```

Com cobertura de código:
```bash
pytest --cov=src --cov-report=html
```

## 🎨 Formatação e Linting

**Formatar código automaticamente:**
```bash
black .
```

**Verificar problemas de estilo:**
```bash
flake8 src tests
```

**Análise estática com pylint:**
```bash
pylint src
```

**Type checking com mypy:**
```bash
mypy src
```

## 🔧 Boas Práticas

1. **Sempre ative o ambiente virtual** antes de trabalhar
2. **Execute os testes** antes de commitar
3. **Use pre-commit hooks** para garantir qualidade do código
4. **Documente suas funções** com docstrings
5. **Mantenha requirements.txt atualizado**

## 📝 Desenvolvimento

Para adicionar novas dependências:
```bash
pip install <pacote>
pip freeze > requirements.txt
```
