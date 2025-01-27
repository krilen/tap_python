"""
2 Öva på funktioner och moduler
Samla ihop dina funktioner så att de ligger i en eller flera moduler. 
Importera och anropa dem från main.py, så att main-filen bara innehåller funktionsanrop.
...
"""

from e2_func_strings import print_string, eko
from e2_func_loop import repeat_loop
from e2_func_list import last, cut_edges
from e2_func_other import increase, average, pretty_print


def main():
    
    print("\n1-3\n--------------------")
    
    print_string("David")
    eko("Hej", 13)
    repeat_loop()
    
    print("\n4\n--------------------")
    
    print(last([]))
    print(last([1, 2, 3, 4, 5]))
    print(last(["Jack", "Bob", "Mary"]))
    
    print("\n5\n--------------------")
    
    print(cut_edges([]))
    print(cut_edges([1, 2, 3, 4, 5]))
    print(cut_edges([1, 2]))
    print(cut_edges(["Jack", "Bob", "Mary"]))

    print("\n6\n--------------------")

    print(increase(1))
    
    print("\n7\n--------------------")

    print(average(4, 8))
    print(average(1, 2))
    
    
    print("\n8\n--------------------")

    pretty_print([4, 8])
    pretty_print(["a", 3.14, "Mike"])

if __name__ == "__main__":
    main()