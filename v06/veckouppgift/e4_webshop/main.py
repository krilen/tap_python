from product.product_category import ProductCategory

import sys
from typing import Any


def main():
    product_category = ProductCategory()
    product_categories = product_category.product_categories

    if len(product_categories) == 0:
        print("Sorry we are having some issues, try again later")
        sys.exit()

    cart: list[dict[Any]] = []

    # Welcome menu
    print()
    print(" ****** Welcome to DummyShop ******")
    print(" Sponsered by: https://dummyjson.com")

    while True:
        # Main menu
        print()
        print(" * Press 'p' to see the product categories.")
        print(" * Press 'c' to see your cart with products.")
        print(" * Press 'o' to see your orders.")
        print(" * Press 'q' to quit.")
        print()

        select = input(" What would you like to do? >> ").casefold()

        match select:
            case "q":
                break
        
            case "p":
                # The user selected to see the product category
                cart = product_category.menu_product_categories(cart)

            case _:
                print()
                print(" This is not a valid selection.")



    print()
    print(" Thanks for visiting our shop")
    sys.exit()



if __name__ == "__main__":
    main()