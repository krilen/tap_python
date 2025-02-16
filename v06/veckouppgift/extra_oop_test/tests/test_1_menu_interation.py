import pytest
from main import main

"""
This test the basic interaction of the application with only intent of navigating it
"""

# Test start the app and quiting
def test_interact_menu__start_app_and_quit(monkeypatch, capsys):
    # Using builtin.input from pythin std libray and monkeypatch from pytest
    monkeypatch.setattr('builtins.input', lambda prompt: 'q') # send 'q' to quit
    
    main()  # Run the application function
    
    captured = capsys.readouterr()  # Capture the printed output
    assert "Press 'q' to quit." in captured.out  # Ensure the prompt is shown in main()
    assert "Have a nice day" in captured.out  # Ensure the quitting message is shown


# Test start the app press incorrect key get a propmt than quiting
def test_interact_menu__start_app_and_press_incorrect_key_than_quit(monkeypatch, capsys):
    # Multiple inputs
    inputs = iter(["x", "q"])
    monkeypatch.setattr('builtins.input', lambda prompt: next(inputs))
    
    main()
    
    captured = capsys.readouterr() 
    assert "Not a valid selection!" in captured.out
    assert "Press 'q' to quit." in captured.out
    assert "Have a nice day" in captured.out

 
# Test start the app press 'a' to see the cart submit menu
def test_interact_menu__start_app_and_press_key_to_get_cart_submit(monkeypatch, capsys):
    inputs = iter(["a", "e", "q"])
    monkeypatch.setattr('builtins.input', lambda prompt: next(inputs))
    
    main()
    
    captured = capsys.readouterr() 
    assert "Cart menu" in captured.out
    assert "Main menu" in captured.out
    assert "Have a nice day" in captured.out


# Test start the app press 'a' to see the cart submit menu and also an inncorrect key
def test_interact_menu__start_app_and_press_key_to_get_cart_submit_and_incorrect_key(monkeypatch, capsys):

    inputs = iter(["a", "x", "e", "q"])
    monkeypatch.setattr('builtins.input', lambda prompt: next(inputs))
    
    main()
    
    captured = capsys.readouterr() 
    assert "Cart menu" in captured.out
    assert "Not a valid selection!" in captured.out
    assert "Main menu" in captured.out
    assert "Have a nice day" in captured.out


# Test start the app press 'v' to see the cart items
def test_interact_menu__start_app_and_press_key_to_see_cart_items(monkeypatch, capsys):
    # Multiple inputs
    inputs = iter(["v", "e", "q"])
    monkeypatch.setattr('builtins.input', lambda prompt: next(inputs))
    
    main()  # Run the application function
    
    captured = capsys.readouterr() 
    assert "Cart items" in captured.out
    assert "Main menu" in captured.out
    assert "Have a nice day" in captured.out
    
    
# Test start the app press 'v' to see the cart items and also an inncorrect key
def test_interact_menu__start_app_and_press_key_to_see_cart_items_and_incorrect_key(monkeypatch, capsys):
    # Multiple inputs
    inputs = iter(["v", "x", "e", "q"])
    monkeypatch.setattr('builtins.input', lambda prompt: next(inputs))
    
    main()  # Run the application function
    
    captured = capsys.readouterr() 
    assert "Cart items" in captured.out
    assert "Not a valid selection!" in captured.out
    assert "Main menu" in captured.out
    assert "Have a nice day" in captured.out
    

# Test start the app press 'o' to see the orders
def test_interact_menu__start_app_and_press_key_to_see_orders(monkeypatch, capsys):
    # Multiple inputs
    inputs = iter(["o", "e", "q"])
    monkeypatch.setattr('builtins.input', lambda prompt: next(inputs))
    
    main()  # Run the application function
    
    captured = capsys.readouterr() 
    assert "Orders" in captured.out
    assert "Main menu" in captured.out
    assert "Have a nice day" in captured.out


# Test start the app press 'o' to see the orders
def test_interact_menu__start_app_and_press_key_to_see_orders_and_incorrect_key(monkeypatch, capsys):
    # Multiple inputs
    inputs = iter(["o", "x", "e", "q"])
    monkeypatch.setattr('builtins.input', lambda prompt: next(inputs))
    
    main()  # Run the application function
    
    captured = capsys.readouterr() 
    assert "Orders" in captured.out
    assert "Not a valid selection!" in captured.out
    assert "Main menu" in captured.out
    assert "Have a nice day" in captured.out
