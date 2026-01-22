from selenium.webdriver.common.by import By
from pages.base_page import BasePage 

class CheckoutPage1(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.first_name = (By.ID, "first-name")
        self.last_name = (By.ID, "last-name")
        self.zip_code = (By.ID, "postal-code")
        self.continue_button = (By.ID, "continue")
        self.cancel_button1 = (By.ID, "cancel")

    def fill_checkout_info(self, first, last, zip_code):
        self.find_element(self.first_name).send_keys(first)
        self.find_element(self.last_name).send_keys(last)
        self.find_element(self.zip_code).send_keys(zip_code)
        self.click(self.continue_button)

    def cancel_checkout(self):
        self.click(self.cancel_button)
