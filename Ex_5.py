def build_pyramid():
    x = 9
    for i in range(1, 10, 2):
        print(' ' * x + i * '*')
        x = x - 1


build_pyramid()