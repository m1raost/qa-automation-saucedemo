from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class CheckoutPage(BasePage):

    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    FINISH_BUTTON = (By.ID, "finish")
    SUCCESS_MESSAGE = (By.CLASS_NAME, "complete-header")

    def fill_checkout_form(self, first_name, last_name, postal_code):
        self.type(self.FIRST_NAME, first_name)
        self.type(self.LAST_NAME, last_name)
        self.type(self.POSTAL_CODE, postal_code)

    def continue_checkout(self):
        self.click(self.CONTINUE_BUTTON)

        # ✅ Wait for next step page to load
        self.wait.until(
            EC.url_contains("checkout-step-two")
        )

    def finish_checkout(self):
        self.click(self.FINISH_BUTTON)

        # ✅ Wait for confirmation page
        self.wait.until(
            EC.url_contains("checkout-complete")
        )

    def get_success_message(self):
        return self.get_text(self.SUCCESS_MESSAGE)
