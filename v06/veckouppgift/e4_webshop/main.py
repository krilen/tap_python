from product.product_category import ProductCategory
from cart.cart import Cart
from order.order import Order

import sys
from typing import Any


def main():
    product_category = ProductCategory()
    product_categories = product_category.product_categories

    if len(product_categories) == 0:
        print("Sorry we are having some issues, try again later")
        sys.exit()

    cart = Cart()
    order = Order()

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
                cart = product_category.menu_product_categories(cart)

            case "c":
                cart.menu_cart_all(order)
                
            case "o":
                order.menu_order_all()

            case _:
                print()
                print(" > That was not a valid selection.")

    print()
    print(" Thank you for visiting our shop")
    sys.exit()



if __name__ == "__main__":
    main()