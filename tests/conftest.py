import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from utils.config_reader import ConfigReader

@pytest.fixture(scope="function")
def driver():
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(ConfigReader.get_timeouts())
    driver.maximize_window()
    driver.get(ConfigReader.get_base_url())
    yield driver
    driver.quit()
