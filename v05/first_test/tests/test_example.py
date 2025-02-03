from example import *

def test_subtract__subtract_correctly():
    expected = 3
    actual = subtract(10, 7)
    
    assert actual == expected
    
#def test_subract__false():
#    assert False

def test_complare_names__input_is_not_a_string():
    excepted = False
    acutal = compare_names(123, "olle")
    
    assert acutal == excepted
    
def test_compare_names__name_is_not_a_string():
    excepted = False
    acutal = compare_names("olle", 123)
    
    assert acutal == excepted
    
def test_compare_names__compare_string_true():
    excepted = True
    acutal = compare_names("kal", "Kalle")
    
    assert acutal == excepted
    
def test_compare_names__compare_string_false():
    excepted = False
    acutal = compare_names("kal", "Olle")
    
    assert acutal == excepted
