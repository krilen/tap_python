"""
2 Det har smugit sig in kommentarer i stället för kod på några ställen. Skriv färdigt testfallen test_empty_list och test_number_list.
Returnerar summan av alla tal i listan
"""

def sum_list(list):
    if not list:
        return None
    
    return sum(list)
