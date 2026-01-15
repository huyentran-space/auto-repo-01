from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

def test_handle_alert_and_confirm():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get("https://www.letskodeit.com/practice")

    alert_button = driver.find_element(By.ID, "alertbtn")
    alert_button.click()

    alert = driver.switch_to.alert
    sleep(2)
    alert.accept()

    confirm_button = driver.find_element(By.ID, "confirmbtn")
    confirm_button.click()

    confirm_alert = driver.switch_to.alert
    sleep(2)
    confirm_alert.accept()

    sleep(2)
    driver.quit()
