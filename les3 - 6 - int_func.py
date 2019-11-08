#utf_8

def int_func(word):
    new_word = word.title()
    return new_word

my_list = list(input('Введите строку из слов, сосотоящих из маленьких букв, разделенных пробелом: ').split())
new_list = []
for el in my_list:
    new_list.append(int_func(el))

my_string = ' '.join(new_list)
print(my_string)