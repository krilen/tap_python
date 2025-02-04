from src.example import subtract
from src.example import compare_names


def test_subtract__subtracts_correctly():
    #x = 10
    #y = 7
    expected = 3
    actual = subtract(10, 7)
    assert actual == expected

#def test_fail():
#    assert False


def test_compare_names__input_is_not_a_string():
    expected = False
    actual = compare_names(123, "Olle")
    assert actual == expected

def test_compare_names__name_is_not_a_string():
    expected = False
    actual = compare_names("kal", 998)
    assert actual == expected

def test_compare_names__input_is_in_name():
    expected = True
    actual = compare_names("kal", "Kalle")
    assert actual == expected

# TODO: testa fjärde fallet, expected==False om namnen inte matchar
