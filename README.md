# Unit Tests - Python Project

Professional Python development training project.

## 🚀 Environment Setup

### Prerequisites
- Python 3.8+
- pyenv (recommended)

### Installation

1. **Clone the repository** (if applicable)
```bash
git clone <your-repository>
cd unit_tests
```

2. **Create virtual environment**
```bash
python3 -m venv .venv
```

3. **Activate virtual environment**
```bash
source .venv/bin/activate
```

4. **Install dependencies**
```bash
# Production dependencies
pip install -r requirements.txt

# Development dependencies
pip install -r requirements-dev.txt
```

5. **Setup pre-commit hooks**
```bash
pre-commit install
```

## 🏗️ Project Structure

```
unit_tests/
├── .venv/                  # Virtual environment (not committed)
├── src/                    # Source code
│   └── __init__.py
├── tests/                  # Unit tests
│   └── __init__.py
├── run.py                  # Main script
├── requirements.txt        # Production dependencies
├── requirements-dev.txt    # Development dependencies
├── pyproject.toml         # Project configuration
├── .flake8                # Flake8 configuration
├── .pre-commit-config.yaml # Pre-commit hooks
├── .gitignore             # Git ignored files
└── README.md              # This file
```

## 🧪 Testing

Run tests with:
```bash
pytest
```

With code coverage:
```bash
pytest --cov=src --cov-report=html
```

## 🎨 Formatting and Linting

**Auto-format code:**
```bash
black .
```

**Check style issues:**
```bash
flake8 src tests
```

**Static analysis with pylint:**
```bash
pylint src
```

**Type checking with mypy:**
```bash
mypy src
```

## 🔧 Best Practices

1. **Always activate virtual environment** before working
2. **Run tests** before committing
3. **Use pre-commit hooks** to ensure code quality
4. **Document your functions** with docstrings
5. **Keep requirements.txt updated**

## 📝 Development

To add new dependencies:
```bash
pip install <package>
pip freeze > requirements.txt
```
