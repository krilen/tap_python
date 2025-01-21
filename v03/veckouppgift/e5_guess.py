"""
5 Gissa talet
Gör ett spel som slumpar ett hemligt tal mellan 1 och 100. Sedan ska man försöka gissa
det. Om man gissar för lågt eller för högt ska spelet tala om det. Efter att man har gissat
rätt ska spelet skriva ut antalet gissningar.

# Slumpa ett hemligt tal
secret = random.randint(1, 100)

Exempel:
Välkommen till gissa talet! Jag tänker på ett tal mellan 1 och 100. Kan du
gissa vilket det är?Gissa: 40
Nej, det är för lågt!
Gissa: 55
Nej, det är för högt!
Gissa: 51
Det är rätt!! Du gjorde det på 3 gissningar.

Version 2: skriv ut om man är nära ifall man gissar högst 5 ifrån det rätta svaret.
"Nu börjar det brännas!"
"""
import random

number_lower: int = 1
number_upper: int  = 100

secret: int = random.randint(number_lower, number_upper +1)

print("Welcome to guess the number")
print(f"I am thinging of a number betweeen {number_lower} and {number_upper}.")
print("Can you guess which number it is?")
print()

guesses: list[int] = []

while True:
    
    try:
        guess: int = int(input("Guess a number: >> "))

    except ValueError:
        print("That is not a number!")
        guesses.append(0) # If you can't read the instuctions you will waste a guess
        
    else:
        
        guesses.append(guess)
        
        if guess == secret:
            break
            
        elif guess > secret:
            print("No, to high!")
            
        else:
            print("No, to low!")
            
    print()
        
print()
print(f"That is correct! It took you {len(guesses)} tries to guess it.")
print()