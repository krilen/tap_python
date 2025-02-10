"""
5 Winner takes it all brukar det ju heta, men nu ska vi försöka ge lite heder åt alla andrapristagare. Formulera testfall för en funktion som hittar näst största talet i en lista!
# Returnerar det nästa största talet i listan
# Returnerar None om det inte finns något
# Om det är delad förstaplats så returneras det talet
"""

import pytest
from e1.e1_5_second_max import *


def test_find_2nd_max__fetch_2nd_max_value():
    assert find_2nd_max() == None
    assert find_2nd_max("") == None
    assert find_2nd_max([]) == None
    assert find_2nd_max("a") == None
    assert find_2nd_max([1]) == None # misstolkat uppgift: trodde att vid 1 tal skulle det retuneras och inte None 
    assert find_2nd_max([1, 1]) == 1
    assert find_2nd_max([1, 2]) == 1
    assert find_2nd_max([1, 2, 3]) == 2
    assert find_2nd_max([4, "a"]) == None # se ovan misstolkning
    assert find_2nd_max(["a", 2, 4, "5", 7]) == 4
