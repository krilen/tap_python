"""
3A + B
"""

try:
    
    number_1 = int(input("Please provide me with a number >> "))
    number_2 = int(input("Please provide me with another number >> "))

    print(f"The sum of the numbers are: {number_1 + number_2}.")
# All errors
except:
    print("Something went wrong with you provided numbers")  
    
"""
3C
"""

cost_of_jacket = 2000
sale = 40
sale_calc = 1 -sale/100
print(f"The jacket on sale costs: {(cost_of_jacket * sale_calc):.0f} kr.")

"""
3D
"""
try:
    discount = int(input("What discount are you looking for (in %)? >> "))
    discount_calc = discount/100
    
    print("Till exempel {}%, som är {:.0f}kr. Då ska jackan kosta {} - {:.0f} = {:.0f} kr.".format(
            discount,
            (cost_of_jacket * discount_calc),
            cost_of_jacket,
            (cost_of_jacket * discount_calc),
            (cost_of_jacket * (1 -discount/100))
    ))
except:
    print(f"Sorry something went wrong, you will have to pay 1999 kr.")
    
