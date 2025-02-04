"""
1 E 2
"""
import pytest
from e1.e1_2_fix_error import *

def test_empty_list():
    expected = None
    actual   = sum_list([])
    assert actual == expected
    

def test_number_list():
    assert sum_list([5]) == 5
    assert sum_list([5, 12]) == 17
    assert sum_list([1,2,3,4,5]) == 15
    assert sum_list([1]) == 1