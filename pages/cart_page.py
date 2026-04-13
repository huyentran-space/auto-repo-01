from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from tests.conftest import driver 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.checkout_button = (By.ID, "checkout")
        self.continue_shopping_button = (By.ID, "continue-shopping")
        self.remove_button = (
            By.XPATH,
            "//div[@data-test='cart-list']//button[contains(@data-test,'remove')]"
        )
        self.cartpage_title_locator = (By.CLASS_NAME, "title")    

    def click_checkout(self):
        self.click(self.checkout_button)

    def click_continue_shopping(self):
        self.click(self.continue_shopping_button)

    def get_cartpage_title(self):
        return self.find_element(self.cartpage_title_locator).text
    
    def find_remove_buttons(self):
        return self.find_elements(self.remove_button)
    
    def remove_all_products_from_cart(self):
        wait = WebDriverWait(self.driver, 10)
        while True:
            remove_buttons = self.find_remove_buttons()
            if not remove_buttons:
                break

            wait.until(EC.element_to_be_clickable(remove_buttons[0]))

            remove_buttons[0].click()

            # Chờ DOM update (button cũ biến mất)
            wait.until(EC.staleness_of(remove_buttons[0]))




