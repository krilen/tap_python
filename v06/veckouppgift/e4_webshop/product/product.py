from api.api import Api

from typing import Any



class Product():
    """
    A class that handles a single product
    """
    
    def __init__(self, product_id):
        self._product_id = product_id
        self._product = {}

        _url = "https://dummyjson.com/products/" + str(self._product_id)

        _api = Api(_url)
        _data: dict[list[dict[Any]], int, int, int] = _api()
        del(_api)

        if _data != None:
            self._product = _data
            
    
    def menu_product(self, cart):
        
        while True:
        
            something_went_wrong: bool = False
            
            print()
           
            print(f" {self._product['title']} ({self._product['category'].title()})")
            print()
            
            # Spliting the describtion of the product into multirow but only by the spaces
            desc_split = 45
            desc = " "
            desc_split_lower = 0
            desc_split_upper = desc_split
            
            while True:
                pos_space = 0
                
                if desc_split_upper < len(self._product['description']):
                    pos_space = self._product['description'].find(" ", desc_split_upper)
                    
                else:
                    pos_space = -1
                    
                if pos_space >= 0:
                    desc += self._product['description'][desc_split_lower:pos_space]
                    desc += "\n "

                elif pos_space == -1:
                    desc += self._product['description'][desc_split_lower:]
                    break
            
                desc_split_lower = pos_space +1
                desc_split_upper = pos_space +1 +desc_split

            print(desc)
            print()
            
            print(" Dimensions:")
            print(f"  - weight: {self._product['weight']}")
            print(f"  - height: {self._product['dimensions']['height']}")
            print(f"  - width:  {self._product['dimensions']['width']}")
            print(f"  - depth:  {self._product['dimensions']['depth']}")
            print()
            
            print(f" Price: ${self._product['price']} ({self._product['availabilityStatus'].lower()})")
            print()
            
            if self._product["stock"] > 0: 
                print(" * Press 'a' add the item to your cart.")
            
            print(" * Press 'e' to exit to the products.")
            print()
            
            select_choice = input(" Enter your selection >> ").casefold()
            
            if select_choice == "a" and self._product["stock"] == 0:
                select_choice = "x"

            match select_choice:
                case "e":
                    break
            
                case "a":
                    cart.shopping = {"id": self._product["id"], 
                                     "title": self._product["title"],
                                     "category": self._product["category"],
                                     "count": 1, 
                                     "price": self._product["price"], 
                                     "sum_price": self._product["price"]}
                    
                    print()
                    print(" > The product has been added to your cart!")
            
                case _:
                    print()
                    print(" > That was not a valid selection.")

        return cart
    

    # Gets called when the class get deleted
    def __del__(self):
        del(self._product_id)
        del(self._product)



if __name__ == "__main__":
    print("Wrong file")