# QA Automation Framework – SauceDemo

This project is a basic UI automation framework built using:

- Python
- Selenium
- Pytest
- Page Object Model (POM)

## Project Overview

The framework automates the following scenarios on https://www.saucedemo.com:

- Valid login
- Invalid login
- Add product to cart
- Complete checkout flow

## Project Structure

qa-automation-saucedemo/
│
├── pages/           # Page Object classes
├── tests/           # Test files
├── conftest.py      # Pytest fixtures (WebDriver setup)
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