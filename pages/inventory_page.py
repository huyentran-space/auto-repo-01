from selenium.webdriver.common.by import By
from pages.base_page import BasePage 

class InventoryPage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.add_buttons = (By.CSS_SELECTOR, ".inventory_item button")
        self.cart_icon = (By.CLASS_NAME, "shopping_cart_link")

    def add_products_to_cart(self, number=3):
        buttons = self.find_elements(self.add_buttons)
        for i in range(number):
            buttons[i].click()

    def go_to_cart(self):
        self.click(self.cart_icon)