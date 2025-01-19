"""
5 Miniräknare

1 Gör ett program som frågar användaren efter 3 tal. Sedan ska det räkna ut vad summan
blir, och skriva ut på konsolen. (summa: tal1 + tal2 + tal3)

2 Programmet ska tala om vilket som är det största talet, utan att använda
Python-funktionen max. Använd i stället if/elif/else. Fundera på om man kan lösa uppgiften
på olika sätt.

3 Programmet ska tala om ifall två av talen är lika, eller alla tre är lika.

4 Programmet ska tala om vilket som är det mellersta talet. Observera att det bara finns ett
mellersta tal om alla tre är olika, eller alla tre är lika. (Om talen skulle vara till exempel 2, 2,

5 så räknas inget av dem som mellerst i den här uppgiften.)För att testa systematiskt kan du göra en tabell. Kör sedan programmet. Kontrollera att
programmet skriver ut samma saker som du har skrivit in i tabellen. Vi kallar talen t1, t2
och t3.

Förslag på värden att testa med: 1 2 3, 1 3 2, 3 2 1, -1 -3 -1, 9 9 9, 32 32 16

+-----+-----+-----+--------+-----------+-----------+----------+
| t1  | t2  | t3  | Störst | Två lika? | Tre lika? | Mellerst |
+-----+-----+-----+--------+-----------+-----------+----------+
|  1  |  2  |  3  |    3   |    nej    |    nej    |    2     |
+-----+-----+-----+--------+-----------+-----------+----------+

"""

while True:
    try:
        print("Give me three numbers!")
        num_1: int = int(input("Number 1? >> "))
        num_2: int = int(input("Number 2? >> "))
        num_3: int = int(input("Number 3? >> "))
        
    except ValueError:
        print("That was not valid numbers!\n")
        
    else:
        break
    
print(f"\nSum of: {num_1} + {num_2} + {num_3} is {num_1 +num_2 +num_3}.\n")

biggest_num: int = None

if num_1 > num_2 and num_1 > num_3:
    print(f"{num_1} (Number 1) is the biggest number")
    biggest_num = num_1
    
elif num_2 > num_3 and num_2 > num_1:
    print(f"{num_2} (Number 2) is the biggest number")
    biggest_num = num_2
    
else:
    print(f"{num_3} (Number 3) is the biggest number")
    biggest_num = num_3

print()

different: bool = True

if num_1 == num_2 == num_3:
    print("All numbers are thesame.\n")
    different = False
elif num_1 == num_2 or num_1 == num_3 or num_2 == num_3:
    print("Two of the three numbers are thesame.\n")
    different = False
    
if different:
    if (num_1 == biggest_num and num_2 > num_3) or (num_3 == biggest_num and num_2 > num_1):
        print(f"{num_2} (Number 2) is in the middle")
        
    elif (num_2 == biggest_num and num_3 > num_1) or (num_1 == biggest_num and num_3 > num_2):
        print(f"{num_3} (Number 3) is in the middle")
        
    else:
        print(f"{num_1} (Number 1) is in the middle")
        