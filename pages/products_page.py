from .base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time


class ProductsPage(BasePage):

    all_sizes = (By.XPATH, "//span[@class='checkmark']")
    product_name = (By.XPATH, "//p[text()='Black Batman T-shirt']")
    products_count = (By.XPATH, "//p[contains(normalize-space(), 'Product(s) found')]")
    products_free_shipping = (By.XPATH, '//div[normalize-space()="Free shipping"]')
    cart_quantity = (By.XPATH, "//div[@title='Products in cart quantity']")
    close_cart_button = (By.XPATH, "//span[normalize-space()='X']")
    all_products = (By.XPATH, "//button[contains(normalize-space(),'Add to cart')]//parent::div/parent::div/div")
    cart_button = (By.XPATH, "//div[@title='Products in cart quantity']/parent::div")
    all_cart_items = (By.XPATH, "//span[contains(normalize-space(),'Cart')]//parent::div/following-sibling::div[1]/div")
    cart_subtotal = (By.XPATH, "//p[normalize-space()='SUBTOTAL']//parent::div//div//p[1]")
    plus_icon_cart = (By.XPATH, "//button[normalize-space()='+'][1]")
    remove_items = (By.XPATH, "//button[@title='remove product from cart']")
    checkout = (By.XPATH, "//button[normalize-space()='Checkout']")
    cart = (By.XPATH, "//span[normalize-space()='Cart']")
    subtotal_text = (By.XPATH, "//p[normalize-space()='SUBTOTAL']")

    new_cart_quantity = (By.XPATH, "//span[normalize-space()='Cart']//parent::div/div/div")


    def __init__(self, driver):
        super().__init__(driver)

    def click_size(self, size):
        self.wait_for_initial_load(self.products_count)
        text_before = self.get_text(self.products_count)
        self.click((By.XPATH, "//span[text()='"+ size +"']"))
        self.wait_for_text_to_change(self.products_count, text_before) 

    def get_product_name(self, *, timeout=2):
        if self.wait_for_presence_of_element(self.product_name, timeout=timeout):
            return self.get_text(self.product_name)

    def get_no_of_products(self):
        products_count_text = self.get_text(self.products_count)
        return int(products_count_text.split()[0])
    
    def add_to_cart_free_shipping_items(self, *, no_of_items_to_add=4):
        count_of_items_added = 0
        self.wait_for_initial_load(self.products_count)
        for product in self.get_elements(self.products_free_shipping):
            if count_of_items_added < no_of_items_to_add:
                product.find_element(By.XPATH, 'parent::div/button').click()
                # self.wait_for_element_to_be_clickable(self.remove_items)
                time.sleep(1)
                self.click(self.close_cart_button)
                count_of_items_added += 1
                # self.wait_for_element_to_be_invisible(self.subtotal_text)
                time.sleep(1)
            else:
                break

    def add_to_cart_not_free_shipping_items(self, *, no_of_items_to_add=1):
        count_of_items_added = 0
        self.wait_for_initial_load(self.products_count)
        for product in self.get_elements(self.all_products):
            if not product.find_element(By.XPATH, 'child::div').text and count_of_items_added < no_of_items_to_add:
                product.find_element(By.XPATH, 'button').click()
                # self.wait_for_element_to_be_clickable(self.remove_items)
                time.sleep(1)
                self.click(self.close_cart_button)
                count_of_items_added += 1
                time.sleep(1)
              
    def no_of_items_in_cart(self):
        time.sleep(1)
        return int(self.get_text(self.cart_quantity))
    
    def list_of_items_in_cart(self):
        items_list = []
        time.sleep(1)
        self.click(self.cart_button)
        # self.wait_for_element_to_be_clickable(self.remove_items)
        time.sleep(1)
        for item in self.get_elements(self.all_cart_items):
            item_name = item.find_element(By.XPATH, "div[1]/p[1]").text
            item_price = item.find_element(By.XPATH, 'div[2]/p').text
            items_list.append((item_name, item_price))
        self.click(self.close_cart_button)
        time.sleep(1)

        return items_list
    
    def get_cart_subtotal(self):
        self.wait_for_element_to_be_clickable(self.cart_button)
        self.click(self.cart_button)
        # self.wait_for_element_to_be_clickable(self.checkout)
        time.sleep(1)
        subtotal = self.get_text(self.cart_subtotal)
        self.click(self.close_cart_button)
        time.sleep(1)
        return subtotal
    
    
    def increase_quantity_from_cart(self):
        # self.wait_for_element_to_be_clickable(self.cart_button)
        time.sleep(1)
        self.click(self.cart_button)
        # self.wait_for_element_to_be_clickable(self.remove_items)
        time.sleep(1)
        self.click(self.plus_icon_cart)
        self.click(self.close_cart_button)
        time.sleep(1)

    def remove_all_items_from_cart(self):
        self.click(self.cart_button)
        # self.wait_for_element_to_be_clickable(self.remove_items)
        time.sleep(1)
        for item in self.get_elements(self.remove_items):
            item.click()
        self.click(self.close_cart_button)
        time.sleep(1)

    def cart_checkout(self):
        self.click(self.cart_button)
        # self.wait_for_element_to_be_clickable(self.remove_items)
        time.sleep(1)
        self.click(self.checkout)
        if self.wait_for_alert():
            alert = self.driver.switch_to.alert
            text = alert.text
            alert.accept()
            return text
        
    def refresh(self):
        self.driver.refresh()

    def get_cart_quantity(self):
        time.sleep(1)
        self.click(self.cart_button)
        time.sleep(1)
        cart_quantity = int(self.get_text(self.new_cart_quantity))
        self.click(self.close_cart_button)
        time.sleep(1)
        return cart_quantity
    
    def remove_highest_priced_product(self):
        cart_items = self.list_of_items_in_cart()
        max_price_item = max([float(item[1].split()[1]) for item in cart_items])
        time.sleep(1)
        self.click(self.cart_button)
        time.sleep(1)
        for item in self.get_elements(self.all_cart_items):
            if float((item.find_element(By.XPATH, 'div[2]/p').text).split()[1]) == max_price_item:
                item_name = item.find_element(By.XPATH, "div[1]/p[1]").text
                item_to_remove = item.find_element(By.XPATH, "div[1]/p[1]")
                
                ActionChains(self.driver).scroll_to_element(item_to_remove).perform()
                self.driver.execute_script("arguments[0].scrollIntoView();", item_to_remove)
                time.sleep(4)
                self.driver.find_element(By.XPATH, "//p[normalize-space()='"+item_name+"']//parent::div//parent::div/button[@title='remove product from cart']").click()
    
        time.sleep(1)
        self.click(self.close_cart_button)
        time.sleep(1)
        
                
            
        
