from time import sleep
import pytest
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

@pytest.mark.remove_product
def test_remove_all_products_from_cart(logged_in_driver):
     driver = logged_in_driver
     
     inventory_page = InventoryPage(driver)
     inventory_page.add_products_to_cart(4)
     #sleep(3)  # Wait for the products to be added to the cart
     inventory_page.go_to_cart()
     #sleep(3)  # Wait for the cart page to load
     
     cart_page = CartPage(driver)
     cart_page.remove_all_products_from_cart()
     #sleep(3)  # Wait for the products to be removed from the cart
     
     assert len(cart_page.find_remove_buttons()) == 0
     print("Removed all products from cart")
