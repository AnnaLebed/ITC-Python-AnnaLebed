def is_even(number):
    if isinstance(number, float):
        print("Number should be an integer!!!")
        exit()
    elif number % 2 == 0:
        return True
    else:
        return False



