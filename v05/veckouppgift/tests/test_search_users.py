"""
Söka efter användare
"""
import pytest
from search_users.users import autocomplete

master_list = ["JohnSmith", "LauraDoe", "EmilyJohnson", "MichaelBrown", "SarahDavis",
                "DavidClark", "JessicaTaylor", "JamesMartinez", "OliviaWilson",
                "DanielAnderson", "SophiaThomas", "MatthewDoe", "JohnJackson", 
                "EthanWhite", "IsabellaHarris", "DavidLewis", "ChloeTaylor", 
                "BenjaminYoung", "MiaSmith", "WilliamScott"]

def test_autocomplete__search_for_users():
    
    assert autocomplete("", master_list) == None
    assert autocomplete(12, master_list) == None
    assert autocomplete("John", []) == None
    
    assert autocomplete("MIA", master_list) == ["MiaSmith"]
    assert autocomplete("John", master_list) == ["JohnSmith", "EmilyJohnson", "JohnJackson"]
    assert autocomplete("carl", master_list) == []
    
