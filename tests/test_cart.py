import config
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


def test_add_item_updates_cart_badge(logged_in_driver):
    inventory_page = InventoryPage(logged_in_driver)
    inventory_page.add_first_item_to_cart()

    assert inventory_page.get_cart_badge_count() == 1


def test_cart_shows_added_item(cart_with_item_driver):
    cart_page = CartPage(cart_with_item_driver)

    assert cart_page.get_item_count() == 1


def test_cart_to_checkout_navigation(cart_with_item_driver):
    cart_page = CartPage(cart_with_item_driver)
    cart_page.click_checkout()

    assert "checkout-step-one" in cart_with_item_driver.current_url


def test_full_checkout_from_cart(cart_with_item_driver):
    cart_page = CartPage(cart_with_item_driver)
    cart_page.click_checkout()

    checkout_page = CheckoutPage(cart_with_item_driver)
    checkout_page.fill_checkout_form(
        config.CHECKOUT_FIRST_NAME,
        config.CHECKOUT_LAST_NAME,
        config.CHECKOUT_POSTAL_CODE,
    )
    checkout_page.continue_checkout()
    checkout_page.finish_checkout()

    assert "Thank you" in checkout_page.get_success_message()
