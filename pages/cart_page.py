from selenium.webdriver.common.by import By
from pages.base_page import BasePage 

class CartPage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.checkout_button = (By.ID, "checkout")
        self.continue_shopping_button = (By.ID, "continue-shopping")    

    def click_checkout(self):
        self.click(self.checkout_button)

    def click_continue_shopping(self):
        self.click(self.continue_shopping_button)
