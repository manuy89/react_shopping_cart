from tests.base_test import BaseTest
from pages.products_page import ProductsPage
from utilities.test_data import TestDataRemoveMaxPriceItem

class TestRemoveMaxPriceItem(BaseTest):
    
    def test_remove_items(self):
        products_page = ProductsPage(self.driver)
        products_page.add_to_cart_free_shipping_items(no_of_items_to_add=3)
        actual_cart_quantity = products_page.get_cart_quantity()

        assert actual_cart_quantity == TestDataRemoveMaxPriceItem.cart_quantity

        products_page.remove_highest_priced_product()
        actual_cart_quantity = products_page.get_cart_quantity()

        assert actual_cart_quantity == TestDataRemoveMaxPriceItem.cart_quantity_after_remove

    

        