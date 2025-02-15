import pytest
from order.order import Order

# Test to see if the order list when empty 
def test_order__class_init_order_list():
    o = Order()
    
    assert isinstance(o._orders, list) == True
    assert o._orders == []  # The list itself NOT the getter
    assert o.orders == []   # The getter of the order list
    
    
# Test the getter and setter for the order list in the order class
@pytest.mark.parametrize("data", [([1]), ([1,2,5]), ([1,2,3,4,5,6])])
def test_order__order_list_get_set(data):
    o = Order()
    
    # Setter
    for d in data:
        o.orders = d

        
    assert o.orders == data # Getter compair to expected


# Test the count of the number of orders
@pytest.mark.parametrize("data, expected", [([], 0), ([1,2,5], 3), ([1,2,3,4,5,6], 6)])
def test_order__count_orders(data, expected):
    o = Order()
    
    # Setter
    for d in data:
        o.orders = d
        
    assert o.count_orders() == expected
    
    
# Test to insert an order
@pytest.mark.parametrize("cart", [([{'item': 1, 'count': 1, 'sum_item': 1}]),
                                ([{'item': 1, 'count': 1, 'sum_item': 1}, {'item': 2, 'count': 2, 'sum_item': 2}])])
def test_order__insert_order(cart):
    o = Order()
    o.insert_order(cart)                            # Order gets inserted, only one order exits
        
    for i in range(0, len(cart)):                   
        assert cart[i] == o.orders[0]['items'][i]   # Compair the cart items agains the order items
    
    
    