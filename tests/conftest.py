import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    driver.implicity_wait(10)
    driver.maximize_window()
    url="https://wikipeida.org"
    driver.get(url)
    yield driver
    driver.quit()