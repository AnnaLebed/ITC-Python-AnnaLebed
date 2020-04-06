import math


def list_square_even_power_odd(list_range):
    try:
        new_list = [(math.sqrt(i)) if (i % 2 == 0) else i ** 2 for i in list_range]
        return new_list
    except TypeError:
        print("Oops! The data should be integer!")
        return False


#print(list_square_even_power_odd(range(8)))