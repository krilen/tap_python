# Multiply
import pytest
from multi.multiply import multiplication_table


def test_multiplication_table__check_multiply():
    
    assert multiplication_table() == None
    assert multiplication_table("", "") == None
    assert multiplication_table("", 1) == None
    assert multiplication_table(1, "") == None
    
    assert multiplication_table(1, 1) == [1]
    assert multiplication_table(15, 2) == [15, 30]
    assert multiplication_table(0, 3) == [0, 0, 0]