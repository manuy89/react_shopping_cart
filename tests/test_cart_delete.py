from tests.base_test import BaseTest
from pages.products_page import ProductsPage
from utilities.test_data import TestCartDelete


class TestRemoveItems(BaseTest):
    
    def test_remove_cart_items(self):
        products_page = ProductsPage(self.driver)
        products_page.add_to_cart_free_shipping_items()

        actual_cart_quantity = products_page.no_of_items_in_cart()
        actual_cart_items_list = products_page.list_of_items_in_cart()

        assert actual_cart_quantity == TestCartDelete.cart_quantity
        assert actual_cart_items_list == TestCartDelete.items_expected_in_cart

        products_page.remove_all_items_from_cart()

        actual_cart_subtotal = products_page.get_cart_subtotal()
        actual_cart_quantity = products_page.no_of_items_in_cart()

        assert actual_cart_subtotal == TestCartDelete.cart_subtotal_after_delete
        assert actual_cart_quantity == TestCartDelete.cart_quantity_after_delete

    def test_cart_checkout(self):
        products_page = ProductsPage(self.driver)
        products_page.add_to_cart_free_shipping_items()
        actual_cart_subtotal = products_page.get_cart_subtotal()
        alert_text = products_page.cart_checkout()

        assert TestCartDelete.cart_subtotal in alert_text

        products_page.refresh()

        actual_cart_quantity = products_page.no_of_items_in_cart()

        assert actual_cart_quantity == 0