#2.2
import pytest
from e2.words import count_words

def test_count_words__number_of_words():
    assert count_words("") == None
    assert count_words(12) == None
    assert count_words("Hello") == 1
    assert count_words("Hello World") == 2