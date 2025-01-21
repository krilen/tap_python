"""
Skriv in följande kod och modifiera den, så att den skriver ut figurerna a-j en i taget.
"""
print()

for y in range(1, 7):
    s: str = ""
    
    for i in range(0, 10):
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
               if y == 3 or x == 3:
                    s += "#"
               else:
                    s += "."
                    
        # e: weird A
            if i == 4:
               if (x == 5) or (x + y == 7):
                    s += "#"
               else:
                    s += "."
                    
        # f: cross
            if i == 5:
               if (x == y) or (x + y == 7):
                    s += "#"
               else:
                    s += "."
                    
        # g: hash and dot
            if i == 6:
               if (x % 2 == 1):
                    s += "#"
               else:
                    s += "."
                    
        # h: square
            if i == 7:
               if (((y == 2 or y == 5) and 1 < x < 8) or
                    ((2 < y < 5) and (x == 2 or x == 7))):
                    s += "#"
               else:
                    s += "."
                    
        # i: dot, hash and O
            if i == 8:
               if (((3+x) % 3 == 2 and (3 + y) % 3 == 1) or 
                  ((3+x) % 3 == 0 and (3 + y) % 3 == 2) or 
                  ((3+x) % 3 == 1 and (3 + y) % 3 == 0)):
                    s += "#"
               elif (((3+x) % 3 == 0 and (3 + y) % 3 == 1) or 
                    ((3+x) % 3 == 1 and (3 + y) % 3 == 2) or 
                    ((3+x) % 3 == 2 and (3 + y) % 3 == 0)):
                    s += "O"
               else:
                    s += "."
        
        # j: "face"
            if i == 9:
                if ((1 <= y <= 3 and (x == 3 or x == 6)) or 
                    (y == 5 and x % 2 == 0) or 
                    (y == 6 and x % 2 == 1)) :
                    s += "#"
                else:
                    s += "."
                    
        
        s += "  "
    print(s)
print()