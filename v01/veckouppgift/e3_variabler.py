"""
3 Använda variabler och datatyper

1a Använd input för att be användaren om ett heltal. Spara värdet i en variabel. Omvandla
variabelns värde till ett heltal, och skriv ut det för att testa om du har gjort rätt.
Kodexempel med input:
x = input("Fråga här")

1b Fråga användaren efter ett annat heltal. Skriv ut summan av talen, alltså tal1 + tal2.
Testa genom att hitta på två tal och räkna ut summan i huvudet. Kontrollera om
programmet räknar rätt.

2a Nu är det dags att köpa vinterkläder. Du ser en fin jacka som kostar 2000 kronor. Jackan
är på rea, 50%. Skriv ett program som räknar ut hur mycket du behöver betala.
Tips: räkna ut rabatten med formeln: slut_pris = pris * rea_procent / 100.

2b Gör om programmet så att användaren kan skriva in en procentsats.
Testa genom att hitta på en procentsats och räkna ut vad programmet ska svara med,
innan du kör det. Till exempel 10%, som är 200 kr. Då ska jackan kosta 2000 - 200 == 1800
kr.
"""


# 1 A + B
try:
    
    number_1 = int(input("Please provide me with a number >> "))
    number_2 = int(input("Please provide me with another number >> "))

    print(f"The sum of the numbers are: {number_1 + number_2}.")
# All errors
except:
    print("Something went wrong with you provided numbers")
    
# 2A
cost_of_jacket = 2000
sale = 40
sale_calc = 1 -sale/100
print(f"The jacket on sale costs: {(cost_of_jacket * sale_calc):.0f} kr.")

# 2 B
try:
    discount = int(input("What discount are you looking for (in %)? >> "))
    discount_calc = discount/100
    
    print("Till exempel {}%, som är {:.0f}kr. Då ska jackan kosta {} - {:.0f} = {:.0f} kr.".format(
            discount,
            (cost_of_jacket * discount_calc),
            cost_of_jacket,
            (cost_of_jacket * discount_calc),
            (cost_of_jacket * (1 -discount/100))
    ))
except:
    print(f"Sorry something went wrong, you will have to pay 1999 kr.")
    
