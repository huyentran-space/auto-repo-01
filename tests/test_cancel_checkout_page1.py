from time import sleep
import pytest
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page_1 import CheckoutPage1
from pages.checkout_page_2 import CheckoutPage2  
from pages.checkout_complete_page import CheckoutCompletePage

@pytest.mark.cancel_checkout1
def test_cancel_checkout1(logged_in_driver):
    driver = logged_in_driver

    inventory_page = InventoryPage(driver)
    inventory_page.add_products_to_cart(4)
    #sleep(3)  # Wait for the products to be added to the cart
    inventory_page.go_to_cart()
    #sleep(3)  # Wait for the cart page to load

    cart_page = CartPage(driver)
    cart_page.click_checkout()
    #sleep(3)  # Wait for the checkout page to load

    checkout_page1 = CheckoutPage1(driver)
    checkout_page1.fill_checkout_info(
        first="John",
        last="Doe",
        zip_code="70000"
    )
    checkout_page1.cancel_checkout()
    #sleep(3)  # Wait for the cart page to load
    cartpage_title = cart_page.get_cartpage_title()
    assert cartpage_title == "Your Cart"
