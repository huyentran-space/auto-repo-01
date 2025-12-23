from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import pytest

def test_login_successfully(driver):
    driver.find_element(By.NAME, "username").send_keys("Admin")
    driver.find_element(By.NAME, "password").send_keys("admin123")
    #click on "Login" button
    driver.find_element(By.CSS_SELECTOR, ".orangehrm-login-button").click() #.orangehrm-login-button / .oxd-button
    
    sleep(5)
    #Expected result: redirect to HomePage
    #Verify Dashboard tittle
   
    assert driver.find_element(By.CSS_SELECTOR, ".oxd-text--h6").text == "Dashboard"
    
