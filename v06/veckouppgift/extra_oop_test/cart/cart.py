from typing import Any
import random

class Cart():
    
    def __init__(self) -> None:
        """
        Sets up an empty list for holding the items and variable for the sum
        of the items
        """
        self._cart: list[dict[Any]] = []
        self._sum_cart: int = 0


    # Cart getter
    @property
    def shopping_cart(self) -> list[dict[Any]]:
        """
        Returns the items in the cart
        """        
        return self._cart
    

    # Cart setter    
    @shopping_cart.setter
    def shopping_cart(self, item: dict[Any]) -> None:
        """
        Adds an items to the list of items
        """
        self._cart.append(item)


    # Cart deleter
    @shopping_cart.deleter
    def shopping_cart(self) -> None:
        """
        Resets the cart list with an empty list
        """
        self._cart = []
        

    # Cart count
    def count_cart(self) -> int:
        """
        Returns the number of items in the cart
        """
        return len(self.shopping_cart)
    
    
    # Delete item in the cart 
    def delete_item(self, index: int) -> None:
        """
        Removes an items at a certain index and calls for the sum of items to be calculated
        """
        _count: int = self.count_cart()
        
        if _count and index < _count:
            self._cart.pop(index)
            self.calc_sum_cart()
    
    
    # Clean up the cart
    def cleanup_cart(self) -> None:
        """
        Method to reduse the items by putting the duplicates together
        """
        
        _unique_items: list[int] = list(set([n["item"] for n in self.shopping_cart]))
        
        if len(_unique_items) != self.count_cart():
            
            _new_cart = []
            
            for _unique_item in _unique_items:
                _items = [i for i in self._cart if i["item"] == _unique_item]
                _count = sum([i["count"] for i in _items])
                
                _item = _items[0]
                _item["count"] = _count
                _item["sum_item"] = _unique_item * _count
                
                _new_cart.append(_item)
                
            self._cart = _new_cart

            
    # Sum the cart
    def calc_sum_cart(self):
        """
        Method to sum up the items in the cart
        """
        self._sum_cart = sum([i["sum_item"] for i in self.shopping_cart])
            
    
    # Menu for the cart submit
    def menu_cart_submit(self):
        """
        Menu for adding items to the cart
        """
        
        while True:
            number = random.randint(0, 10)
            
            print()
            print(" Cart menu")
            print("=========================================")

            print(f" The random number was: '{number}'.")
            print()

            print(" * Press 's' to submit the number as an item to the cart >> ")
            print(" * Press 'c' to count the items of items in the cart")
            print(" * Press 'e' to exit to the main menu.")

            print()
            
            _select_cart_submit = input(" Make a selection >> ").casefold()
            
            match _select_cart_submit:
                case "e":
                    break
                
                case "s":
                    _count_cart_before = self.count_cart()
                    
                    self.shopping_cart = {"item": number, "count": 1, "sum_item": number}
                    
                    if not _count_cart_before < self.count_cart():
                        print()
                        print(" > ERROR: Item was not added to the cart")
                        
                    else:
                        print()
                        print(f" > Item was added to the cart")
                        
                case "c":
                    print()
                    print(f" > The number of items in the cart is: {self.count_cart()}")
                        
                case _:
                    print()
                    print(" > Not a valid selection!")
                    
    
    # Menu for the cart view
    def menu_cart_view(self, order):
        """
        Menu for view the cart of items, deleting items and creating an order
        """
        
        self.cleanup_cart()
        self.calc_sum_cart()
        
        while True:
            
            _something_went_wrong = False
            
            print()
            print(" Cart items")
            print("=========================================")
            
            if not self.count_cart():
                print(" No items in the cart")
            
            else:
                for i, n in enumerate(self.shopping_cart, start=1):
                
                    print(f" - {i}. Item: {n['item']} x{n['count']}")
                    
                print()
                print(f" The sum of items in the cart is: {self._sum_cart}")

            print()
            
            if self.count_cart():
                print(" * Press the number of the item that you wish to delete")
                print(" * Press 'o' to move the items in the cart to order.")
            
            print(" * Press 'e' to exit to the main menu.")
            
            print()
            
            _select_cart_view = input(" Make a selection >> ").casefold()

            if _select_cart_view == "e":
                break
            
            elif _select_cart_view == "o":
                order.insert_order(self.shopping_cart)
                del(self.shopping_cart)
                break
                
            else:
                
                try:
                    _item_remove_nr = int(_select_cart_view)
                    
                except:
                    _something_went_wrong = True
                    
                else:
                    
                    if 1 <= _item_remove_nr <= self.count_cart():
                        self.delete_item(_item_remove_nr -1)
                    
                    else:
                        _something_went_wrong = True
            
            if _something_went_wrong:
                print()
                print(" > Not a valid selection!")

        
        
if __name__ == "__main__":
    print("Wrong file")