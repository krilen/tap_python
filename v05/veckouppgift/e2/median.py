"""
3a Betrakta funktionen find_median(numbers), som tar en lista med tal och returnerar medianen.
Median är det mittersta talet, t.ex. är medianen 2 för listan [1, 2, 1000].
Om listan har jämnt antal element ska funktionen returnera medelvärdet av de två mittersta talen.
Formulera de krav och acceptanskriterier (AK) som ska gälla för funktionen.
 > * Funktionellt krav: ser inte detta som något som en användare skulle kunna behöva eller behöva ange en input för
   * User story, Tasks, task: ---
   * Acceptanskriterier
      - Medianan av en lista med tal skall fås tillbaka
      - Om ingen tal finns eller andra datatyper som inte är int eller float skall en median inte fås ut
      - DEt är upp till vad som använder funktionen att runda av eventuell beräknad median inte funktiones uppgift
   * Krav
      - Säkerställ att input är en "lista" om det inte är det skall None retuneras
      - Säkerställ att innehållet i en lista är tal, om annat skall None retuneras
      - Säkerställ att en tom lista retuneras som None
      - Talet i mitten är median och skall retuneras
      - Om listan är av jämnt antal tal skall medel av de två mellesta talen retuneras
      - annars skall None retuneras


3b Skriv testfall som testar alla AK.

3c Implementera funktionen, så att alla testfall blir gröna.

"""
from typing import Any


def find_median(numbers: list[int | float] = []) -> None | float:
    if not isinstance(numbers, list):
        return None
    
    if not numbers:
        return None
    
    # Creates a seperate list of anything except numbers (int and float)
    check_none_numbers: list[Any] = [number for number in numbers if not isinstance(number, (int, float))]
    
    if check_none_numbers:
        return None
    
    nr_numbers: int = len(numbers)
    middle_nr = nr_numbers // 2

    if nr_numbers % 2 == 0:
        return (sum(numbers[middle_nr -1: middle_nr +1]) /2)
    
    else:
        return numbers[middle_nr]
