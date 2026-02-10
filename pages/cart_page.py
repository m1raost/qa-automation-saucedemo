from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class CartPage(BasePage):

    CHECKOUT_BUTTON = (By.ID, "checkout")

    def click_checkout(self):
        # wait until we're actually on cart page
        self.wait.until(EC.url_contains("cart"))

        self.click(self.CHECKOUT_BUTTON)

        # wait until checkout page loads
        self.wait.until(EC.url_contains("checkout-step-one"))
