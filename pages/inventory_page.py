from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class InventoryPage(BasePage):

    ADD_BACKPACK = (By.ID, "add-to-cart-sauce-labs-backpack")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")

    def add_backpack_to_cart(self):
        self.click(self.ADD_BACKPACK)

    def get_cart_count(self):
        return self.get_text(self.CART_BADGE)

    def open_cart(self):
        self.click(self.CART_ICON)
