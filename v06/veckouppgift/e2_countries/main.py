"""
2 Länder
"""


class Country:
    
    def __init__(self, name, pop, area=None):
        self.__name = name
        self.__population = pop
        self._area = area   # Sätter det inte som hemligt utan bara som info att detta har man inget att göra med
        self._language = [] # Miss av mig självklart skall det vara 'self._language' och inte 'self.language'
        
        
    def print_info(self):
        """
        Prints a summary
        """
        print(f" * I {self.__name} bor det {self.__population} miljoner invånare", end="")
        
        if self._area:
            print(f" med en area på {self._area} tusen km2.", end="")
        
        print()
        
        if self.language:
            print("    - Officiella språk i", end=" ")
            print(self.__name, "är:", end=" ")
            print(*self.language, sep=",")
        
        
    @property
    def language(self):
        return self._language
        
    @language.setter
    def language(self, lang):
        self._language = lang
        
    
            

se = Country("Sverige", 10.5, 450)
no = Country("Norge", 5.5)

"""
1a På Island bor det 383726 invånare och i Danmark 5961249. Skapa objekt för länderna.
(Data från januari 2024. Avrunda befolkningen.)

"""
island = Country("Island", 0.4)
danmark = Country("Danmark", 5.9, 42)

"""
1b Lägg till en metod med namnet "print_info". 
Om man anropar den för Sverige-objektet ska den skriva ut: "I Sverige bor det 10.5 miljoner invånare".
Funktionen ska använda sina egenskaper, så att den fungerar för de andra länderna också.
"""
# > Se i class Country
se.print_info()
no.print_info()
island.print_info()
danmark.print_info()


"""
1c Lägg till landets area som en egenskap till klassen. Använd en parameter till konstruktorn, 
alltså __init__ metoden. Ge arean ett default värde på None så att man inte måste ange arean när man
skapar ett landsobjekt.

Exempel på default värde för en vanlig funktion:
# y har default värde 10
def exempel(x, y=10):
    print(x + y)

exempel(2)  # skriver ut 12
"""
# > Se i class Country


"""
1d Ändra i metoden "print_info" så att den skriver ut arean också, men bara om arean inte är None.
"""
# > Se i class Country


"""
1e Skapa en ny metod med namnet "add_language". Den ska lägga till ett av landets officiella språk. 
(Sverige har bara ett, men Finland har två språk (svenska och finska) och Schweiz har fyra.) 
För att kunna spara ett varierande antal behöver du använda en lista.
"""
# > Se i class Country

"""
1f Ändra i "print_info" så att den skriver ut alla officiella språk, på en ny rad.
"""
# > Se i class Country

finland = Country("Finland", 45.6, 338)
finland.language = ["svenska, finska"]

finland.print_info()

se.language = ["svenska"]
se.print_info()