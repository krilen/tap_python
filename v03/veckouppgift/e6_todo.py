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
todos_done: list[str] = []

def list_todo(list_todos) -> None:
    for i, todo in enumerate(list_todos, start = 1):
        print(f" + {i}. - {todo}")


while True:
    
    print(" *** Todo *** ")
    print(" * 1: See the todos")
    print(" * 2: Add a todo")
    print(" * 3: Mark a todo done")
    print(" * 4: See the todos that are done")
    print(" * 5: Move a done todo back")
    
    print("---")
    print(" * r: Remove all todos")
    print(" * q: To quit")
    
    selection: str = input("Choose what to do >> ")
    
    print()
    
    match selection:
        # See todos
        case "1":
            if len(todos) > 0:
                print("Current todos:")
                list_todo(todos)
            
            else:
                print("Your todo is empty")
        
        # Add todo
        case "2":
            todo: str = input("What do you want to add to the todo: >> ")
            print(f"Added: {todo!r} to you todo")
            todos.append(todo)
        
        # Mark a todo done
        case "3":
            if len(todos) > 0:
                print("Current todos:")
                list_todo(todos)
                
                try:
                    mark: int = int(input("What todo are done (nr)? >> "))
                                    
                except ValueError:
                    print("That is not a valid todo (nr)!")
                    
                else:
                    done: str = todos.pop(mark -1)
                    print(f"Marked: {done!r} as done")
                    
                    todos_done.append(done)
                    
        case "4":
            if len(todos_done) > 0:
                print("These todos are marked as done:")
                list_todo(todos_done)
                
            else:
                print("Your done todos is empty")

        case "5":
            if len(todos_done) > 0:
                print("These todos are marked as done:")
                list_todo(todos_done)

                try:
                    mark: int = int(input("What done todo to move (nr)? >> "))
                                    
                except ValueError:
                    print("That is not a valid done todo (nr)!")
                    
                else:
                    move: str = todos_done.pop(mark -1)
                    print(f"Marked: {done!r} as done")
                    
                    todos.append(move)
        
        case "q":
            break
        
        case "r":
            todos.clear()
            todos_done.clear()
        
        case _:
            print("That is not a valid selection!")

    print()