from typing import Any

# 6
"""
Lös felen i koden.
"""
def increase(x):
    x += 1
    return x


# 7
"""
Bygg en funktion med namnet average. Den ska ta parametrar: x och y. Båda ska vara tal.
Funktionen ska returnera medelvärdet. 
Till exempel så räknar man ut medelvärdet av 4 och 8 genom med formeln: (4 + 8) / 2, vilket blir 6.
"""
def average(x: int, y: int) -> int:
    return (x +y ) /2


# 8
"""
Gör en funktion som kan skriva ut innehållet i en lista lite snyggare. 
Först ska funktionen tala om ifall listan är tom, eller hur många element den har. 
Sedan ska funktionen skriva ut elementen i en punktlista. 
"""
def pretty_print(elements: list[Any]) -> None:
    
    if not elements:
        return None
    
    print(f"Listan har {len(elements)} elements:")
    
    for i, element in enumerate(elements, start=1):
        print(f" {i}. {element}")
        
    print()
        
    return None


if __name__ == "__main__":
    print("Wrong file to execute")