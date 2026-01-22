from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys   
from pages.base_page import BasePage 


class LoginPage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.username = (By.ID, "user-name")
        self.password = (By.ID, "password")
        self.login_button = (By.ID, "login-button")
       
    def enter_username(self, username):
        self.find_element(self.username).send_keys(username)
       
    def enter_password(self, password):
        self.find_element(self.password).send_keys(password)
       
    def click_login_button(self):
        self.click(self.login_button)
       
    def do_login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()