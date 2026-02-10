from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


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

    inventory_page = InventoryPage(driver)
    inventory_page.add_backpack_to_cart()
    inventory_page.open_cart()

    cart_page = CartPage(driver)
    cart_page.click_checkout()

    checkout_page = CheckoutPage(driver)
    checkout_page.fill_checkout_form("Mira", "Test", "12345")
    checkout_page.continue_checkout()
    checkout_page.finish_checkout()

    assert "Thank you" in checkout_page.get_success_message()
