# 2.4
import pytest
from e2.sort_asc import is_sorted_ascending


def test_is_sorted_ascending__numbers_ascending():
    assert is_sorted_ascending() == False
    assert is_sorted_ascending([]) == False
    assert is_sorted_ascending(["", 2]) == False
    assert is_sorted_ascending([1]) == True
    assert is_sorted_ascending([1, 2]) == True
    assert is_sorted_ascending([1, 2, 3]) == True
    assert is_sorted_ascending([2, 3, 1]) == False