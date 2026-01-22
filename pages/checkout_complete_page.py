from selenium.webdriver.common.by import By
from pages.base_page import BasePage 

class CheckoutCompletePage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.title = (By.CLASS_NAME, "complete-header")
        self.message = (By.CLASS_NAME, "complete-text")

    def get_title_text(self):
        return self.find_element(self.title).text

    def get_message_text(self):
        return self.find_element(self.message).text
