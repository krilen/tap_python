# 2.3
import pytest
from e2.median import find_median


def test_find_median__get_median_number():
    assert find_median() == None
    assert find_median("") == None
    assert find_median([]) == None
    assert find_median([1, "hello"]) == None
    assert find_median([1]) == 1 
    assert find_median([1.25, 1.75]) == 1.5
    assert find_median([1, 0.343]) == 0.6715
    assert find_median([1, 2, 3]) == 2 

