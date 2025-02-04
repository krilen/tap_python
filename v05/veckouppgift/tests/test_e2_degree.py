# 2.1
import pytest
from e2.degree import c_to_f


def test_c_to_f__validate_degree_convert():
    assert c_to_f(-300) == None
    assert c_to_f(0) == 32.0