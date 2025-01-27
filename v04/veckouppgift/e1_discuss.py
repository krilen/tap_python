"""
Skriv ner vad du tror kommer skrivas ut. 
Skriv sedan in koden i din IDE, exakt som den står, och kör den.
Fick du samma resultat som du trodde? Om inte, varför?

Tillsammans med Rasmus
"""

print("1a -------------------------")

# 1a
def foo(t):
    print("test")

foo("hej")

# >Skriver ut "test", ignorerar parametern

print("1b -------------------------")

# 1b
def fun1(x, y):
    return x * y

print(3, 5)

# >Skriver "3 5" inget "function call" 

print("1c -------------------------")

# 1c
def fun1(x, y):
    return x * y

print(fun1(3, 5))

# >Skriver ut "15", allt enligt spec.

print("1d -------------------------")

# 1d
def fun2(i):
    return 5 * i

x = 2
y = 3
a = fun2(fun2(x) + fun2(y))
print(a)

# >Skriver 125

print("1e -------------------------")

# 1e
a = 5
def fun3(a):
    a += 1

a += 2
print(a)

# >Skriver "7" ingen function call

print("1f -------------------------")

# 1f
def foo(i):
    return 2*i*i

def goo(x, y):
    return x(y)

a = goo(foo, 3);
print(a)

# >Skriver ut "18"

print("1g -------------------------")

# 1g Funktionen "isinstance" kan kontrollera en variabels datatyp. 
# Vad gör funktionen is_number? Går det att förbättra koden?

def is_number(x):
    if isinstance(x, int):
        return True
    elif isinstance(x, float):
        return True
    return False

print(is_number(5.5))
print(is_number(42))
print(is_number("Hello")) # False

# > Kontrollerar om parametern är en int eller float och skickar tillbaka
#   'True' som ett svar annars 'False'
#   Dålig return värde, det säger inget vad ör typ av värde förutom att
#   både 'float' och 'int' får i return som 'True' och allt annat 'False'

print("1h -------------------------")

# 1h
def average_words(strings):
    found = []
    for item in strings:
        if 4 < len(item) < 8: # 5 till 7
            found.append(item)
    return found

selected_words = average_words(["sup", "how's", "it", "going", "reflecting", "on", "programs", "and", "coding"])
print(*selected_words )

# > Egentligen inget eftersom inte någon 'print' finns men om det fanns så skulle
#   alla ord som har en längt mellan 5 och 7 retuneras i en lista

print("1g -------------------------")

# 1g
"""
En uppgift i tre delar:
 1. Lista ut vad som är funktionens syfte, baserad på namn och sammanhang.
    > Loppar igenom en lista men nummer och retunerar en sträng som förklara 
      vilken siffra i listan som var minst
      
 2. Lista ut vad som ska vara det förväntade resultatet för de tre testlistorna.
    > Se nedan
    
 3. Rätta felen, så funktionen gör det den ska.
    > * If sats för att unvika tomma listion som input
      * Ändra vad som anses vara första jämföresle vårdet
      * Ta bort return
    
"""

def find_min(numbers):
    
    if len(numbers) == 0:
        print("No numbers avaiable")
    
    else: 
        counter = numbers[0]
        for item in numbers[1:]:

            if item < counter:
                counter = item
    
        print(f"The smallest item is: {counter}")


find_min([10, 3, -4, -11]) # > -11
find_min([])  # > 0
find_min([100]) # > 0

find_min([-2, 2, 3, -1, 1]) # Extra för kontroll


