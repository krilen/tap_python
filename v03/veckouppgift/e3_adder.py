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

"""