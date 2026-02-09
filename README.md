# QA Automation Framework – SauceDemo

This project is a UI automation framework built using:

- Python
- Selenium WebDriver
- Pytest
- Page Object Model (POM)

## Overview

The framework automates core user flows on https://www.saucedemo.com, including:

- Valid login
- Invalid login
- Add product to cart
- Complete checkout process

The project follows Page Object Model structure to ensure maintainability and scalability.

## Tech Stack

- Python 3.x
- Selenium
- Pytest
- Chrome WebDriver

## Project Structure

qa-automation-saucedemo/
│
├── pages/           # Page Object classes
├── tests/           # Test files
├── conftest.py      # WebDriver fixture setup
├── requirements.txt
└── README.md

## How to Run

1. Clone the repository
2. Create virtual environment:
   python -m venv .venv
3. Activate it:
   source .venv/bin/activate
4. Install dependencies:
   pip install -r requirements.txt
5. Run tests:
   pytest

## Future Improvements

- Add explicit waits where needed
- Add parallel execution
- Integrate CI/CD (GitHub Actions)
- Add reporting (Allure / HTML reports)
