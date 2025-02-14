from api.api import Api
from product.product import Product

from typing import Any


class Products():
    """
    A class that handles multiple products
    """
    
    def __init__(self, product_category):
        self._product_category = product_category
        self._products = []

        _url = self._product_category["url"] + "?limit=20&skip=0&select=id,title,price"

        _api = Api(_url)
        _data:dict[list[dict[Any]], int, int, int] = _api()
        del(_api)

        if _data != None:
            self._products = _data["products"]


    def menu_products(self, cart):
        while True:
            something_went_wrong: bool = False
        
            print()
            print(f" Category: {self._product_category['name']}")
            
            if len(self._products) == 0:
                print("  - There are no products in this category")
                    
            for i, product in enumerate(self._products, start=1):
                    print(f"  - {i}. {product['title']}, ${product['price']}")           
                
            print()
            print(" * Press the above number to see the product details.")
            print(" * Press 'e' to exit to the product categories.")
            print()
            
            select_product = input(" Enter your selection >> ").casefold()

            if select_product == "e":
                break
            
            else:
                try:
                    select_product_nr = int(select_product)

                except:
                    something_went_wrong = True

                else:
                    if select_product_nr <= len(self._products):

                        product = Product(self._products[select_product_nr  -1]["id"])
                        cart = product.menu_product(cart)

                        del(product)

                    else:
                        something_went_wrong = True


            if something_went_wrong:
                print()
                print(" > That was not a valid selection.")

        return cart

    # Gets called when the class get deleted
    def __del__(self):
        del(self._product_category)
        del(self._products)



if __name__ == "__main__":
    print("Wrong file")