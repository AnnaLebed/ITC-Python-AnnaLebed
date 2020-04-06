my_list = ["Hello", "Anna", "always", "exercises", "append"]
def change_words_starting_with_a(list_to_check):
    try:
        string_add_hello = [i + "hello" if i[0].lower() == "a" else i for i in list_to_check]
        return string_add_hello
    except Exception as e:
        print(e)







#print(change_words_starting_with_a(my_list))