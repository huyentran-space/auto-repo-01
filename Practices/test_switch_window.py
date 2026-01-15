import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep

def test_submit_form():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get('https://www.letskodeit.com/practice')
    
    button = driver.find_element(By.ID, "openwindow")
    button.click()
    sleep(1)
    driver.switch_to.window(driver.window_handles[1])
    sleep(2)
    driver.maximize_window()
    sleep(2)
    driver.quit()
    