from tests.base_test import BaseTest
from pages.products_page import ProductsPage
import pytest

class TestSizeFilter(BaseTest):

    @pytest.mark.parametrize(
            'size, expected_no_of_products',
            [('XS', 1), ('M', 1), ('L', 10), ('XXL', 4)]
            )
    def test_single_size_filter(self, size, expected_no_of_products):
        products_page = ProductsPage(self.driver)
        products_page.click_size(size)
        actual_no_of_products = products_page.get_no_of_products()

        assert actual_no_of_products == expected_no_of_products

    
    @pytest.mark.parametrize(
        'size1, size2, expected_no_of_products',
        [('S', 'M', 3), ('L', 'XXL', 11)]
    )
    def test_two_size_filters(self, size1, size2, expected_no_of_products):
        products_page = ProductsPage(self.driver)
        products_page.click_size(size1)
        products_page.click_size(size2)
        actual_no_of_products = products_page.get_no_of_products()
        
        assert actual_no_of_products == expected_no_of_products