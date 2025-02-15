import uuid, datetime
from typing import Any

class Order():
    
    def __init__(self):
        """
        Sets up the order class with a empty list
        """
        self._orders = []
    
    
    # Get the orders
    @property
    def orders(self):
        """
        Retruns all of the ordes in the order list
        """
        return self._orders
    
    
    # Add a order
    @orders.setter
    def orders(self, new_order):
        """
        Adds a order to the order list
        """
        self._orders.append(new_order)
    
    
    # Count the orders
    def count_orders(self):
        """
        Counts the nnumber of orders in the order list
        """
        return len(self.orders)
    

    # Insert a cart as an order
    def insert_order(self, cart: list[dict[Any]]):
        """
        Insert an order from a cart. The carts calls the method in order
        """
        _count_cart_items = sum([c["count"] for c in cart])
        _sum_cart = sum([c["sum_item"] for c in cart])
                
        self.orders = {"order_id": uuid.uuid4(), "items": cart.copy(), "count_items": _count_cart_items, "sum_items": _sum_cart, "timestamp": datetime.datetime.now()}


    # Menu to see orders
    def menu_orders(self):
        """
        Method to view all of the orders
        """
        while True:
            
            _something_went_wrong = False
            
            print()
            print(" Orders")
            print("=========================================")
            
            if not self.count_orders():
                print(" No orders available")
                print()
            
            else:
                for i, order in enumerate(self.orders, start=1):
                
                    print(f" - {i}. {str(order['order_id'])}")
                    print(f"      {order['timestamp'].strftime("%Y-%m-%d %H:%M:%S")}")
                    print(f"      Items count: {order['count_items']}")
                    print(f"      Sum of items: {order['sum_items']}")
                    print("      Items")
                    
                    for item in order['items']:
                        print(f"       - {item['item']} x{item['count']} = {item['sum_item']}")
                        
                    print()
                            
            print(" * Press 'e' to exit to the main menu.")
            print()
            
            _select_order = input(" Make a selection >> ").casefold()

            match _select_order:
                case  "e":
                    break

                case _:
                    print()
                    print(" > Not a valid selection!")



if __name__ == "__main__":
    print("Wrong file")