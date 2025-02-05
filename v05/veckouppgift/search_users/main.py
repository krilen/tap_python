from users import autocomplete

def main():
    
    for user in show_usernames:
    
        print("Search for '", user, sep="", end="' ")
        print("found '", autocomplete(user, usernames), sep="", end="' ")
        print("as possible matches.")


if __name__ == "__main__":
        
    usernames = ["JohnSmith", "LauraDoe", "EmilyJohnson", "MichaelBrown", "SarahDavis",
                "DavidClark", "JessicaTaylor", "JamesMartinez", "OliviaWilson",
                "DanielAnderson", "SophiaThomas", "MatthewDoe", "JohnJackson", 
                "EthanWhite", "IsabellaHarris", "DavidLewis", "ChloeTaylor", 
                "BenjaminYoung", "MiaSmith", "WilliamScott"]
    
    show_usernames = ["John", "", "Scott", 12, "david", "Isa"]
    
    main()