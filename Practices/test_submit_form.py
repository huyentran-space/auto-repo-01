import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep
url = "https://the-internet.herokuapp.com/login"

def test_submit_form():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get(url)
    
    username = driver.find_element(By.ID, "username")
    password = driver.find_element(By.ID, "password")
    username.send_keys("tomsmith")
    sleep(2)
    password.send_keys("SuperSecretPassword!")
    sleep(2)
    driver.find_element(By.TAG_NAME, "form").submit()
    sleep(2)
    assert "Secure Area" in driver.page_source
    driver.quit()

