"""
4 Formulera testfall för en funktion som hittar största talet i en lista.
# Returnerar det största talet i listan
# Returnerar None om det inte finns något
"""

import pytest
from e1.e1_4_max import *

def test_find_max__fetch_max_value():
    assert find_max() == None
    assert find_max("") == None
    assert find_max([0]) == 0
    assert find_max([1,3,2]) == 3