from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

class BasePage:
    def __init__(self,driver):
        self.driver=driver
    
    def find_element(self, locator):
        return self.driver.find_element(*locator)
    
    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    def click(self,locator):
        element = self.find_element(locator)
        try:
            element.click()
        except NoSuchElementException:
            element = self.wait_for_element_clickable(locator)
            element.click()

    def clear_and_type(self, locator, text):
        element = self.find_element(locator)
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.DELETE)
        element.send_keys(text)
        
    def wait_for_element_clickable(self,locator,timeout=None):
        wait = WebDriverWait(self.driver,timeout)
        return wait.until(EC.element_to_be_clickable(*locator))