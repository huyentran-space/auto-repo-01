from time import sleep
import pytest
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page_1 import CheckoutPage1
from pages.checkout_page_2 import CheckoutPage2  
from pages.checkout_complete_page import CheckoutCompletePage

@pytest.mark.checkout
def test_checkout_3_products(logged_in_driver):
    driver = logged_in_driver

    inventory_page = InventoryPage(driver)
    inventory_page.add_products_to_cart(3)
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
    checkout_page1.continue_checkout()
    #sleep(3)  # Wait for the checkout page to load
    checkout_page2 = CheckoutPage2(driver)
    checkout_page2.finish_checkout()
    #sleep(3)  # Wait for the completion page to load

    complete_page = CheckoutCompletePage(driver)
    #sleep(3)  # Wait for the completion page to load

    assert complete_page.get_title_text() == "Thank you for your order!"
    assert complete_page.get_message_text() == (
        "Your order has been dispatched, and will arrive just as fast as the pony can get there!"
    )
