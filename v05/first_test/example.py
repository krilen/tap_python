def subtract(x, y):
    return x -y

def compare_names(input, name):
    if not isinstance(input, str):
        return False
    
    if not isinstance(name, str):
        return False
    
    pos = name.casefold().find(input.casefold())
    
    if pos < 0:
        return False
    
    return True