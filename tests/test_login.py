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


def test_locked_out_user(driver):
    login_page = LoginPage(driver)
    login_page.open(config.BASE_URL)
    login_page.login(config.LOCKED_OUT_USERNAME, config.VALID_PASSWORD)

    assert "locked out" in login_page.get_error_message()


def test_empty_username(driver):
    login_page = LoginPage(driver)
    login_page.open(config.BASE_URL)
    login_page.login("", config.VALID_PASSWORD)

    assert "Username is required" in login_page.get_error_message()


def test_empty_password(driver):
    login_page = LoginPage(driver)
    login_page.open(config.BASE_URL)
    login_page.login(config.VALID_USERNAME, "")

    assert "Password is required" in login_page.get_error_message()


def test_access_inventory_without_login(driver):
    driver.get(config.BASE_URL + "inventory.html")
    login_page = LoginPage(driver)

    assert login_page.is_on_login_page()
