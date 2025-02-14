import uuid, datetime

class Order():
    """
    
    """
    def __init__(self):
        self._orders = []
        
 
    def get_order(self, order_id):
        _order = [o for o in self._order if o['order_id'] == order_id]
        
        if len(_order) == 1:
            return _order
        
        else:
            return None

    
    def add_order(self, cart, total_price) -> bool:
        
        count_order_before = len(self._orders)
       
        count_product = sum([product["count"] for product in cart])
                
        self._orders.append({"order_id": str(uuid.uuid4()), "product_count": count_product, "timestamp": datetime.datetime.now(), "products": cart.copy(), "total_price": total_price, })
        
        if len(self._orders) == count_order_before +1:
            return True
        
        else:
            return False
        
        
        
    def menu_order_all(self):
        
        while True:
            
            something_went_wrong = False
            
            print()
        
            if len(self._orders) == 0:
                print(" No orders to fulfill")
            
            else:
                print(" Orders")
                for i, order in enumerate(self._orders, start=1):
                    print(f"  - {i}. {order['timestamp'].strftime("%Y-%m-%d %H:%M")}, {order['product_count']} item{"s" if order['product_count'] > 1 else ""}, ${order['total_price']}")                    
                
            print()
            
            if len(self._orders) > 0:
                print(" * Press the above number to see the details about the order.")
                
            print(" * Press 'e' to exit to the main menu.")
            print()
            
            select_order_all = input(" Enter your selection >> ").casefold()
            
            if select_order_all == "e":
                break
            
            else:
                try:
                    select_order_all_nr = int(select_order_all)

                except:
                    something_went_wrong = True

                else:
                    if select_order_all_nr <= len(self._orders):
                        self.menu_order_one(select_order_all_nr -1)

                    else:
                        something_went_wrong = True

            if something_went_wrong:
                print()
                print(" > That was not a valid selection.")
                
                
    def menu_order_one(self, order_id: int):
        
        while True:
            
            print()
            print(" Order")
            print(f"  ID: {self._orders[order_id]["order_id"]}")
            print(f"  Order date: {self._orders[order_id]['timestamp'].strftime("%Y-%m-%d %H:%M")}")
            print(f"  Number of items: {self._orders[order_id]['product_count']}")
            print(f"  Order value: ${self._orders[order_id]['total_price']}")
            print()
            
            print("  Ordered products")
            
            for product in self._orders[order_id]["products"]:
                print(f"   - {product['id']}: {product['title']} ({product['category']}) x{product['count']}")
            
            print()
            print(" * Press 'f' if the order is fulfilled.")
            print(" * Press 'e' to exit to the order menu.")
            print()
            
            select_order_one = input(" Enter your selection >> ").casefold()
            
            match select_order_one:
                case "e":
                    break
                
                case "f":
                    self._orders.pop(order_id)
                    
                    print(" > Order was removed.")
                    break
                
                case _:
                    print()
                    print(" > That was not a valid selection.")



if __name__ == "__main__":
    print("Wrong file")