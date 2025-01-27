# 3
def repeat_loop(end: int = 5) -> None:
    """
    Följande kod ska sluta loopa efter 5 varv.
    Flytta den in i en funktion och justera den enligt kommentaren.
    """
    
    y = 1
    
    for x in range(1, 100):
        y *= 2
        
        if x == end:
            break
        
    print(y)


if __name__ == "__main__":
    print("Wrong file to execute")