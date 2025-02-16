import pytest
from main import main

"""
This test the cart of the application
"""

# Test start the app and making sure that the cart is empty in cart view
def test_interact_cart__start_app_and_verify_that_the_cart_is_empty_in_cart_items(monkeypatch, capsys):
    # Multiple inputs
    inputs = iter(["v", "e", "q"])
    monkeypatch.setattr('builtins.input', lambda prompt: next(inputs))
    
    main()
    
    captured = capsys.readouterr()
    
    assert "No items in the cart" in captured.out
    assert "Press 'q' to quit." in captured.out
    assert "Have a nice day" in captured.out


# Test start the app and making sure that the cart is empty in adding to cart
def test_interact_cart__start_app_and_verify_that_the_cart_is_empty_in_cart_menu(monkeypatch, capsys):
    # Multiple inputs
    inputs = iter(["a", "c", "e", "q"])
    monkeypatch.setattr('builtins.input', lambda prompt: next(inputs))
    
    main()
    
    captured = capsys.readouterr()
    
    assert "Cart menu" in captured.out
    assert "The number of items in the cart is: 0" in captured.out
    assert "Press 'q' to quit." in captured.out
    assert "Have a nice day" in captured.out


# Testing to add 1, 2 and 5 items in the cart (based on the number "s") 
@pytest.mark.parametrize("data", [(["a", "c", "s", "c", "e", "q"]), (["a", "c", "s", "s", "c", "e", "q"]), (["a", "c", "s", "s", "s", "s", "s", "c", "e", "q"])])
# Test start the app and add items to the cart and verifying the count
def test_interact_cart__start_app_and_add_items_to_cart_and_verifying_the_count(monkeypatch, capsys, data):
    # Multiple inputs
    inputs = iter(data)
    
    _count = len([d for d in data if d == "s"])
    
    monkeypatch.setattr('builtins.input', lambda prompt: next(inputs))
    
    main()
    
    captured = capsys.readouterr()
    
    assert "Cart menu" in captured.out
    assert "The number of items in the cart is: 0" in captured.out
    
    for _ in range(0, _count):
        assert "Item was added to the cart" in captured.out
        
    _text = f"The number of items in the cart is: {_count}"
    assert _text in captured.out
    
    assert "Press 'q' to quit." in captured.out
    assert "Have a nice day" in captured.out



@pytest.mark.parametrize("data", [(["v", "e", "a", "c", "s", "c", "e", "v", "e", "q"]), # 1 item
                                  (["v", "e", "a", "c", "s", "s", "c", "e", "v", "e", "q"]), # 2 items
                                  (["v", "e", "a", "c", "s", "s", "s", "s", "s", "c", "e", "v", "e", "q"])]) # 5 items
# Test start the app and add items to the cart and verifying the count
def test_interact_cart__start_app_and_verify_cart_items_than_add_items_and_verify_count_and_cart_items(monkeypatch, capsys, data):
    # Multiple inputs
    inputs = iter(data)
    
    _count = len([d for d in data if d == "s"])
    
    monkeypatch.setattr('builtins.input', lambda prompt: next(inputs))
    
    main()
    
    captured = capsys.readouterr()
    
    assert "No items in the cart" in captured.out
    assert "Main menu" in captured.out
    assert "Cart menu" in captured.out
    assert "The number of items in the cart is: 0" in captured.out
    
    for _ in range(0, _count):
        assert "Item was added to the cart" in captured.out
        
    _text = f"The number of items in the cart is: {_count}"
    assert _text in captured.out
    
    assert "Main menu" in captured.out
    assert "The sum of items in the cart is" in captured.out
    assert "Press 'q' to quit." in captured.out
    assert "Have a nice day" in captured.out


