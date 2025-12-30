import pytest
from pages.login_page import LoginPage
from selenium.webdriver.common.by import By
from utils.config_reader import ConfigReader

def test_login(driver):
    login_page = LoginPage(driver)
    login_page.do_login(ConfigReader.get_username(),ConfigReader.get_password())
    assert driver.find_element(By.CSS_SELECTOR, ".oxd-text--h6").text == "Dashboard"
