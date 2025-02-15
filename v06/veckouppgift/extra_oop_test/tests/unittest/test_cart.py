import pytest
from cart.cart import Cart

# Test to see if the cart list when empty 
def test_cart__class_init_cart():
    c = Cart()
    
    assert isinstance(c._cart, list) == True
    assert c._cart == []                    # The list itself NOT the getter
    assert c.shopping_cart == []            # The getter of the cart list


# Test to see the sum of the cart list when empty 
def test_cart__class_init_sum_cart():
    c = Cart()
     
    assert isinstance(c._sum_cart, int) == True
    assert c._sum_cart == 0                # The list itself NOT the getter


# Test the cart setter, getter, deleter and count items cart
@pytest.mark.parametrize("data, count", [([], 0), ([{1}, {2}], 2),
                                         ([{'item': 0, 'count': 1, 'sum_item': 0}, {'item': 0, 'count': 1, 'sum_item': 0}], 2)])
def test_cart__cart_setter_getter_deleter(data, count):
    c = Cart()
    
    for d in data:
        c.shopping_cart = d             # setter
        
    assert c.shopping_cart == data      # getter
    assert c.count_cart() == count      # count method
    del(c.shopping_cart)                # deleter
    assert c.shopping_cart == []


# Test the deleting an item in the cart at a specific index
@pytest.mark.parametrize("data, expected, index", [([{'item': 0, 'count': 1, 'sum_item': 0}, {'item': 0, 'count': 1, 'sum_item': 0}],
                                                        [{'item': 0, 'count': 1, 'sum_item': 0}, {'item': 0, 'count': 1, 'sum_item': 0}], 2), # Out of range 
                                                    
                                                    ([{'item': 0, 'count': 1, 'sum_item': 0}, {'item': 0, 'count': 1, 'sum_item': 0}],
                                                        [{'item': 0, 'count': 1, 'sum_item': 0}], 1),
                                                    
                                                    ([{'item': 1, 'count': 2, 'sum_item': 2}, {'item': 5, 'count': 6, 'sum_item': 30}, {'item': 7, 'count': 1, 'sum_item': 7}],
                                                        [{'item': 1, 'count': 2, 'sum_item': 2}, {'item': 5, 'count': 6, 'sum_item': 30}], 2)
                                                    ])
def test_cart__delte_item_index(data, expected, index):   
    _data = sorted(data.copy(), key=lambda d: d['item'])
    _expected = sorted(expected.copy(), key=lambda d: d['item'])
    
    c = Cart()
    
    for d in _data:
        c.shopping_cart = d             # setter
        
    c.delete_item(index)                # Delete item i list using an index
    
    assert c.shopping_cart == _expected
    

# Test the cart cleanup, removing duplicates from cart and icrease count
@pytest.mark.parametrize("data, expected, count", [([{'item': 0, 'count': 1, 'sum_item': 0}], [{'item': 0, 'count': 1, 'sum_item': 0}], 1),
                                                   
                                                    ([{'item': 0, 'count': 1, 'sum_item': 0}, {'item': 0, 'count': 1, 'sum_item': 0}], 
                                                            [{'item': 0, 'count': 2, 'sum_item': 0}], 1),
                                                   
                                                    ([{'item': 1, 'count': 1, 'sum_item': 1}, {'item': 1, 'count': 1, 'sum_item': 1}],
                                                            [{'item': 1, 'count': 2, 'sum_item': 2}], 1),
                                         
                                                    ([{'item': 1, 'count': 1, 'sum_item': 1}, {'item': 2, 'count': 1, 'sum_item': 2}],
                                                            [{'item': 1, 'count': 1, 'sum_item': 1}, {'item': 2, 'count': 1, 'sum_item': 2}], 2),
                                                    
                                                    ([{'item': 1, 'count': 1, 'sum_item': 1}, {'item': 2, 'count': 1, 'sum_item': 2}, {'item': 1, 'count': 1, 'sum_item': 1}],
                                                            [{'item': 1, 'count': 2, 'sum_item': 2}, {'item': 2, 'count': 1, 'sum_item': 2}], 2),

                                                    ([{'item': 1, 'count': 2, 'sum_item': 3}, {'item': 2, 'count': 1, 'sum_item': 2}, {'item': 1, 'count': 1, 'sum_item': 1}],
                                                            [{'item': 1, 'count': 3, 'sum_item': 3}, {'item': 2, 'count': 1, 'sum_item': 2}], 2),
                                                    
                                                    ([{'item': 1, 'count': 1, 'sum_item': 1}, {'item': 5, 'count': 5, 'sum_item': 25}, {'item': 1, 'count': 1, 'sum_item': 1}, {'item': 5, 'count': 1, 'sum_item': 5}, {'item': 7, 'count': 1, 'sum_item': 7}],
                                                            [{'item': 1, 'count': 2, 'sum_item': 2}, {'item': 5, 'count': 6, 'sum_item': 30}, {'item': 7, 'count': 1, 'sum_item': 7}], 3),
                                                ])
def test_cart__cart_cleanup(data, expected, count):
    _data = sorted(data.copy(), key=lambda d: d['item'])
    _expected = sorted(expected.copy(), key=lambda d: d['item'])
    
    c = Cart()
    
    for d in _data:
        c.shopping_cart = d             # setter
        
    c.cleanup_cart()                    # cleans up, remove dublicates in the cart and ads to the count and sum
        
    assert c.shopping_cart == _expected # getter
    assert c.count_cart() == count      # count method
    
    
    
# Test the cart sum count 
@pytest.mark.parametrize("data, total_sum", [([{'item': 0, 'count': 1, 'sum_item': 0}], 0),
                                                   
                                        ([{'item': 0, 'count': 1, 'sum_item': 0}, {'item': 0, 'count': 1, 'sum_item': 0}], 0), 

                                        ([{'item': 1, 'count': 1, 'sum_item': 1}, {'item': 2, 'count': 1, 'sum_item': 2}], 3),
                                                   
                                        ([{'item': 1, 'count': 2, 'sum_item': 2}, {'item': 5, 'count': 6, 'sum_item': 30}, {'item': 7, 'count': 1, 'sum_item': 7}], 39),
                                        ])   
def test_sum_cart__cart_total_sum(data, total_sum):
    c = Cart()
    
    for d in data:
        c.shopping_cart = d             # setter
        
    c.calc_sum_cart()                   # sal
    
    assert c._sum_cart == total_sum