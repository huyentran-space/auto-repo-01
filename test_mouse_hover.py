import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from time import sleep

def test_hover_main_item_2():
        driver = webdriver.Chrome()
        driver.implicitly_wait(20)
        driver.maximize_window()
        driver.get("https://demoqa.com/menu#")
        
        main_item_2 = driver.find_element(By.XPATH, "//a[normalize-space(text())='Main Item 2']")
        ActionChains(driver).move_to_element(main_item_2).perform()
        sleep(2)

        print("Hovered to 'Main Item 2' successfully")

        driver.quit()
