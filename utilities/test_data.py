class TestData:
    url = 'https://react-shopping-cart-67954.firebaseapp.com/'

class TestAddToCartData:
    items_expected_in_cart = [('Cropped Stay Groovy off white', '$ 10.90'), 
                             ('Basic Cactus White T-shirt', '$ 13.25'),
                              ('Black Tule Oversized', '$ 29.45'),
                              ('Black Batman T-shirt', '$ 10.90'),
                              ('Skater Black Sweatshirt', '$ 25.90')]
    
    same_item_quantity_price = [('Cropped Stay Groovy off white', '$ 10.90')]
    cart_quantity = 5
    cart_quantity_same_items = 3
    cart_subtotal = '$ 32.70'


class TestCartDelete:
    items_expected_in_cart = [('Cropped Stay Groovy off white', '$ 10.90'), 
                             ('Basic Cactus White T-shirt', '$ 13.25'),
                              ('Black Tule Oversized', '$ 29.45'),
                              ('Black Batman T-shirt', '$ 10.90')
                              ]
    
    cart_subtotal = '$ 64.50'
    cart_quantity = 4
    cart_subtotal_after_delete = '$ 0.00'
    cart_quantity_after_delete = 0
    



    

