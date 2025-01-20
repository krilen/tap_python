"""
1a Skriv färdigt kodexemplet.
answer = 0
for i in ????????????:
answer += i
print("Summan av talen 1 till 10 är: " + str(answer))
# Svaret ska bli 55

1b Räkna ut summan av alla tal mellan 1 och 100. (inklusive 1 och 100, rätt svar ska bli 5050)

1c Skriv om 1b så att den använder en while-loop.

2 Räkna ut summan av alla elementen i listan: [1, -2, 3, -2, 4, -3]

3 Träna på att skapa och manipulera listor. Alla uppgifter ska lösas med funktionerna som står i presentationen.
3a Skapa en lista med namnen på fyra filmer. Namnen ska vara strängar. Skriv ut hela listan 2med funktionen print.
3b Lägg till "Fellowship of the ring" sist i listan.
3c Lägg till "The two towers" på första platsen i listan. (index noll)
3d Ta reda på vilken position (index) "Fellowship of the ring" har nu.
3e Ta bort en annan av filmerna. Har Fellowship-filmen ändrat index?
3f Ta reda på hur lång listan är. (len)
3g Vänd listan baklänges.
3h Sortera listan stigande i bokstavsordning.

"""

# 1A
answer = 0

for i in range(11):
    answer += i

print("Summan av talen 1 till 10 är: " + str(answer))

# 1B
# Som ovan men m,ed 'range(1, 101)'
# Tar en liten annan väg, lite mer avancerad
print(f"Summan för alla tal mellan 1 och 100 är: {sum(range(1,101))}")

# 1C
i = 1
summa = 0

while i <= 100:
    summa += i
    i += 1
    
print("Summan med en while loop:", summa)

# 2
elements = [1, -2, 3, -2, 4, -3]
print("Summan av element blir:", sum(elements))

# 3
# Skippar denna




















