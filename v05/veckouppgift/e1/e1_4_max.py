"""
4 Formulera testfall för en funktion som hittar största talet i en lista.
# Returnerar det största talet i listan
# Returnerar None om det inte finns något
"""

def find_max(list_numbers: list[int]=[]) -> None | int:
    if not isinstance(list_numbers, list):
        return None
    
    if not list_numbers:
        return None
    
    return(max(list_numbers))