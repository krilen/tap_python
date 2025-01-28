"""
Spelet 21
Om man lägger ihop talen 1 + 2 + 3 + 4 + …  så kommer talens summa att bli större och större. 
Förr eller senare kommer man förbi 21. Skriv en funktion som skriver ut det första talet i 
talserien som är större än 21.

Version 2: i stället för att använda talserien, slumpa tal mellan 1 och 13. (talen i en vanlig kortlek)
Tips: importera modulen random och använd funktionen randint för att slumpa tal. 
Exempel: card = random.randint(1, 13)

Möjlig vidareutveckling: bygg ett spel som frågar användaren om man vill ta ett nytt kort
eller stanna. (slumpa ett tal) Gör så att datorn kan simulera en motståndare. Målet är att 
vinna över datorn.
"""
from typing import Tuple


# Version 1
def check_total(total: int, increase: int) -> Tuple[bool, int]:
    
    total += increase
    
    if total > 21:
        print(f"First number to increase after 21: {increase}")
        return True, total
    
    return False, total


increase_by = 1
total = 0

while True:
    
    check, total = check_total(total, increase_by)
    
    if check:
        break
    else:
        increase_by += 1



# Version2
import random

total2 = 0
increase_by2 = random.randint(1, 13)

while True:
    
    check, total2 = check_total(total2, increase_by2)
        
    if check:
        break
    else:
        increase_by2 += 1