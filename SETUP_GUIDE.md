# Python Professional Development Setup - macOS

## ✅ What We've Configured

### 1. **Python Environment**
- ✅ Python 3.8.9 (system version)
- ✅ Virtual environment (`.venv`) activated
- ✅ All development dependencies installed

### 2. **Project Structure**
```
unit_tests/
├── .venv/                     # Virtual environment (isolated)
├── .vscode/                   # VS Code settings
│   ├── settings.json          # Editor configuration
│   └── extensions.json        # Recommended extensions
├── src/                       # Source code
│   ├── __init__.py
│   └── calculadora.py         # Example module
├── tests/                     # Unit tests
│   ├── __init__.py
│   └── test_calculadora.py    # Example tests
├── .git/                      # Git repository
├── .gitignore                 # Files to ignore
├── .flake8                    # Linting configuration
├── .pre-commit-config.yaml    # Git hooks configuration
├── Makefile                   # Command shortcuts
├── pyproject.toml             # Project metadata & tools config
├── requirements.txt           # Production dependencies
├── requirements-dev.txt       # Development dependencies
├── README.md                  # Project documentation
└── run.py                     # Main script
```

### 3. **Development Tools**
- ✅ **pytest**: Testing framework with 100% coverage
- ✅ **black**: Code formatter (PEP 8 style, 88 chars)
- ✅ **flake8**: Linting and style checking
- ✅ **pylint**: Advanced code analysis
- ✅ **mypy**: Static type checking
- ✅ **pre-commit**: Automatic code quality checks before commits

### 4. **Git Configuration**
- ✅ Repository initialized with `main` branch
- ✅ Pre-commit hooks installed and working
- ✅ `.gitignore` configured for Python projects

---

## 🚀 Daily Workflow

### Starting Your Work Session
```bash
# Navigate to project
cd /Users/skopotech/projects/python-traning/unit_tests

# Activate virtual environment
source .venv/bin/activate

# Verify you're in the venv (prompt shows (.venv))
which python  # Should show: .venv/bin/python
```

### Running Tests
```bash
# Run all tests with coverage
make test
# or
pytest

# Run specific test file
pytest tests/test_calculadora.py

# Run tests with verbose output
pytest -v
```

### Code Quality Checks
```bash
# Format code automatically
make format
# or
black src tests run.py

# Check code style
make lint
# or
flake8 src tests

# Static analysis
pylint src

# Type checking
mypy src
```

### Making Changes
```bash
# 1. Write your code in src/
# 2. Write tests in tests/
# 3. Run tests
pytest

# 4. Format and check
black .
flake8 .

# 5. Commit (pre-commit hooks run automatically)
git add .
git commit -m "Add new feature"
```

---

## 📦 Managing Dependencies

### Adding a New Package
```bash
# Install the package
pip install requests

# Update requirements
pip freeze > requirements.txt

# Or add manually to requirements.txt
echo "requests==2.31.0" >> requirements.txt
```

### Installing Project on New Machine
```bash
# Create and activate venv
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements-dev.txt

# Install pre-commit hooks
pre-commit install
```

---

## 🛠️ Makefile Commands

```bash
make help          # Show all available commands
make install       # Install production dependencies
make install-dev   # Install development dependencies + hooks
make test          # Run tests with coverage
make lint          # Check code quality
make format        # Format code with black
make clean         # Remove temporary files
make run           # Execute main script
```

---

## ⚙️ VS Code Integration

### Installed Extensions (Recommended)
- **Python** (ms-python.python)
- **Pylance** (ms-python.vscode-pylance)
- **Black Formatter** (ms-python.black-formatter)
- **GitLens** (eamodio.gitlens)

### Configured Features
- ✅ Auto-format on save
- ✅ Auto-organize imports
- ✅ Integrated testing panel
- ✅ Flake8 linting in real-time
- ✅ Type checking with Pylance

---

## 🎯 Next Steps & Best Practices

### 1. **Upgrade Python (Recommended)**
Install `pyenv` to manage multiple Python versions:
```bash
# Install pyenv
brew install pyenv

# Add to ~/.zshrc
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
echo 'eval "$(pyenv init -)"' >> ~/.zshrc

# Restart shell
exec zsh

# Install latest Python
pyenv install 3.12.0
pyenv local 3.12.0

# Recreate venv with new Python
rm -rf .venv
python -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt
```

### 2. **Code Documentation**
Always add docstrings to functions:
```python
def my_function(param: str) -> int:
    """
    Brief description of function.

    Args:
        param: Description of parameter

    Returns:
        Description of return value

    Examples:
        >>> my_function("test")
        42
    """
    return 42
```

### 3. **Type Hints**
Use type hints for better code quality:
```python
from typing import List, Dict, Optional

def process_data(items: List[str]) -> Dict[str, int]:
    """Process items and return counts."""
    return {item: len(item) for item in items}
```

### 4. **Testing Best Practices**
- Write tests BEFORE implementation (TDD)
- Aim for 80%+ code coverage
- Test edge cases and errors
- Use descriptive test names

### 5. **Git Workflow**
```bash
# Create feature branch
git checkout -b feature/new-feature

# Make changes and commit
git add .
git commit -m "Add: new feature description"

# Push to remote (when configured)
git push origin feature/new-feature
```

### 6. **Commit Message Convention**
```
Add: new feature
Fix: bug description
Update: existing feature
Remove: deprecated code
Refactor: code improvement
Docs: documentation update
Test: add or update tests
```

---

## 🔍 Troubleshooting

### Virtual Environment Not Activating
```bash
# Ensure you're in project directory
cd /Users/skopotech/projects/python-traning/unit_tests

# Activate explicitly
source .venv/bin/activate
```

### Pre-commit Hooks Failing
```bash
# Run hooks manually to see errors
pre-commit run --all-files

# Update hooks
pre-commit autoupdate
```

### Tests Not Found
```bash
# Ensure you're in venv
which python  # Should show .venv path

# Run from project root
cd /Users/skopotech/projects/python-traning/unit_tests
pytest
```

### Import Errors in Tests
```bash
# Install project in editable mode
pip install -e .
```

---

## 📚 Resources

- **Python Style Guide**: [PEP 8](https://pep8.org/)
- **pytest Documentation**: [pytest.org](https://docs.pytest.org/)
- **Black Formatter**: [black.readthedocs.io](https://black.readthedocs.io/)
- **Type Hints**: [PEP 484](https://www.python.org/dev/peps/pep-0484/)

---

## ✨ Current Project Status

- ✅ Virtual environment configured
- ✅ All development tools installed
- ✅ Pre-commit hooks working
- ✅ Tests passing with 100% coverage
- ✅ Code formatted and linted
- ✅ Git repository initialized
- ✅ First commit completed

**You're ready to start coding professionally! 🚀**
