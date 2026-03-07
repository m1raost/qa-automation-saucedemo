import config
from pages.inventory_page import InventoryPage
from pages.checkout_page import CheckoutPage


def test_inventory_page_loads(logged_in_driver):
    inventory_page = InventoryPage(logged_in_driver)

    assert inventory_page.get_page_title() == "Products"
    assert inventory_page.get_product_count() == 6


def test_complete_checkout_flow(logged_in_driver):
    logged_in_driver.get(config.CHECKOUT_URL)

    checkout_page = CheckoutPage(logged_in_driver)
    checkout_page.fill_checkout_form(
        config.CHECKOUT_FIRST_NAME,
        config.CHECKOUT_LAST_NAME,
        config.CHECKOUT_POSTAL_CODE,
    )
    checkout_page.continue_checkout()
    checkout_page.finish_checkout()

    assert "Thank you" in checkout_page.get_success_message()


def test_checkout_empty_form(checkout_ready_driver):
    checkout_page = CheckoutPage(checkout_ready_driver)
    checkout_page.submit_empty_form()

    assert "First Name is required" in checkout_page.get_error_message()


def test_checkout_missing_postal_code(checkout_ready_driver):
    checkout_page = CheckoutPage(checkout_ready_driver)
    checkout_page.fill_checkout_form(
        config.CHECKOUT_FIRST_NAME,
        config.CHECKOUT_LAST_NAME,
        "",
    )
    checkout_page.submit_empty_form()

    assert "Postal Code is required" in checkout_page.get_error_message()
