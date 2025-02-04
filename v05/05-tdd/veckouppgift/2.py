
# 2.3 Följande kod ska sluta loopa efter 5 varv. Flytta den in i en funktion och
# justera den enligt kommentaren.
def loop():
    end = 5
    y = 1
    for x in range(1, 100):
        y *= 2
        if x == end:
            return y

return_value = loop()
print( return_value )


def check_sort_list(list_in):
    x = 0
    if len(list_in) == 0:
        print('\nThe list is empty!')
    else:
        #print(f"\nThe list has {len(list_in)} elements:")
        print('\nThe list has', len(list_in), 'elements:')
        # i brukar betyda "index" och användas för tal
        for item in list_in:
            x += 1
            print(str(x) + '. ' + str(item))


check_sort_list(["röd", "gul", "grön"])

check_sort_list([])