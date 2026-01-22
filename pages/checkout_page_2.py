from selenium.webdriver.common.by import By
from pages.base_page import BasePage 

class CheckoutPage2(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.finish_button = (By.ID, "finish")
        self.cancel_button2 = (By.ID, "cancel")

    def finish_checkout(self):
        self.click(self.finish_button)

    def cancel_checkout(self):
        self.click(self.cancel_button2)
