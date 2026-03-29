from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class CartPage(BasePage):

    CHECKOUT_BUTTON = (By.ID, "checkout")
    CART_ITEM = (By.CLASS_NAME, "cart_item")
    CART_ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")

    def click_checkout(self):
        self.js_click(self.CHECKOUT_BUTTON)
        self.wait.until(EC.visibility_of_element_located((By.ID, "first-name")))

    def get_item_count(self):
        self.wait.until(EC.visibility_of_element_located(self.CART_ITEM))
        return len(self.driver.find_elements(*self.CART_ITEM))

    def get_item_names(self):
        self.wait.until(EC.visibility_of_element_located(self.CART_ITEM))
        return [el.text for el in self.driver.find_elements(*self.CART_ITEM_NAME)]