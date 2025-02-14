

class Cart():
    
    def __init__(self):
        self._cart = []
        self.__total_price = 0

    @property
    def shopping(self):
        return self._cart
    
    @shopping.setter
    def shopping(self, product):
        self._cart.append(product)
        
    @shopping.deleter
    def shopping(self):
        self._cart.clear()
        
    
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
                _tmp_product["sum_price"] =  round(_tmp_product["price"] *sum(_product_count), 2)
                
                _new_cart.append(_tmp_product)
                
            self._cart = _new_cart

    
    def cart_total_price(self) -> None:
        """
        Method to update the total sum of the cart
        """
        self.__total_price = round(sum([p["sum_price"] for p in self._cart]), 2)


    def cart_item_modify(self, item_index: int, modification: str) -> None:
        
        match modification:
            case "delete":
                self._cart.pop(item_index)
            
            case "add":
                self._cart[item_index]["count"] += 1
                self._cart[item_index]["sum_price"] = round(self._cart[item_index]["sum_price"] 
                                                            + self._cart[item_index]["price"], 2)
            
            case "remove":
                self._cart[item_index]["count"] -= 1
                self._cart[item_index]["sum_price"] = round(self._cart[item_index]["sum_price"] 
                                                            - self._cart[item_index]["price"], 2)
                
                
        self.cart_total_price()


    def menu_cart_all(self, order):
        """
        Method for seeing the whole shopping cart
        """
        self.cart_cleanup()
        self.cart_total_price()
        
        while True:
            something_went_wrong: bool = False
            
            print()
            
            if len(self._cart) == 0:
                print(" No products in your cart")
                print()
                print(" The total sum is: $0")
                print()
        
            else:
                print(" Products in your cart")
                
                for i, item in enumerate(self._cart, start=1):
                    print(f"  - {i}. {item['title']} ({item['category'].title()})")
                    print(f"       {' ' if i > 9 else ''}${item['price']} x {item['count']} = ${item['sum_price']}")
                
                print()
                print(f" The total sum is: ${self.__total_price}")
                print()
                print(" * Press the above number to see the cart details for that product.")
                print(" * Press 'o' to make the order.")
                   
            print(" * Press 'e' to exit to the main menu.")
            print()
            
            select_cart_all = input(" Enter your selection >> ").casefold()
            
            if select_cart_all  == "e":
                break
            
            if select_cart_all  == "o":
                
                if len(self._cart) > 0:
                    order_added: bool = order.add_order(self._cart, self.__total_price)
                    
                    if order_added:
                        print()
                        print(" > Your order was processed")
                        del(self.shopping)
                        break
                        
                    else:
                        print()
                        print(" > Error: your order was not able to be processed.")
                        
                        
                    break
                
                else:
                    something_went_wrong = True
                
            else:
                try:
                    select_cart_all_nr = int(select_cart_all)

                except:
                    something_went_wrong = True

                else:
                    if select_cart_all_nr <= len(self._cart):

                        self.menu_cart_item(select_cart_all_nr -1)

                    else:
                        something_went_wrong = True

            if something_went_wrong:
                print()
                print(" > That was not a valid selection.")


    def menu_cart_item(self, item_index: int) -> None:
        
        while True:
            something_went_wrong: bool = False
            
            print()
            print(" Product in your cart")
            print(f"  - {self._cart[item_index]['title']} ({self._cart[item_index]['category'].title()})")
            print(f"    ${self._cart[item_index]['price']} x {self._cart[item_index]['count']} = ${self._cart[item_index]['sum_price']}")
            print()
            
            print(" * Press 'd' to delete the product from your cart.")
            print(" * Press '+' to add the same product to your cart.")
            print(" * Press '-' to remove the same product to your cart.")
            print(" * Press 'e' to exit to your cart.")
            print()

            select_cart_item = input(" Enter your selection >> ").casefold()
            
            match select_cart_item:
                case "e":
                    break 

                case "d":
                    self.cart_item_modify(item_index, "delete")
                    break
                    
                case "+":
                    self.cart_item_modify(item_index, "add")
                    
                case "-":
                    if self._cart[item_index]['count'] > 1: 
                        self.cart_item_modify(item_index, "remove")
                    
                case _:
                    something_went_wrong: bool = True

            if something_went_wrong:
                print()
                print(" > That was not a valid selection.")


 
if __name__ == "__main__":
    print("Wrong file")