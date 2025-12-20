from selenium import webdriver

from selenium.webdriver.common.by import By
from time import sleep
import pytest

def test_login_successfully_non_press_key():
    #open browser
    driver = webdriver.Chrome()
    base_url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    #input url on browser
    driver.get(base_url)
    driver.maximize_window()
    #wait for system under test to be fully loaded
    sleep(5)
    #input username & password
    driver.find_element(By.NAME, "username").send_keys("Admin")
    driver.find_element(By.NAME, "password").send_keys("admin123")
    #click on "Login" button
    driver.find_element(By.CSS_SELECTOR, ".orangehrm-login-button").click() #.orangehrm-login-button / .oxd-button
    
    sleep(5)
    #Expected result: redirect to HomePage
    #Verify Dashboard tittle
   
    assert driver.find_element(By.CSS_SELECTOR, ".oxd-text--h6").text == "Dashboard"
    

    