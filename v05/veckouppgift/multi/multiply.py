"""
Multiplikationstabellen
Vi behöver en funktion som kan ge oss multiplikationstabellen.
Parametern "n" talar om vilket tals tabell vi ska skapa.
Parametern "limit" talar om var vi ska sluta.
Om vi till exempel frågar efter 3:ans tabell, med limit==4, ska programmet räkna ut:
3*1 = 3
3*2 = 6
3*3 = 9
3*4 = 12

multiplication_table(3, 4) → [3, 6, 9, 12]

def muliplication_table(n, limit):
    return None  # TODO

Formulera krav och acceptanskriterier.
 > AK: * Möjlighet att kunna få ut olika multiplikations tabeller för olika bas tal
       * Ingen begrändning på bas talet eller hur limit för multiplikations tabellen

   Krav: * Endast int som input både som bastal och limit 
         * Vid saknad av någon av inputs skall None retuneras
         * Vid annan datatype än int skall None retuneras
         * Default return skall ALLTID vara en lista med de korrekta värderna även 
           om det bara är ett tal
   
Kör sedan red-green-refactor för varje acceptanskriterium.
"""


def multiplication_table(n: int ="", limit: int ="") -> list[int]:
    
    if not isinstance(n, int):
        return None
    
    if not isinstance(limit, int):
        return None
    
    answers = [n*r for r in range(1, limit+1)]
    
    return answers



if __name__ == "__main__":
    print("Wrong file")