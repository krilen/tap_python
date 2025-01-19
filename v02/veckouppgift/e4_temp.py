"""
Skriv ett program som kan omvandla en temperatur i grader Celsius till grader Fahrenheit.

Version 1, exempel på output:
Skriv in en temperatur i grader Celsius: 22
Det blir 71.6 grader Fahrenheit.

Version 2: fråga först användaren om man vill ange temperaturen i Celsius eller Fahrenheit.
Sedan räknar programmet om till den andra temperaturen.

Tips: be användaren skriva in t.ex. "F" om man vill ange temperaturen i i Fahrenheit.

Använd sedan if + else.

Version 3: om temperaturen som omvandlas är under 10°C ska programmet dessutom
säga till användaren att ta på sig vinterkläder. Och om temperaturen är minst 20°C ska det
föreslå att man packar badkläder.

Formel för konvertering mellan temperaturenheter:
C = (F - 32) / 1.8
F = 1.8 * C + 32

Förslag på värden att testa med:
 Celsius   | Fahrenheit
 ---------------------------
  0        |  32
  -17.777… |  0
  37.777…  |  100
  100      |  212

"""

# Func to convert scale and return it with the string of the scale
def convert_degrees(degree: int, scale: str) -> tuple[int, str]:
    
    # Converting FROM not to
    # For Farenehit you will get Celsius 
    if scale == "f":
        return (degree -32) / 1.8, "Celsius"
    
    return (1.8 * degree) +32, "Farenheit"


# Valid scale
while True:
    temp_scale: str = input("What temperature scale would you like use Celsius (c) or Farenheit (f)? >> ").casefold()

    if temp_scale == "c" or temp_scale == "f":
        break

    print("Not a valid temperature scale!")


# Valid temperature
INPUT_TEMP: str = "For degrees in {} enter a temperature in {} >> "

while True:
    try:
        temp: int = int(input(INPUT_TEMP.format("Celcius" if temp_scale == "f" else "Farenheit",
                                       "Celsius" if temp_scale == "c" else "Farenheit")))
    
    except ValueError:
        print("Not a valid temperature (int)!")
        
    else:
        break

converted_temp, converted_scale = convert_degrees(temp, temp_scale)
print(f"This is {converted_temp:.0f} degrees in {converted_scale}.")

# Winter, from Celcius or to Celcius
if (converted_scale == "Celsius" and converted_temp < 10) or (temp < 10 and temp_scale == "c"):
    print("Time to thing about those long johns.")

# Summer, from Celcius or to Celcius
if (converted_scale == "Celsius" and converted_temp > 20) or (temp > 10 and temp_scale == "c"):
    print("Remember the bathing suit.")
