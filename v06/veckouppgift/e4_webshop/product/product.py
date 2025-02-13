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
        
        #_api = [12]
        del(_api)

        #_data = {'id': 6, 'title': 'Calvin Klein CK One', 'description': "CK One by Calvin Klein is a classic unisex fragrance, known for its fresh and clean scent. It's a versatile fragrance suitable for everyday wear.", 'category': 'fragrances', 'price': 49.99, 'discountPercentage': 0.32, 'rating': 4.85, 'stock': 17, 'tags': ['fragrances', 'perfumes'], 'brand': 'Calvin Klein', 'sku': 'DZM2JQZE', 'weight': 5, 'dimensions': {'width': 11.53, 'height': 14.44, 'depth': 6.81}, 'warrantyInformation': '5 year warranty', 'shippingInformation': 'Ships overnight', 'availabilityStatus': 'In Stock', 'reviews': [{'rating': 5, 'comment': 'Great value for money!', 'date': '2024-05-23T08:56:21.619Z', 'reviewerName': 'Sophia Brown', 'reviewerEmail': 'sophia.brown@x.dummyjson.com'}, {'rating': 3, 'comment': 'Very disappointed!', 'date': '2024-05-23T08:56:21.619Z', 'reviewerName': 'Madison Collins', 'reviewerEmail': 'madison.collins@x.dummyjson.com'}, {'rating': 1, 'comment': 'Poor quality!', 'date': '2024-05-23T08:56:21.619Z', 'reviewerName': 'Maya Reed', 'reviewerEmail': 'maya.reed@x.dummyjson.com'}], 'returnPolicy': 'No return policy', 'minimumOrderQuantity': 20, 'meta': {'createdAt': '2024-05-23T08:56:21.619Z', 'updatedAt': '2024-05-23T08:56:21.619Z', 'barcode': '2210136215089', 'qrCode': 'https://assets.dummyjson.com/public/qr-code.png'}, 'images': ['https://cdn.dummyjson.com/products/images/fragrances/Calvin%20Klein%20CK%20One/1.png', 'https://cdn.dummyjson.com/products/images/fragrances/Calvin%20Klein%20CK%20One/2.png', 'https://cdn.dummyjson.com/products/images/fragrances/Calvin%20Klein%20CK%20One/3.png'], 'thumbnail': 'https://cdn.dummyjson.com/products/images/fragrances/Calvin%20Klein%20CK%20One/thumbnail.png'}


        if _data != None:
            self._product = _data
            
    
    def menu_product(self):
        
        while True:
        
            something_went_wrong: bool = False
            
            print()
           
            print(f" {self._product['title']} (Category: {self._product['category'].title()})")
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
            
            print(f" * Press 'e' to exit the product")
            print(" * Press 'c' add the item to your cart")
            print()
            
            select_choice = input(" Enter your selection >> ").casefold()

            match select_choice:
                case "e":
                    break
            
                case "c":
                    #Add to cart
                    break
            
                case _:
                    print()
                    print(" This is not a valid selection.")


    # Gets called when the class get deleted
    def __del__(self):
        del(self._product_id)
        del(self._product)



if __name__ == "__main__":
    print("Wrong file")