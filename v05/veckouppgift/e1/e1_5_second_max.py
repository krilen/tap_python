"""
5 Winner takes it all brukar det ju heta, men nu ska vi försöka ge lite heder åt alla andrapristagare. Formulera testfall för en funktion som hittar näst största talet i en lista!
# Returnerar det nästa största talet i listan
# Returnerar None om det inte finns något
# Om det är delad förstaplats så returneras det talet
"""

def find_2nd_max(list_numbers: list[int]=[]) -> None | int:
    if not isinstance(list_numbers, list):
        return None
    
    if not list_numbers:
        return None
    
    # Eftersom en ny lista skapas behövs ingen '<list>.copy()'
    # göras för att säkerställa att orginal listan inte påverkas
    check_list_numbers = [ n for n in list_numbers if isinstance(n, int) ]

    if len(check_list_numbers) > 1:
        check_list_numbers.sort()
        
        return check_list_numbers[-2]
    
    else:
        return None
