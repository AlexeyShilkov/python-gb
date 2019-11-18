
with open("text_5.txt", 'w') as f:
    a = input('Введите числа, разделенные пробелами')
    a_1 = list(a.split())
    try:
        print(f'Сумма введенных чисел равна {sum(map(int, a_1))}.')
        f.write(a)
    except ValueError:
        print('Ошибка ввода данных.')

