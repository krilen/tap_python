"""
2 Öva på TDD
Samla ihop dina funktioner så att de ligger i en eller flera moduler. 
Importera och anropa dem från main.py, så att main-filen bara innehåller funktionsanrop.

"""

# 2.1
from degree import c_to_f

# 2.2
from words import count_words

# 2.3
from median import find_median

# 2.4
from sort_asc import is_sorted_ascending

def main():
    
    # 2.1 
    degrees: list[float] = [-300, 0]
    
    for degree in degrees:
   
        print(f"If degree in celcius is {degree} than the degree in farenheit is {c_to_f(degree):}.")

    print()

    # 2.2
    sentence = "Hello world this is sentence"
    
    print(f"Sentence: {sentence!r} has {count_words(sentence)} words in it.")
    
    print()
    
    # 2.3
    numbers: list[list[int | float]] = [[74, 3.21, 52, 19.68, 6], [99.05, 13, 45.33, 87, 0.56, 29, 64.78, 5, 13.45, 32], [70.19, 81, 0.72, 48, 90.6]]
    
    for number in numbers:
        print("The median of", end=" '")
        print(*number, sep=", ", end="' ")
        print("is", find_median(number))
        
    print()
    
    # 2.4

    numbers2: list[list[int]] = [[7, 23, 56], [12, 34, 89], [1, 67, 45], [90, 22, 33, 77], [50, 65, 81], [42, 19, 39, 10]]
    
    for number2 in numbers2:
        print("The list of numbers", end=" '")
        print(*number2, sep=", ", end="' ")
        print("is sorted ascending:", is_sorted_ascending(number2))





if __name__ == "__main__":
    
    main()