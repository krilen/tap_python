"""
Turtle graphics
Python har ett paket med inbyggda, enkla funktioner för grafik: turtle. Tänk dig att du har en robotarm som håller en penna mot ett papper. Man kan ge olika instruktioner till roboten, för att styra den. Några exempel:
forward - gå rakt framåt i standardriktningen (peka ursprungligen åt höger)
backward - gå bakåt
left, right - sväng vänster eller höger ett antal grader, 360 grader för ett helt varv
dot - sätt ut en prick med en viss storlek
speed - normal=6, fast=10, maximal=0

Läs mer här: Turtle graphics — Python 3.13.1 documentation 
Kodexempel:
...
"""
import turtle as t

def square(length: int = 50) -> None:
    t.penup()
    t.left(90)
    t.forward(200)
    t.pendown()
    t.color("green")
    
    for _ in range(4):
        t.right(90)
        t.forward(length)
        
        
    t.penup()
    
# Upprepa 3 gånger
for x in range(3):
    t.forward(100)
    t.left(120)

# Lyft pennan för att flytta utan att rita
t.penup()
t.forward(100)
t.pendown()
t.dot(10, "red")
t.color("blue")
t.forward(50)

square()

# Låt fönstret stanna kvar tills användaren stänger det
t.mainloop()
