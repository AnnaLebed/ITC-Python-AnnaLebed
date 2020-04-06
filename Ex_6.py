def build_pyramid_with_given_height(height):
    if not type(height) is int:
        raise TypeError("Only integers are allowed")
    elif height <= 0:
        raise Exception("Sorry, no numbers zero and below")
    else:
        n = (2 * height) - 2
        for i in range(0, height):
            for j in range(0, n):
                print(end=' ')
            n = n - 1
            for j in range(0, i + 1):
                print("*", end=" ")
            print(" ")


build_pyramid_with_given_height(0)