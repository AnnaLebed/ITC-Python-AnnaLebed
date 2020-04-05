def is_parsable(input):
        try:
            num = int(input)
        except ValueError:
            return False
        return True


#print(is_parsable('25'))
