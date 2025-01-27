# 1
def print_string(name: str) -> None:
    """
    Skriv en funktion som tar en sträng som parameter. 
    När den anropas ska den skriva ut strängen och 'är en fena på programmering'."
    """
    
    print(f"{name} är en fena på programmering")
   
    
# 2 A, B"
def eko(string: str, count: int) -> None:
    """
    A: Skriv en funktion med namnet "eko". När den anropas med en sträng ska den upprepa strängen, och skriva ut resultatet
    B: Lägg till en parameter "count", som avgör hur många ekon som ska skapas.
    """
    print(string * count)


if __name__ == "__main__":
    print("Wrong file to execute")