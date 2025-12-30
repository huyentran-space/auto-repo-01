import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep
url = "https://the-internet.herokuapp.com/dropdown"

def test_select_dropdown():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get(url)
    
    dropdown_element = driver.find_element(By.ID,"dropdown")    
    dropdown = Select(dropdown_element)
    
    sleep(3)
    
    dropdown.select_by_visible_text("Option 2")
    assert driver.find_element(By.XPATH,"//option[@selected='selected']").text == "Option 2"
    
    sleep(3)
    
    dropdown.select_by_value("1")
    assert driver.find_element(By.XPATH,"//option[@selected='selected']").text == "Option 1"

    sleep(3)
    
                                               
    driver.quit() 