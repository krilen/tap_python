"""
4 Betrakta funktionen is_sorted_ascending(numbers). 
Den ska returnera True om listan numbers är sorterad i stigande ordning, False annars.

4a Vilka ekvivalensklasser har numbers?
 > * True
   * False

4b Formulera krav och acceptanskriterier för funktionen.
 > * Funktionellt krav
   * User story, Tasks, task: ---
   * Acceptanskriterier
      - Skall bara svara på om listan med tal är sorterad i stigande ordning
   * Krav
      - Säkerställ att input är en "lista" om det inte är det skall False retuneras
      - Om andra datatyper än tal (int eller float) får inte finnas med i listan då retuneras False
      - Säkerställ att listan innehåller 1 eller mera tal



4c Skriv testfall för funktionen.

"""
from typing import Any

def is_sorted_ascending(numbers: list[int | float] = []) -> False | True:
    if not isinstance(numbers, list):
        return False
    
    if not numbers:
        return False
    
    # Creates a seperate list of anything except numbers (int and float)
    check_none_numbers: list[Any] = [number for number in numbers if not isinstance(number, (int, float))]
    
    if check_none_numbers:
        return False
    
    check: bool = True
    check_number = numbers[0]
    
    for number in numbers[1:]:
        if check_number < number:
            check_number = number
            
        else:
            check = False
            break
    
    return check