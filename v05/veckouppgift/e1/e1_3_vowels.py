"""
3a Diskutera följande kod. Räcker det med ett testfall för att testa funktionen?
# Returnerar ett heltal med antalet vokaler som finns i ordet (aeiouyåäö)
"""

def count_vowels(word):
    if not word:
        return 0
    
    nr_of_vowels = 0
    
    for letter in word.casefold():
        if letter in "aeiouyåäö":
            nr_of_vowels += 1
            
    return nr_of_vowels
