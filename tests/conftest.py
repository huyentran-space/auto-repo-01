import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from utils.config_reader import ConfigReader
from pages.login_page import LoginPage


@pytest.fixture(scope="function")
def driver():
    options = Options()
    options.add_argument("--disable-save-password-bubble")
    options.add_argument("--disable-password-manager-reauthentication")
    options.add_argument("--disable-features=PasswordManagerOnboarding")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-extensions")
    options.add_argument("--incognito")
    #options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(ConfigReader.get_timeouts())
    driver.maximize_window()
    driver.get(ConfigReader.get_base_url())
    yield driver
    driver.quit()
    
@pytest.fixture(scope="function")
def logged_in_driver(driver):
    login_page = LoginPage(driver)
    login_page.do_login(ConfigReader.get_username(),ConfigReader.get_password())
    return driver
