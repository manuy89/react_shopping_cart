from pages.products_page import ProductsPage
from tests.base_test import BaseTest
from utilities.test_data import TestAddToCartData

class TestAddToCart(BaseTest):

    def test_order_of_items_in_cart(self):
        products_page = ProductsPage(self.driver)
        products_page.add_to_cart_free_shipping_items()
        products_page.add_to_cart_not_free_shipping_items()

        actual_cart_quantity = products_page.no_of_items_in_cart()
        actual_cart_items_list = products_page.list_of_items_in_cart()

        assert actual_cart_quantity == TestAddToCartData.cart_quantity

        assert actual_cart_items_list == TestAddToCartData.items_expected_in_cart

    
    def test_add_same_item_to_cart(self):
        products_page = ProductsPage(self.driver)
        for _ in range(2):
            products_page.add_to_cart_free_shipping_items(no_of_items_to_add=1)
        
        products_page.increase_quantity_from_cart()
        actual_cart_quantity = products_page.no_of_items_in_cart()
        actual_cart_items_list = products_page.list_of_items_in_cart()
        actual_cart_subtotal = products_page.get_cart_subtotal()
        
        assert actual_cart_quantity == TestAddToCartData.cart_quantity_same_items

        assert actual_cart_items_list == TestAddToCartData.same_item_quantity_price

        assert actual_cart_subtotal == TestAddToCartData.cart_subtotal


    

    


