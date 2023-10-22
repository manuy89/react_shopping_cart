from pages.products_page import ProductsPage
from tests.base_test import BaseTest

class TestAddToCart(BaseTest):

    def test_add_items_to_cart(self):
        products_page = ProductsPage(self.driver)
        products_page.add_to_cart_free_shipping_items()
        products_page.add_to_cart_not_free_shipping_items()

        actual_cart_quantity = products_page.no_of_items_in_cart()

        assert actual_cart_quantity == 5

# Cropped Stay Groovy off white
# Basic Cactus White T-shirt
# Black Tule Oversized
# Black Batman T-shirt
# Skater Black Sweatshirt