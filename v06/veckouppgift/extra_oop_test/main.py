from order.order import Order
from cart.cart import Cart

def main():
    
    c = Cart()
    o = Order()
    
    while True:
        
        print()
        print(" Main menu")
        print("=========================================")
        print(" * Press 'a' to add items to the cart.")
        print(" * Press 'v' to view the items in the cart.")
        print(" * Press 'o' to see the order.")
        print(" * Press 'q' to quit.")
        print()
        
        select_main = input(" Make a selection >> ").casefold()
        
        match select_main:
        
            case "q":
                break
            
            case "a":
                c.menu_cart_submit()
                
            case "v":
                c.menu_cart_view(o)
                
            case "o":
                o.menu_orders()
                
            case _:
                print()
                print(" Not a valid selection!")
                
            

    
    print()
    print(" Have a nice day")
    print()


if __name__ == "__main__":
    main()