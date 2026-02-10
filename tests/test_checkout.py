from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_add_backpack_to_cart(driver):
    login_page = LoginPage(driver)
    login_page.open("https://www.saucedemo.com/")
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(driver)
    inventory_page.add_backpack_to_cart()

    assert inventory_page.get_cart_count() == "1"


def test_complete_checkout_flow(driver):

    login_page = LoginPage(driver)
    login_page.open("https://www.saucedemo.com/")
    login_page.login("standard_user", "secret_sauce")

    # Ensure login success
    WebDriverWait(driver, 10).until(
        EC.url_contains("inventory")
    )

    inventory_page = InventoryPage(driver)
    inventory_page.add_backpack_to_cart()

    # Ensure badge appears
    assert inventory_page.get_cart_count() == "1"

    inventory_page.open_cart()

    # Ensure cart page loaded
    WebDriverWait(driver, 10).until(
        EC.url_contains("cart")
    )

    cart_page = CartPage(driver)
    cart_page.click_checkout()

    # Ensure checkout step one loaded
    WebDriverWait(driver, 10).until(
        EC.url_contains("checkout-step-one")
    )

    checkout_page = CheckoutPage(driver)
    checkout_page.fill_checkout_form("Mira", "Test", "12345")
    checkout_page.continue_checkout()

    # Ensure step two loaded
    WebDriverWait(driver, 10).until(
        EC.url_contains("checkout-step-two")
    )

    checkout_page.finish_checkout()

    # Ensure complete page loaded
    WebDriverWait(driver, 10).until(
        EC.url_contains("checkout-complete")
    )

    assert "Thank you" in checkout_page.get_success_message()

