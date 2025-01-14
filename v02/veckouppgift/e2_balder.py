"""
2 Balder

För att få åka Balder på Liseberg måste man vara 130 cm lång. Skriv ett program som kan
säga om man får åka!

1. Fråga användaren hur lång man är (i cm)
2. Skriv ut antingen "Du får åka!" eller "Du får inte åka"

Skriv in följande värden för att testa att ditt program gjort rätt:
A. 121 cm (får inte åka)
B. 130 cm (får åka)
C. 155 cm (får åka)

Diskutera:
 * Varför just tre värden?
   > För att testa gränsen
 * Varför dessa värden?
   > * 121 för att testa under gränsen och ett negativt utfall
     * 130 för att testa gränsen EXAKT och att det blir ett positivt utfall
       Detta eftersom 130 är den satta gränsen och är ett positivt utfall
     * 155 för att testa över gränsen och ett positivt utfall
 * Skulle det vara bra att lägga till testvärdet 129 cm?
   > Nej eftersom 129 är ett negativt utfall och har inget eller lika mycket
     som 121 att göra med detta gränsfall
     
"""

OUTPUT_VALID_LENGTH = "You are able to go on the ride"
OUTPUT_INVALID_LENGTH = "You are NOT able to go on the ride!"

try:
    riders_length = int(input("How tall are you (in cm)? >> "))

except:
    print("That was not a valid length!")
    print(OUTPUT_INVALID_LENGTH)
    
else:
    if riders_length >= 130:
        print(OUTPUT_VALID_LENGTH)
    else:
        print(OUTPUT_INVALID_LENGTH)

"""
Code review, 2025jan14 (med Rasmus och Rebecca)
 * Kort och gott inget överflödigt

"""