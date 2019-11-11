from itertools import count, cycle

n = ''
try:
    n = int(input('Введите число, начиная с которого будет генерироваться бесконечный список целых чисел: '))
    for el in count(n):
        print(el)
        if el > 100:
            break
except ValueError:
    print('Введите корректное значение.')

n = 0
my_list = input('Введите элементы списка: ')
for el in cycle(my_list):
    print(el)
    n += 1
    if n > 100:
        break
