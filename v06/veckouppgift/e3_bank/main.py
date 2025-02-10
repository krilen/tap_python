from account import *
from menu import *



def main():
    
    print(" ***** Welcome to simple ATM *****")

    
    while True:
        
        select: str = input("\n Choose what you want to do >> ")
        
        
        
        if select == "q":
            break
        

    print("\n Thank you for using simple ATM\n")


if __name__ == "__main__":
    main()