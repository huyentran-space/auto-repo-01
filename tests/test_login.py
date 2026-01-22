import pytest
from pages.login_page import LoginPage
from selenium.webdriver.common.by import By
from utils.config_reader import ConfigReader
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.login
 
def test_login(driver):
    login_page = LoginPage(driver)
    login_page.do_login(ConfigReader.get_username(),ConfigReader.get_password())
    
    WebDriverWait(driver, 10).until(
    EC.url_to_be("https://www.saucedemo.com/inventory.html")
)
    assert driver.current_url == "https://www.saucedemo.com/inventory.html"
    