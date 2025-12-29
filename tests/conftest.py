import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    url="https://opensource-demo.orangehrmlive.com/"
    driver.get(url)
    yield driver
    driver.quit()
