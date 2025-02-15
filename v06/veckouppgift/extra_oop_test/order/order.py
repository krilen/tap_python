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
        
        Input from cart
            '[{'item': <int>, 'count': <int>, 'sum_item': <int>}, ...]'
        Many dict (objects) within a list
        
        Inserted into order
            [{'order_id': UUID('847fe6d3-5402-4a95-8cca-a36764bbbef6'), 'items': [{'item': 9, 'count': 1, 'sum_item': 9}], 'count_items': 4, 'sum_items': 15, 'timestamp': datetime.datetime(2025, 2, 15, 16, 8, 0, 463768)}]
        The dict from the cart gets added to items and additional stuff like uuid, count, sum and date also gets added
        
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
                
                    print(f" - {i}. Order ID: {str(order['order_id'])}")
                    print(f"      Date: {order['timestamp'].strftime("%Y-%m-%d %H:%M:%S")}")
                    print(f"      Items count: {order['count_items']}")
                    print(f"      Sum of items: {order['sum_items']}")
                    print()
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