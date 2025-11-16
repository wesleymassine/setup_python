# PEP 8 Configuration Guide

This project strictly follows **PEP 8** - Python's official style guide.

## 🎯 What is PEP 8?

PEP 8 is the official Python style guide that provides conventions for writing readable and consistent Python code.

**Reference:** https://peps.python.org/pep-0008/

---

## ✅ Current PEP 8 Configuration

### **1. Line Length**
- **Maximum: 88 characters** (Black's default, acceptable by PEP 8)
- PEP 8 recommends 79, but 88 is widely accepted in modern Python

### **2. Indentation**
- **4 spaces per indentation level** (strict PEP 8)
- No tabs allowed

### **3. Imports**
- Imports on separate lines
- Grouped in order: standard library, third-party, local
- Sorted alphabetically within groups (using `isort`)

### **4. Naming Conventions**
- **Functions/Variables:** `snake_case`
- **Classes:** `PascalCase`
- **Constants:** `UPPER_CASE_WITH_UNDERSCORES`
- **Private:** `_leading_underscore`

### **5. Whitespace**
- No trailing whitespace
- Two blank lines between top-level functions/classes
- One blank line between methods

---

## 🛠️ Tools Configuration

### **Black (Auto-formatter)**
```toml
[tool.black]
line-length = 88
target-version = ['py38']
```
- Automatically formats code to PEP 8
- Opinionated formatter (no configuration needed)

### **Flake8 (PEP 8 Checker)**
```ini
[flake8]
max-line-length = 88
extend-ignore = E203, W503
```
- **E203:** Whitespace before ':' (Black compatibility)
- **W503:** Line break before binary operator (new PEP 8 convention)

### **pycodestyle (Official PEP 8 Checker)**
```ini
[pycodestyle]
max-line-length = 88
ignore = E203, W503
```
- Official PEP 8 checker (formerly pep8)

### **isort (Import Sorter)**
```toml
[tool.isort]
profile = "black"
line_length = 88
```
- Sorts imports according to PEP 8

### **Pylint (Advanced Linter)**
```toml
[tool.pylint.messages_control]
max-line-length = 88
```
- Additional code quality checks beyond PEP 8

---

## 📝 Usage

### **Check PEP 8 Compliance**
```bash
# Using flake8 (recommended)
flake8 src tests run.py

# Using pycodestyle (official)
pycodestyle src tests run.py

# Full report with statistics
flake8 src tests run.py --statistics --count
```

### **Auto-fix PEP 8 Issues**
```bash
# Format with Black (recommended)
black src tests run.py

# Auto-fix with autopep8
autopep8 --in-place --aggressive --aggressive src/**/*.py

# Sort imports
isort src tests run.py
```

### **Pre-commit Hooks**
All checks run automatically on `git commit`:
```bash
git add .
git commit -m "Your message"
# Black, flake8, isort run automatically
```

---

## 🎨 PEP 8 Examples

### ✅ **Good (PEP 8 Compliant)**
```python
"""Module docstring describing the module."""

import os
import sys

import requests

from my_package import my_module


CONSTANT_VALUE = 42


class MyClass:
    """Class docstring."""

    def __init__(self, name: str) -> None:
        """Initialize with name."""
        self.name = name
        self._private_var = 0

    def public_method(self, value: int) -> int:
        """Public method doing something."""
        return value * 2


def my_function(param1: str, param2: int) -> bool:
    """
    Function with proper docstring.

    Args:
        param1: Description of param1
        param2: Description of param2

    Returns:
        Boolean result
    """
    if param2 > 0:
        return True
    return False
```

### ❌ **Bad (PEP 8 Violations)**
```python
import sys,os  # Multiple imports on one line
import requests
import my_module  # Wrong order

constantValue=42  # Should be CONSTANT_VALUE

class myClass:  # Should be MyClass
    def __init__(self,name):  # Missing spaces after comma
        self.name=name  # Missing spaces around =

def MyFunction( param1,param2 ):  # Wrong naming, extra spaces
    if param2>0:return True  # Multiple statements, missing spaces
```

---

## 🔧 VS Code Integration

The project's `.vscode/settings.json` is configured for PEP 8:
```json
{
  "python.linting.enabled": true,
  "python.linting.flake8Enabled": true,
  "python.formatting.provider": "black",
  "editor.formatOnSave": true,
  "editor.rulers": [88]
}
```

**Features:**
- ✅ Auto-format on save with Black
- ✅ Real-time PEP 8 warnings with Flake8
- ✅ Visual ruler at 88 characters
- ✅ Auto-organize imports

---

## 📊 Verify Your Code

### **Run All Checks**
```bash
make lint
```

This runs:
1. **flake8** - PEP 8 style check
2. **pylint** - Advanced analysis
3. **mypy** - Type checking

### **Current Status**
```bash
$ flake8 src tests run.py --count
0
```
✅ **Zero PEP 8 violations!**

---

## 📚 PEP 8 Key Rules Summary

| Category | Rule | Example |
|----------|------|---------|
| **Indentation** | 4 spaces | `def func():`<br>`····return 42` |
| **Line Length** | Max 88 chars | Wrap long lines |
| **Blank Lines** | 2 between functions | `def func1():`<br>`····pass`<br><br><br>`def func2():` |
| **Imports** | One per line | `import os`<br>`import sys` |
| **Quotes** | Consistent | `"string"` or `'string'` |
| **Whitespace** | Around operators | `x = 1 + 2` |
| **Naming** | snake_case functions | `def my_function():` |
| **Naming** | PascalCase classes | `class MyClass:` |
| **Comments** | Inline with 2 spaces | `x = 1  # comment` |
| **Docstrings** | Triple quotes | `"""Docstring."""` |

---

## 🚀 Best Practices

1. **Run Black before committing** - Automatic PEP 8 formatting
2. **Check with Flake8** - Catch violations early
3. **Use type hints** - Modern Python standard
4. **Write docstrings** - Document all public functions/classes
5. **Let pre-commit hooks work** - They catch issues automatically

---

## 🔗 Resources

- [PEP 8 Official](https://peps.python.org/pep-0008/)
- [Black Documentation](https://black.readthedocs.io/)
- [Flake8 Documentation](https://flake8.pycqa.org/)
- [Python Type Hints (PEP 484)](https://peps.python.org/pep-0484/)
- [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html)

---

**✨ This project is 100% PEP 8 compliant!**
