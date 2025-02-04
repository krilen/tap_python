"""
3a Diskutera följande kod. Räcker det med ett testfall för att testa funktionen?
# Returnerar ett heltal med antalet vokaler som finns i ordet (aeiouyåäö)
> Nej måste också testa
   * Med endast vokaler
   * Blandat
"""


import pytest
from e1.e1_3_vowels import *

def test_count_vowels__no_vowels():
    assert count_vowels("qwrt") == 0
    assert count_vowels("Tt") == 0
    assert count_vowels("123 123") == 0
    assert count_vowels("") == 0
    
def test_count_vowels__only_vowels():
    assert count_vowels("a") == 1
    assert count_vowels("aE") == 2
    assert count_vowels("a e I") == 3
    
def test_count_vowels__mixed():
    assert count_vowels("Sandra") == 2
    assert count_vowels("John Doe") == 3
    assert count_vowels("Svenska tecken åäö") == 7
