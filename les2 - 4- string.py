# utf-8

my_string = input('Введите строку из нескольких слов, разделенных пробелами: ')
my_string = my_string.split() 

for ind, el in enumerate(my_string):
    if len(el) > 10:
        el = el[0:10]
    print(ind, el)
