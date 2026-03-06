import config
from pages.login_page import LoginPage


def test_valid_login(driver):
    login_page = LoginPage(driver)
    login_page.open(config.BASE_URL)
    login_page.login(config.VALID_USERNAME, config.VALID_PASSWORD)

    assert "inventory" in driver.current_url


def test_invalid_login(driver):
    login_page = LoginPage(driver)
    login_page.open(config.BASE_URL)
    login_page.login(config.VALID_USERNAME, config.INVALID_PASSWORD)

    assert "Epic sadface" in login_page.get_error_message()
