from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class CartPage(BasePage):

    CHECKOUT_BUTTON = (By.ID, "checkout")

    def click_checkout(self):
        self.click(self.CHECKOUT_BUTTON)
        self.wait.until(EC.visibility_of_element_located((By.ID, "first-name")))