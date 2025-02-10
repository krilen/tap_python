"""
1 E 2
"""
import pytest
from e1.e1_2_fix_error import *

def test_empty_list():
    expected = 0 # Rättning None -> 0
    actual = sum_list([])
    assert actual == expected
    
# Undvik att "återanvända" olika tal
def test_number_list():
    assert sum_list([5]) == 5
    assert sum_list([10, -8]) == 2
    assert sum_list([1,2,3,4]) == 10