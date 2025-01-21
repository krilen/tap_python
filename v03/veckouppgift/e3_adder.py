"""
Gör ett program som upprepade gånger ber användaren skriva in ett tal. När man skriver in strängen "quit" eller "avsluta" ska programmet ska det räkna ut summan av talen. Exempel:
Välkommen till Kvittokompis! Avsluta genom att skriva: quit
Skriv in ett belopp: 25
Skriv in ett belopp: 50
Skriv in ett belopp: quit
Det blir 75 kr totalt. Välkommen åter!

Tips! För att lösa uppgiften behöver du: flera variabler, input, while-loop.

Version 2: programmet ska fråga hur många man är, och tala om hur mycket varje person i sällskapet ska betala.
Hur många är ni? 3
Det blir 75 kr totalt, alltså 25.0 kr per person. Välkommen åter!

Version 3: programmet ska fråga hur många procent dricks man vill lägga på. Om användaren inte skriver något (tom sträng) ska programmet använda 10% som standardinställning.

Nice to have: prova att använda try+except eller isdigit för att hantera de fall när användaren skriver ett felaktigt värde. Python Try Except , isdigit | StackOverflow
("Nice to have" handlar om funktionalitet som inte är nödvändig, men som är bra att ha. Gå gärna vidare till nästa uppgift och återvänd till den här om du vill lära dig mer.)

Testa programmet med följande inputs:
Version 1:
100
10, 20, 15

Version 2:
100, 1 person
100, 2 personer
10, 10, 40 personer
30, 20, 30, 1 person

Lägg till egna testfall för dricksen.

testfall >
 * 10; 1 person; 0% tip -> 10                               <= Täcker en person utan dricks, eftersom 0 är speciell
 * 10; 1 person; default tip -> 11                          <= Täcker en person med default dricks, 10%
 * 10; 1 person; 20% tip -> 12                              <= Täcker en person med extra dricks 20%
 * 10+20; 2 person, default tip -> 33 / 16.5                <= Räknar ihop och delar för 2 personer med default dricks, 10%
 * 10+20; 2 person, 20% tip -> 36 / 18                      <= Räknar ihop (3 st) och delar med 2 personer med extra dricks 20%
 * 10+20; 3 personer, 0% tip -> 30 / 10                     <= Räknar ihop och delar med 3 personer utan dricks
 * 10+20+30+40; 2 personer, default tip -> 110 / 55         <= Räknar ihop
"""

numbers: list[float] = []
tip: int = 10

print("Welcome to 'Kvittokompis', quit by enter: 'quit'")

# Getting the numbers
while True:
    
    user_input: str = input("Please enter a number: >> ")
    
    if user_input.casefold() == "quit":
        break
    
    try:
        number: float = float(user_input)
        
    except ValueError:
        print("That is not av valid input, please try again!")
        
    else:
        numbers.append(number)


# Getting the number of people
while True:
    
    try:
        nr_of_people: int = int(input("How many people are there >> "))
        
    except ValueError:
        print("That is not a valid number of people")
        
    else:
        break

total_amount: float = sum(numbers)


# Getting the tip
print(f"How much tip do you want to add, currently at {tip}% it add {round(total_amount * tip/100, 1)} kr.")

tip_str = input("How much tip in % do you wish to add? >> ")
    
if tip_str != "":
    try:
        tip: float = float(tip_str)
    
    except ValueError:
        pass

tip_amount: float = total_amount * tip/100
total_amount += tip_amount


# Output
print()

print(f"That will be {total_amount:.1f} kr in total, including {tip_amount:.1f} kr in tip")

if nr_of_people > 1:
    print(f"This will be for each {(total_amount / nr_of_people):.1f} kr.")
    
print("Welcome back.")
        