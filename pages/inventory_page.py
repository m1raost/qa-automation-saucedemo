from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class InventoryPage(BasePage):

    PAGE_TITLE = (By.CLASS_NAME, "title")
    PRODUCT_ITEMS = (By.CLASS_NAME, "inventory_item")

    def get_page_title(self):
        return self.get_text(self.PAGE_TITLE)

    def get_product_count(self):
        self.wait.until(EC.visibility_of_element_located(self.PRODUCT_ITEMS))
        return len(self.driver.find_elements(*self.PRODUCT_ITEMS))
