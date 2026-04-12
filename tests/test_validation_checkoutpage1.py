from time import sleep
import pytest
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page_1 import CheckoutPage1
from pages.checkout_page_2 import CheckoutPage2  
from pages.checkout_complete_page import CheckoutCompletePage

@pytest.mark.validation
def test_empty_first_name(logged_in_driver):
    driver = logged_in_driver

    inventory_page = InventoryPage(driver)
    inventory_page.add_products_to_cart(1)
    #sleep(3)  # Wait for the products to be added to the cart
    inventory_page.go_to_cart()
    #sleep(3)  # Wait for the cart page to load

    cart_page = CartPage(driver)
    cart_page.click_checkout()
    #sleep(3)  # Wait for the checkout page to load

    checkout_page1 = CheckoutPage1(driver)
    checkout_page1.fill_checkout_info_with_empty_first_name(
        last="Doe",
        zip_code="70000"
    )        
    sleep(3)  # Wait for the fields to be filled

    checkout_page1.continue_checkout()
    sleep(3)  # Wait for the error message to appear

    assert checkout_page1.get_error_message() == "Error: First Name is required"  

def test_empty_last_name(logged_in_driver):
    driver = logged_in_driver

    inventory_page = InventoryPage(driver)
    inventory_page.add_products_to_cart(1)
    #sleep(3)  # Wait for the products to be added to the cart
    inventory_page.go_to_cart()
    #sleep(3)  # Wait for the cart page to load

    cart_page = CartPage(driver)
    cart_page.click_checkout()
    #sleep(3)  # Wait for the checkout page to load

    checkout_page1 = CheckoutPage1(driver)
    checkout_page1.fill_checkout_info_with_empty_last_name(
        first="John",
        zip_code="70000"
    )        
    sleep(3)  # Wait for the fields to be filled

    checkout_page1.continue_checkout()
    sleep(3)  # Wait for the error message to appear

    assert checkout_page1.get_error_message() == "Error: Last Name is required"  