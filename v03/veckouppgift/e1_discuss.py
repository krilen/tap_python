"""
Skriv in koden i din IDE, exakt som den står, och kör den.

1 Vad skrivs ut?  


2 Vad skrivs ut?  

3 Vad blir summan? Skriv ner din bästa gissning _innan_ du kör koden.  


4 Vad skrivs ut?  
För att förstå koden kan du sätta ut brytpunkter och köra med debugging. Det kan också underlätta att skriva samtidigt med papper och penna.  

5 Vad skrivs ut?  
Kan du göra om koden så att den skriver ut "time" i stället?  


6 Vad skrivs ut?  
Kan du flytta linjen ett steg åt höger?  
for y in range(1, 7):  
 s \= ""  
 for x in range(1, 9):  
 if x \== y:  
 s \+= "\#"  
 else:  
 s \+= "."  
 print(s)
"""


"""
limit = 15
index = 5

while index <= limit:
    print(index)
    index = index + 2
    
""" 
    
""""
for i in range(10):
    if i == 5:
        print("")
    else:
        print(i)
        
    i = i + 1

"""

"""
counter = 0
for i in range(6):
        counter += 1

print(counter)

"""


x = 0
y = 1

while y < 10:
    if y % 2 == 0:
        x = y # Tips: sätt en brytpunkt här
    else:
        x += y * y # och här
    y += 1
    
    