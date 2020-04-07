names = ["Anna Lebed", "Igor", "Zlata", "Amir", "Zlata Lebed"]


def name_checker(list_of_names):
    for i in list_of_names:
        yield i


for i in name_checker(names):
    if not i.__contains__(" "):
        print(i)


