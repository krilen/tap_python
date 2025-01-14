"""
3 Sportresultat

Tottenham spelar mot Liverpool i Champions League. Skriv ett program som frågar
användaren hur många mål respektive lag gjorde, och talar om vilket lag som vann.

Exempel på output:
Matchen är över, nu ska vi räkna ut resultatet!
Hur många mål gjorde Tottenham? 2
Hur många mål gjorde Liverpool? 1
Tottenham vann!

Version 2: programmet ska tala om ifall det blev oavgjort.

Version 3: nu ska programmet tala om hur många mål mer laget vann med. Exempel:
Tottenham vann med 1 mål!

Eftersom det finns tre möjliga utfall (lag 1 vinst, lag 2 vinst, oavgjort) behöver du minst
tre testfall. Hitta på värden som du kan använda för att testa alla möjliga utfall.

> Testfall
   * 0-0 => draw,
   * 1-0 => Win Tottenham with 1 goal
   * 1-3 => Win Liverpool with 2 goals
   
"""

print("The game is over, let's see who won!")

while True:
    
    try:
        tottenham = int(input("How many goals did Tottenham do? >> "))
        liverpool = int(input("How many goals did Liverpool do? >> "))
    
    except ValueError:
        print("Something went wrong with the input, try again")
        
    else:
        break
        
        
if tottenham == liverpool:
    print("The game was a draw")

else:
    goal_diff = abs(tottenham -liverpool)
    output_tmpl = "{} won with {} goal{}!"

    if tottenham > liverpool:
        print(output_tmpl.format("Tottenham", goal_diff, "s" if goal_diff > 1 else ""))
    else:
        print(output_tmpl.format("Liverpool", goal_diff, "s" if goal_diff > 1 else ""))