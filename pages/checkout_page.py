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
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")

    def fill_checkout_form(self, first_name, last_name, postal_code):
        self.type(self.FIRST_NAME, first_name)
        self.type(self.LAST_NAME, last_name)
        self.type(self.POSTAL_CODE, postal_code)

    def continue_checkout(self):
        self.click(self.CONTINUE_BUTTON)
        self.wait.until(EC.visibility_of_element_located(self.FINISH_BUTTON))

    def submit_empty_form(self):
        self.click(self.CONTINUE_BUTTON)

    def get_error_message(self):
        return self.get_text(self.ERROR_MESSAGE)

    def finish_checkout(self):
        self.click(self.FINISH_BUTTON)
        self.wait.until(EC.visibility_of_element_located(self.SUCCESS_MESSAGE))

    def get_success_message(self):
        return self.get_text(self.SUCCESS_MESSAGE)
