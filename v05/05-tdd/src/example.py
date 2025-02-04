
# Drar ifrån y från x
def subtract(x, y):
    return x - y


def compare_names(input, name):
    if not isinstance(input, str):
        return False
    if not isinstance(name, str):
        return False
    name_small = name.casefold()
    input_small = input.casefold()
    position = name_small.find(input_small)
    if position == -1:
        return False
    else:
        return True
