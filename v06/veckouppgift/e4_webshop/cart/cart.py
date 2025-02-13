

class Cart():
    
    def __init__(self):
        self._cart = []
        self.__sum_price = 0

    @property
    def shopping(self):
        return self._cart
    
    @shopping.setter
    def shopping(self, product):
        self._cart.append(product)
        
    
    def cart_cleanup(self) -> None:
        """
        Method that goes though the shopping cart and fixes dublicates...
        """
        _unique_product_id = list(set([product["id"] for product in self._cart]))
        
        if len(_unique_product_id) != len(self._cart):
            _new_cart = []
            
            for _unique_id in _unique_product_id:
                
                _product = [p for p in self._cart if p["id"] == _unique_id]
                _product_count = [p["count"] for p in _product]
                _tmp_product = _product[0]
                _tmp_product["count"] = sum(_product_count)
                _tmp_product["total_price"] =  round(_tmp_product["price"] *sum(_product_count), 2)
                
                _new_cart.append(_tmp_product)
                
            self._cart = _new_cart
    
    
    def cart_total_price(self) -> None:
        self.__sum_price = round(sum([p["total_price"] for p in self._cart]), 2)
        
    
    def menu_cart(self):
        
        self.cart_cleanup()
        self.cart_total_price()
        
        print(f"Items in the cart:")
        
        for item in self._cart:
            print(f" - {item}")
        
        print()
        print(self.__sum_price)
        print()
        hello = input("hello")
    
if __name__ == "__main__":
    print("Wrong file")