"""
Rätta eventuella fel. Vad gör koden?
---
x = 100  # biljettpris
y = 200  # pengar på fickan
print("Det blir " + (y - x) " kronor över.") <-- fel
z = 200 - 100 / 2 <-- missade detta, oklart
print("Hälften är: " + z) <-- fel
---
Kom på bättre namn, i stället för x, y och z.

Fel

 * Blandar en subtraktion (operation) när en print skall göras 
   och man blandar också text med nummer när det gäller +
   >Enklaste lösningen är att gå över till en f-string print

 * Använder ett + mellan text och nummer dvs slå ihop
   >Enklaste lösningen är att använda ett komma istället 

"""
# x -> ticket_price
ticket_price = 100  # biljettpris

# y -> money_on_hand
money_on_hand = 200  # pengar på fickan
print(f"Det blir {money_on_hand - ticket_price } kronor över.")

# z -> number
number = (200 - 100) / 2
print("Hälften är: ", number)

