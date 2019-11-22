#utf-8

def split(a,b):
    try:
        result = round(a / b, 2)
    except ZeroDivisionError:
        print('Ошибка! На 0 делить нельзя!')
        return 'Операция невозможна!'
    return result

a = float(input('Введите первое число: a = '))
b = float(input('Введите второе число: b = '))
print(f'Результат деления a / b =  {split(a,b)}')


