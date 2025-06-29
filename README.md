# Testing GitHub Actions

A simple Python project demonstrating CI/CD pipeline implementation with GitHub Actions and automated testing.

## 🚀 Features

- Basic mathematical operations (add, subtract, multiply, divide, modulus, power)
- Comprehensive unit tests with pytest
- Automated CI/CD pipeline using GitHub Actions
- Cross-platform testing support

## 📁 Project Structure

```
├── .github/workflows/
│   └── ci.yml              # GitHub Actions workflow
├── src/
│   └── mathOperation.py    # Main mathematical functions
├── tests/
│   └── test_operation.py   # Unit tests
└── README.md
```

## 🧪 Running Tests

### Locally
```bash
# Install dependencies
pip install pytest

# Run tests
python -m pytest tests/ -v
```

### GitHub Actions
Tests run automatically on:
- Push to `main` branch
- Pull requests to `main` branch

## 🛠️ Technologies Used

- **Python 3.8+**
- **pytest** for testing
- **GitHub Actions** for CI/CD
- **Ubuntu** runner environment

## ✅ Test Coverage

- Addition operations
- Subtraction operations  
- Multiplication operations
- Division operations
- Modulus operations
- Power operations

---

*This project demonstrates best practices for Python testing and continuous integration.*
