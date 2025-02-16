import pytest
from main import main

"""
This test the order of the application
But to get an order we need to add items to the cart and create the order
"""

# Test start the app and making sure that the order is empty
def test_interact_order__start_app_and_verify_that_order_is_empty(monkeypatch, capsys):
    # Multiple inputs
    inputs = iter(["o", "e", "q"])
    monkeypatch.setattr('builtins.input', lambda prompt: next(inputs))
    
    main()
    
    captured = capsys.readouterr()
    
    assert "No orders available" in captured.out
    assert "Press 'q' to quit." in captured.out
    

# Test start the app and add items to the cart and verifying the count
def test_interact_order__start_app_and_add_items_create_order_and_verify_order(monkeypatch, capsys):
    # Multiple inputs
    inputs = iter(["o", "e", "a", "c", "s", "c", "e", "v", "o", "o", "e", "q"])
    monkeypatch.setattr('builtins.input', lambda prompt: next(inputs))
    
    main()
    
    captured = capsys.readouterr()
    
    assert "No orders available" in captured.out                        # No orders
    
    assert "Main menu" in captured.out                                  # Back at main menu
    
    assert "Cart menu" in captured.out                                  # Cart submit
    assert "The number of items in the cart is: 0" in captured.out      # Cart count
    assert "Item was added to the cart" in captured.out                 # Add item        
    assert "The number of items in the cart is: 1" in captured.out      # Cart count should be one item in the cart
    assert "Main menu" in captured.out                                  # Back to main menu

    assert "The sum of items in the cart is" in captured.out            # Cart items
    assert "Main menu" in captured.out                                  # Cart -> Orders
    
    assert "Items count: 1" in captured.out                             # Orders
    
    assert "Press 'q' to quit." in captured.out                         # Back at main menu
    assert "Have a nice day" in captured.out                            # Quit

