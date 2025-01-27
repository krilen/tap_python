from typing import Any

# 4 
def last(elements: list[Any]) -> Any:
    """
    Skriv en funktion med namnet last. 
    Den ska ta en lista som parameter och returnera det sista elementet i listan.
    """
    
    if elements:
        return elements[-1]

    return None


# 5
def cut_edges(elements: list[Any]) -> list[Any]:
    """
    Skriv en funktion med namnet cut_edges. Den ska ta en lista som parameter. 
    När den anropas ska den returnera en ny lista, där den har tagit bort första och sista elementet.
    """
    if len(elements) > 1:
        return elements[1:-1]
    
    return []














if __name__ == "__main__":
    print("Wrong file to execute")