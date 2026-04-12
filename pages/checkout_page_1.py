from selenium.webdriver.common.by import By
from pages.base_page import BasePage 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

class CheckoutPage1(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.first_name = (By.ID, "first-name")
        self.last_name = (By.ID, "last-name")
        self.zip_code = (By.ID, "postal-code")
        self.continue_button = (By.ID, "continue")
        self.cancel_button1 = (By.ID, "cancel")
        self.error_message = (By.CSS_SELECTOR, "h3[data-test='error']") 

    def fill_checkout_info(self, first, last, zip_code):
        self.clear_and_type(self.first_name, first)
        self.clear_and_type(self.last_name, last)
        self.clear_and_type(self.zip_code, zip_code)

    def fill_first_name(self, first):
        self.clear_and_type(self.first_name, first)

    def fill_last_name(self, last):
        self.clear_and_type(self.last_name, last)

    def fill_zip_code(self, zip_code):
        self.clear_and_type(self.zip_code, zip_code)

    def fill_checkout_info_with_empty_first_name(self, last, zip_code):
        self.clear_and_type(self.last_name, last)
        self.clear_and_type(self.zip_code, zip_code)

    def fill_checkout_info_with_empty_last_name(self, first, zip_code):
        self.clear_and_type(self.first_name, first)
        self.clear_and_type(self.zip_code, zip_code)

    def fill_checkout_info_with_empty_zip_code(self, first, last):
        self.clear_and_type(self.first_name, first)
        self.clear_and_type(self.last_name, last)

    def clear_checkout_info(self):
        self.find_element(self.first_name).clear()
        self.find_element(self.last_name).clear()
        self.find_element(self.zip_code).clear()

    def clear_first_name(self):
        self.find_element(self.first_name).clear()

    def clear_last_name(self):
        self.find_element(self.last_name).clear()

    def clear_zip_code(self):
        self.find_element(self.zip_code).clear()

    def continue_checkout(self):
        self.click(self.continue_button)

    def cancel_checkout(self):
        self.click(self.cancel_button1)

    def get_error_message(self):
        return WebDriverWait(self.driver, 10).until(
        EC.visibility_of_element_located(self.error_message)
    ).text
