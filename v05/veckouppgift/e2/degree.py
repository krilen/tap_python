"""
2 Öva på TDD

1a Hitta på lämplig testdata till följande funktion, som omvandlar grader Celsius till grader Fahrenheit.
def c_to_f(degree):
    if degree < -273.15:
        return None
    return degree * 9 / 5 + 32

1b Vilka ekvivalensklasser har parametern degree?
    > * -300 och 0 på vadera sida av -273.15

1c Skriv ett testfall.
"""

def c_to_f(degree):
    if degree < -273.15:
        return None
    return degree * 9 / 5 + 32