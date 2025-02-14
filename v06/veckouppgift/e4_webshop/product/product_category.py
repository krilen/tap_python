from api.api import Api
from product.products import Products

class ProductCategory():
    """
    A class the handles different product classes that exists
    """

    def __init__(self) -> None:
        self._product_categories = []
        
        _api = Api("https://dummyjson.com/products/categories")
        _data = _api()
        del(_api)

        if _data != None:        
            self._product_categories = _data


    @property
    def product_categories(self):
        """
        A getter for the different product categories
        Return a list of the avaible product categories, no categories no need to continue
        """
        return self._product_categories
    

    def menu_product_categories(self, cart):
        
        while True:
            something_went_wrong: bool = False

            print()
            print(" List of available product categories")

            for i, category in enumerate(self._product_categories, start=1):
                print(f"  - {i}. {category['name']}")

            print()
            print(" * Press the above number to see products in that category.")
            print(" * Press 'e' to exit to the main menu.")
            print()
            

            select_category = input(" Enter your selection >> ").casefold()

            if select_category == "e":
                break
            
            else:
                try:
                    select_category_nr = int(select_category)

                except:
                    something_went_wrong = True

                else:
                    if select_category_nr <= len(self._product_categories):
                        products = Products(self._product_categories[select_category_nr -1])
                        cart = products.menu_products(cart)

                        del(products)

                    else:
                        something_went_wrong = True

            if something_went_wrong:        
                print()
                print(" > That was not a valid selection.")

        return cart


if __name__ == "__main__":
    print("Wrong file")