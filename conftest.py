import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
import config


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


@pytest.fixture
def logged_in_driver(driver):
    login_page = LoginPage(driver)
    login_page.open(config.BASE_URL)
    login_page.login(config.VALID_USERNAME, config.VALID_PASSWORD)
    yield driver


@pytest.fixture
def checkout_ready_driver(logged_in_driver):
    inventory_page = InventoryPage(logged_in_driver)
    inventory_page.add_backpack_to_cart()
    inventory_page.open_cart()

    cart_page = CartPage(logged_in_driver)
    cart_page.click_checkout()

    yield logged_in_driver
