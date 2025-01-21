"""
Skriv in följande kod och modifiera den, så att den skriver ut figurerna a-j en i taget.
"""

for i in range(0, 10):

    for y in range(1, 7):
        s = ""
        for x in range(1, 9):
            
            # a: single verticle line
            if i == 0:
                if x == 1:
                    s += "#"
                else:
                    s += "."
                        
            # b: backward dashdash
            if i == 1:
                if x == y:
                    s += "#"
                else:
                    s += "."
                
            # c: thick (3) verticle line
            if i == 2:
                if x == 3 or x == 4 or x == 5:
                    s += "#"
                else:
                    s += "."
            
            # d: cross
            if i == 3:
                if x == 3 or y == 3:
                    s += "#"
                else:
                    s += "."
        
        print(s)
    print()