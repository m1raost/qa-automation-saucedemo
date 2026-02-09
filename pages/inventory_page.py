from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class InventoryPage(BasePage):

    ADD_BACKPACK_BUTTON = (By.ID, "add-to-cart-sauce-labs-backpack")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")

    def add_backpack_to_cart(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.ADD_BACKPACK_BUTTON)
        )
        self.driver.find_element(*self.ADD_BACKPACK_BUTTON).click()

    def get_cart_count(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.CART_BADGE)
        ).text
