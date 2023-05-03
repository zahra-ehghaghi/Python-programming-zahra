def get_max():
    grades = [9.6, 9.2, 9.7]
    maxvale_local = max(grades)
    return  maxvale_local


def get_max_min():
    grades = [9.6, 9.2, 9.7]
    maxvale_local = max(grades)
    minvale_local = min(grades)
    return  maxvale_local, minvale_local


def get_maximum():
    celsius = [14, 15.1, 12.3]
    maximum = max(celsius)
    return (maximum)


celsius = get_maximum()

fahrenheit = celsius * 1.8 + 32
print(fahrenheit)


maxvale = get_max()
print(maxvale)

max_min_values = get_max_min()
print( f"Max: {max_min_values[0]}, Min: {max_min_values[0]}")




