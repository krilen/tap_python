def main()->None:
    name:str = input("Please enter you name >> ")
    
    try:
        number:int = int(input("Please enter a number >> "))
    # Capture ALL errors not only ValueError
    except:
        print("That was not a valid number, I will help you")
        number = 0

    print(f"Your name is {name.title()!r} and your number plus one is {str(number+1)!r}.")



if  __name__ == "__main__":
    main()