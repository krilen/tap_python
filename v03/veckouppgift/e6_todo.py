"""
6 Todo list (att göra-lista)

Bygg ett program där användaren kan lägga till saker till en todo-lista.
Tips: använd en loop, input och en variabel för listan.

Exempel:
** Todo list extravaganza **
1. Se innehållet i din lista
2. Lägga till nya punkter i din lista
Välj ett alternativ: 1
Din lista är tom
.
Välj ett alternativ: 2
Skriv in en ny sak du måste komma ihåg att göra: mata guldfisken
Ok, lade till "mata guldfisken" i listan.
.
Välj ett alternativ: 1
+ Mata guldfisken
.

Version 2: lägg till ett menyalternativ, "Markera som klar". När användaren väljer det, ska
programmet fråga efter vilken grej man är färdig med. Den färdiga grejen ska tas bort från
listan.

Version 3: lägg över färdiga grejer i en ny lista. Användaren ska kunna välja vad man har
bockat av tidigare, eller välja att lägga tillbaka grejen i todo-listan.
"""

todos: list[str] = []

while True:
    
    print(" ** Todo ** ")
    print(" * 1: See the content of the todo")
    print(" * 2: Add a todo")
    
    
    print("---")
    print(" * c: clear the todo ")
    print(" * q: To quit")
    
    selection: str = input("Choose what to do >> ")
    
    print()
    
    match selection:
        case "1":
            if len(todos) > 0:
                for i, todo in enumerate(todos, start = 1):
                    print(f" + {i}. - {todo}")
        
            else:
                print("Your todo is empty")
        
        case "2":
            todo: str = input("What do you want to add to the todo: >> ")
            print(f"Added: {todo!r} to you todo")
            todos.append(todo)
        
        case "q":
            break
        
        case "c":
            todos.clear()
        
        case _:
            print("That is not a valid selection!")

    print()