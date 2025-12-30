import pytest
from selenium import webdriver
from utils.config_reader import ConfigReader

@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(ConfigReader.get_timeouts())
    driver.maximize_window()
    driver.get(ConfigReader.get_base_url())
    yield driver
    driver.quit()
