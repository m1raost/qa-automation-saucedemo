# QA Automation Framework – SauceDemo

This project is a UI automation framework built using:

- Python
- Selenium WebDriver
- Pytest
- Page Object Model (POM)

## Overview

The framework automates core user flows on https://www.saucedemo.com, including:

- Valid login
- Invalid login (wrong password, locked out user, empty fields)
- Access control (unauthenticated redirect)
- Inventory page content verification
- Complete checkout process
- Checkout validation (empty form, missing postal code)

The project follows Page Object Model structure to ensure maintainability and scalability.

## Tech Stack

- Python 3.x
- Selenium
- Pytest
- pytest-xdist (parallel execution)
- pytest-html (HTML reports)
- Chrome WebDriver
- GitHub Actions (CI/CD)

## Project Structure

```
qa-automation-saucedemo/
│
├── pages/                  # Page Object classes
├── tests/                  # Test files
├── .github/workflows/      # GitHub Actions CI pipeline
├── reports/                # Generated HTML reports (local, git-ignored)
├── conftest.py             # WebDriver fixture setup
├── config.py               # URLs and test data
├── requirements.txt
└── README.md
```

## How to Run

1. Clone the repository
2. Create virtual environment:
   ```
   python -m venv .venv
   ```
3. Activate it:
   ```
   source .venv/bin/activate
   ```
4. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
5. Run tests:
   ```
   pytest
   ```

Tests run in parallel automatically and generate an HTML report at `reports/report.html`.

## CI/CD

Every push to `main` triggers a GitHub Actions workflow that:
- Runs all 10 tests in parallel on Ubuntu
- Uploads the HTML report as a downloadable artifact

## Reports

After each local run, open `reports/report.html` in your browser to see results.

In GitHub Actions, download the `test-report` artifact from the Actions tab after a run completes.
