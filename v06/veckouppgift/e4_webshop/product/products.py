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

        _url = self._product_category["url"] + "?limit=10&skip=0&select=id,title,price"

        _api = Api(_url)
        _data:dict[list[dict[Any]], int, int, int] = _api()
        
        #_api = [12]
        del(_api)

        #_data = {'products': [
        #            {'id': 6, 'title': 'Calvin Klein CK One', 'price': 49.99}, 
        #            {'id': 7, 'title': 'Chanel Coco Noir Eau De', 'price': 129.99}, 
        #            {'id': 8, 'title': "Dior J'adore", 'price': 89.99}, 
        #            {'id': 9, 'title': 'Dolce Shine Eau de', 'price': 69.99}, 
        #            {'id': 10, 'title': 'Gucci Bloom Eau de', 'price': 79.99}
        #            ], 'total': 5, 'skip': 0, 'limit': 5}

        if _data != None:
            self._products = _data["products"]

    def menu_products(self):
        while True:
            something_went_wrong: bool = False
        
            print()
            print(f" Category: {self._product_category["name"]!r}")
            
            if len(self._products) == 0:
                print("  - There are no products in this category")
                    
            for i, product in enumerate(self._products, start=1):
                    print(f"  - {i}. {product['title']}, ${product['price']}")           
                
            print()
            print(f" * Press 'e' to exit the products for category {self._product_category["name"]!r}")
            print(" * Press the above number to see the product details")
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
                        product.menu_product()

                        del(product)

                    else:
                        something_went_wrong = True


            if something_went_wrong:
                print()
                print(" This is not a valid selection.")


    # Gets called when the class get deleted
    def __del__(self):
        del(self._product_category)
        del(self._products)



if __name__ == "__main__":
    print("Wrong file")