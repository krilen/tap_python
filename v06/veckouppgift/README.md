# Veckouppgift 6

## Vecka 6, 10/2

*1 Du ska lösa uppgiften självständigt eller tillsammans med en annan student. Men vid minst ett tillfälle ska du göra code review i en grupp.*

*2 Du får ta hjälp av AI för att förklara koncept och lösa fel. Du får inte be AI lösa uppgiften åt dig direkt. Om du gör det, kommer du inte att lära dig grunderna, och inte kunna lösa svårare problem.*

---

### 1 Läsa och förstå kod \- diskutera i grupp

Skriv ner vad du tror kommer skrivas ut. Skriv sedan in koden i din IDE, exakt som den står, och kör den. Fick du samma resultat som du trodde? Om inte, varför?

1 Vad gör följande kod?  
class SafeStorage:  
    \_\_data \= None  
    def get(self):  
        return self.\_\_data  
    def put(self, data):  
        self.\_\_data \= data

safe \= SafeStorage()  
safe.put("Anakonda")  
x \= safe.get()  
safe.put("Boaorm")  
y \= safe.get()  
print(x, y)

2a Vad gör följande kod? Fixa eventuella fel.  
class Animal:  
    def make\_noise(self):  
        print("Detta djur har vi inget ljud för.")

class Dog(Animal):  
    def make\_noise(self):  
    print("Voff\!")

class Cat(Animal):  
    def make\_noise(shelf):  
        super().make\_noise()  
        print("Mjau\!")

def sound\_off(animal):  
    animal.make\_noise()

c \= Cat()  
d \= Dog()  
h \= Rooster()  
sound\_off(\[c, d, h\])

2b Lägg till en klass för ett annat djur, till exempel en guldfisk.

---

### 2 Länder

1a På Island bor det 383726 invånare och i Danmark 5961249\. Skapa objekt för länderna. (Data från januari 2024\. Avrunda befolkningen.)  
class Country:  
    def \_\_init\_\_(self, name, pop):  
        self.\_\_name \= name  
        self.\_\_population \= pop

se \= Country("Sverige", 10.5)  
no \= Country("Norge", 5.5)

1b Lägg till en metod med namnet "print\_info". Om man anropar den för Sverige-objektet ska den skriva ut: "I Sverige bor det 10.5 miljoner invånare". Funktionen ska använda sina egenskaper, så att den fungerar för de andra länderna också.

1c Lägg till landets area som en egenskap till klassen. Använd en parameter till konstruktorn, alltså \_\_init\_\_ metoden. Ge arean ett *default värde* på None så att man inte måste ange arean när man skapar ett landsobjekt.  
Exempel på default värde för en vanlig funktion:  
\# y har default värde 10  
def exempel(x, y\=10):  
    print(x \+ y)

exempel(2)  \# skriver ut 12

1d Ändra i metoden "print\_info" så att den skriver ut arean också, men bara om arean inte är None.

1e Skapa en ny metod med namnet "add\_language". Den ska lägga till ett av landets officiella språk. (Sverige har bara ett, men Finland har två språk (svenska och finska) och Schweiz har fyra.) För att kunna spara ett varierande antal behöver du använda en lista.

1f Ändra i "print\_info" så att den skriver ut alla officiella språk, på en ny rad.

---

### 3 Banken

Skapa en klass som representerar ett bankkonto. Banken ska kunna:

* sätta in pengar (deposit)  
* ta up pengar (withdraw)  
* returnera nuvarande saldo (balance)  
* räkna ut ränta (apply\_interest, lägger till räntan till kontot)  
* tala om ifall man har råd att betala en räkning (returnera True/False)

Gör en metod för varje funktion.

Skriv enhetstester för varje funktion. Använd gärna TDD-metoden, att börja med testfallen innan du skriver koden.

---

### 4 Webbshop

Skapa klasser som representerar en webbshop:

* produkter (Product)  
* beställningar (Order)  
* kundvagn (ShoppingCart)

Tips 1\! Ge varje klass en egenskap "\_\_id". Man kan använda den för att referera till ett annat objekt. Detta behövs eftersom både kundvagn och beställningar kommer att innehålla befintliga produkter.

Tips 2\! Du kan använda AI för att skapa realistisk testdata. Prova till att börja med:  
"Skapa testdata för 10 produkter till en webbshop, som säljer verktyg. Visa datan i en tabell. Varje produkt ska ha namn, pris och ett unikt id."  
---

---

.