# utf-8

def degree(x, y):
    print(f'Результат возведения числа {x} в степень {y} равен {x**y}')

def degree_2(x,y):
    a = x
    i = 1
    while i < abs(y):
        a = a * x
        i +=1
    print(f'Результат возведения числа {x} в степень {y} равен {1 / a}')

x = 0
y = 0
while x <= 0:
    try:
        x = float(input('Введите любое положительное число x = '))
    except ValueError:
        continue

while y >= 0:
    try:
        y = int(input('Введите целое отрицательное число y = '))
    except ValueError:
        continue

degree(x, y)

degree_2(x, y)



