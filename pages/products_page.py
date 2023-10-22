from .base_page import BasePage
from selenium.webdriver.common.by import By
import time


class ProductsPage(BasePage):

    all_sizes = (By.XPATH, "//span[@class='checkmark']")
    product_name = (By.XPATH, "//p[text()='Black Batman T-shirt']")
    products_count = (By.XPATH, "//p[contains(normalize-space(), 'Product(s) found')]")
    products_free_shipping = (By.XPATH, '//div[normalize-space()="Free shipping"]')
    cart_quantity = (By.XPATH, "//div[@title='Products in cart quantity']")
    close_cart_button = (By.XPATH, "//span[normalize-space()='X']")
    all_products = (By.XPATH, "//button[contains(normalize-space(),'Add to cart')]//parent::div/parent::div/div")


    def __init__(self, driver):
        super().__init__(driver)

    def click_size(self, size):
        self.wait_for_initial_load(self.products_count)
        text_before = self.get_text(self.products_count)
        print(f"text_before: {text_before}")
        self.click((By.XPATH, "//span[text()='"+ size +"']"))
        self.wait_for_text_to_change(self.products_count, text_before) 

    def get_product_name(self, *, timeout=2):
        if self.wait_for_presence_of_element(self.product_name, timeout=timeout):
            return self.get_text(self.product_name)

    def get_no_of_products(self, *, timeout=2):
        products_count_text = self.get_text(self.products_count)
        return int(products_count_text.split()[0])
    
    def add_to_cart_free_shipping_items(self, *, no_of_items_to_add=4):
        count_of_items_added = 0
        self.wait_for_initial_load(self.products_count)
        for product in self.get_elements(self.products_free_shipping):
            if count_of_items_added < no_of_items_to_add:
                product.find_element(By.XPATH, 'parent::div/button').click()
                time.sleep(1)
                count_of_items_added += 1
                self.click(self.close_cart_button)
                time.sleep(1)
            else:
                break

    def add_to_cart_not_free_shipping_items(self, *, no_of_items_to_add=1):
        count_of_items_added = 0
        self.wait_for_initial_load(self.products_count)
        for product in self.get_elements(self.all_products):
            if not product.find_element(By.XPATH, 'child::div').text and count_of_items_added < no_of_items_to_add:
                product.find_element(By.XPATH, 'button').click()
                time.sleep(1)
                self.click(self.close_cart_button)
                count_of_items_added += 1
                time.sleep(1)
              


    def no_of_items_in_cart(self):
        return int(self.get_text(self.cart_quantity))