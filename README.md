# 💰 Financial Calculator MLOps Lab

[![Financial Calculator - Pytest CI](https://github.com/uXmii/financial-calculator-mlops/actions/workflows/pytest_workflow.yml/badge.svg)](https://github.com/uXmii/financial-calculator-mlops/actions/workflows/pytest_workflow.yml)
[![Financial Calculator - Unittest CI](https://github.com/uXmii/financial-calculator-mlops/actions/workflows/unittest_workflow.yml/badge.svg)](https://github.com/uXmii/financial-calculator-mlops/actions/workflows/unittest_workflow.yml)

> **Enhanced MLOps Lab**: From basic arithmetic to sophisticated financial analysis

##  Project Overview

This project transforms a basic calculator into a comprehensive **Financial Calculator and Investment Analyzer**. It demonstrates MLOps best practices including automated testing, CI/CD pipelines, and proper code organization.

###  Key Features

- ** Advanced Financial Calculations**
  - Compound Interest Calculator
  - Loan Payment Calculator
  - Investment Return Analysis
  - Portfolio Value Assessment
  - Risk Assessment Metrics
  - Future Value of Annuities

- **🔧 MLOps Best Practices**
  - Comprehensive testing (pytest & unittest)
  - GitHub Actions CI/CD
  - Multiple Python version support
  - Code coverage reporting
  - Proper error handling & validation

## Project Structure

```
financial-calculator-mlops/
├── src/
│   ├── __init__.py
│   └── financial_calculator.py    # Main financial functions
├── test/
│   ├── __init__.py
│   ├── test_pytest.py            # Pytest test suite
│   └── test_unittest.py          # Unittest test suite
├── .github/
│   └── workflows/
│       ├── pytest_workflow.yml   # Pytest CI pipeline
│       └── unittest_workflow.yml # Unittest CI pipeline
├── data/
│   └── __init__.py
├── requirements.txt
├── .gitignore
└── README.md
```

##  Installation & Setup

### Prerequisites
- Python 3.8, 3.9, or 3.10
- Git

### Local Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/uXmii/financial-calculator-mlops.git
   cd financial-calculator-mlops
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   
   # Windows
   venv\Scripts\activate
   
   # Mac/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

##  Running Tests

### Using Pytest
```bash
# Run all tests with coverage
pytest --cov=src --cov-report=html -v

# Run specific test class
pytest test/test_pytest.py::TestCompoundInterest -v

# Run with XML report (for CI)
pytest --junitxml=pytest-report.xml
```

### Using Unittest
```bash
# Run all unittest tests
python -m unittest test.test_unittest -v

# Run specific test class
python -m unittest test.test_unittest.TestFinancialCalculator -v
```

## 💻 Usage Examples

### Compound Interest Calculation
```python
from src.financial_calculator import compound_interest

# Calculate compound interest: $10,000 at 5% for 10 years, compounded quarterly
result = compound_interest(10000, 0.05, 10, 4)
print(f"Final amount: ${result}")  # Final amount: $16436.19
```

### Monthly Loan Payment
```python
from src.financial_calculator import monthly_payment

# Calculate monthly payment for $200,000 mortgage at 4% for 30 years
payment = monthly_payment(200000, 0.04, 30)
print(f"Monthly payment: ${payment}")  # Monthly payment: $954.83
```

### Portfolio Analysis
```python
from src.financial_calculator import portfolio_value

investments = [
    {'amount': 10000, 'return_rate': 8.5},
    {'amount': 15000, 'return_rate': 12.0},
    {'amount': 20000, 'return_rate': 6.5}
]

portfolio = portfolio_value(investments)
print(f"Total value: ${portfolio['total_value']}")
print(f"Weighted avg return: {portfolio['weighted_avg_return']}%")
```

### Risk Assessment
```python
from src.financial_calculator import risk_assessment

# Analyze historical returns
returns = [8.5, 12.3, -2.1, 15.7, 6.8, 9.2, -1.5, 11.4]
risk_metrics = risk_assessment(returns)

print(f"Average return: {risk_metrics['mean_return']}%")
print(f"Volatility: {risk_metrics['volatility']}%")
print(f"Sharpe ratio: {risk_metrics['sharpe_ratio']}")
```

##  CI/CD Pipeline

This project uses GitHub Actions for continuous integration:

- **Multi-Python Version Testing**: Tests run on Python 3.8, 3.9, and 3.10
- **Automated Testing**: Both pytest and unittest suites run automatically
- **Code Coverage**: Coverage reports generated and uploaded
- **Artifact Upload**: Test reports saved for review

### Workflow Triggers
- Push to `main` or `develop` branches
- Pull requests to `main` branch

## Available Functions

| Function | Description | Example |
|----------|-------------|---------|
| `compound_interest()` | Calculate compound interest | `compound_interest(1000, 0.05, 5, 12)` |
| `monthly_payment()` | Calculate loan payments | `monthly_payment(200000, 0.04, 30)` |
| `investment_return()` | Calculate annualized returns | `investment_return(1000, 1500, 3)` |
| `portfolio_value()` | Analyze portfolio metrics | `portfolio_value(investments_list)` |
| `risk_assessment()` | Calculate risk metrics | `risk_assessment(returns_list)` |
| `future_value_annuity()` | Future value calculations | `future_value_annuity(500, 0.05, 20)` |

##  Key Improvements from Original Lab

1. **Enhanced Functionality**: From basic arithmetic to sophisticated financial analysis
2. **Better Testing**: Comprehensive test suites with edge cases and parametrization
3. **Modern CI/CD**: Updated GitHub Actions with matrix testing and better error handling
4. **Code Quality**: Type hints, comprehensive docstrings, and robust error handling
5. **Real-world Application**: Practical financial calculations that users actually need

##  Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

##  License

This project is part of an MLOps coursework assignment.

##  Author

**uXmii** - [GitHub Profile](https://github.com/uXmii)

---

*This project demonstrates the evolution from a simple calculator to a comprehensive financial analysis tool, showcasing MLOps best practices and real-world applicability.* 