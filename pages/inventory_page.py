from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class InventoryPage(BasePage):

    PAGE_TITLE = (By.CLASS_NAME, "title")
    PRODUCT_ITEMS = (By.CLASS_NAME, "inventory_item")
    FIRST_ADD_TO_CART = (By.CSS_SELECTOR, "[data-test^='add-to-cart']")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")

    def get_page_title(self):
        return self.get_text(self.PAGE_TITLE)

    def get_product_count(self):
        self.wait.until(EC.visibility_of_element_located(self.PRODUCT_ITEMS))
        return len(self.driver.find_elements(*self.PRODUCT_ITEMS))

    def add_first_item_to_cart(self):
        self.js_click(self.FIRST_ADD_TO_CART)
        self.wait.until(EC.visibility_of_element_located(self.CART_BADGE))

    def get_cart_badge_count(self):
        return int(self.get_text(self.CART_BADGE))

    def go_to_cart(self):
        self.js_click(self.CART_ICON)
        self.wait.until(EC.url_contains("cart"))
