from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class InventoryPage(BasePage):

    ADD_BACKPACK_BUTTON = (By.ID, "add-to-cart-sauce-labs-backpack")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")
    PAGE_TITLE = (By.CLASS_NAME, "title")
    PRODUCT_ITEMS = (By.CLASS_NAME, "inventory_item")

    def add_backpack_to_cart(self):
        self.click(self.ADD_BACKPACK_BUTTON)

        # wait until badge appears
        self.wait.until(
            EC.visibility_of_element_located(self.CART_BADGE)
        )

    def get_cart_count(self):
        return self.get_text(self.CART_BADGE)

    def get_page_title(self):
        return self.get_text(self.PAGE_TITLE)

    def get_product_count(self):
        self.wait.until(EC.visibility_of_element_located(self.PRODUCT_ITEMS))
        return len(self.driver.find_elements(*self.PRODUCT_ITEMS))

    def open_cart(self):
        self.js_click(self.CART_ICON)
        self.wait.until(EC.visibility_of_element_located((By.ID, "checkout")))
