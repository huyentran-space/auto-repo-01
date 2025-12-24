from pages.login_page import LoginPage
from selenium.webdriver.common.by import By

def test_login(driver):
    login_page = LoginPage(driver)
    login_page.do_login("Admin","admin123")
    assert driver.find_element(By.CSS_SELECTOR, ".oxd-text--h6").text == "Dashboard"
