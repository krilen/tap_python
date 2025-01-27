"""
Skriv in koden i din IDE, exakt som den står, och kör den.

1 Vad skrivs ut?  
    > Skriver ut 6 gånger siffror: 5,7,9,11,13 och 15
2 Vad skrivs ut?  
    > Skriver ut 0 till 9 utan 5
3 Vad blir summan? Skriv ner din bästa gissning _innan_ du kör koden.  
    > Skriver ut 6
4 Vad skrivs ut?  
För att förstå koden kan du sätta ut brytpunkter och köra med debugging. 
Det kan också underlätta att skriva samtidigt med papper och penna.  
    > Skriver ut ...
5 Vad skrivs ut?
    > Skriver ut "_tim"
Kan du göra om koden så att den skriver ut "time" i stället?  
    > Öka slice "stop" med 1 dvs till 8

6 Vad skrivs ut?  
Kan du flytta linjen ett steg åt höger?  
~~~
for y in range(1, 7):  
    s = ""  
    for x in range(1, 9):  
        if x == y:  
            s += "\#"  
        else:  
            s += "."  
    print(s)
~~~
    > Efter som variablen 'y' hanterar den horisontella placeringen bör det ökas 
      med 1 om den skall placeras ett steg till höger.
 
 
"""

print("Nr 1 --------------------------")

limit = 15
index = 5

while index <= limit:
    print(index)
    index = index + 2
    
print("\n\nNr 2\n--------------------------")

for i in range(10):
    if i == 5:
        print("")
    else:
        print(i)
        
    i = i + 1

print("\n\nNr 3\n--------------------------")

counter = 0
for i in range(6):
    counter += i

print(counter)

print("\n\nNr 4\n--------------------------")

x = 0
y = 1

while y < 10:
    if y % 2 == 0:
        x -= y 
    else:
        x += y * y
    y += 1
    
print("\n\nNr 5\n--------------------------")

message = "its_time_to_get_coding"
print(message[3:8])

print("\n\nNr 6\n--------------------------")


for y in range(1, 7):
    s = ""
    for x in range(1, 9):
        if x == y+1:       # <-- från 'if x == y'
            s += "#"
        else:
            s += "."
    print(s)

