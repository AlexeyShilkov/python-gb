# utf - 8

n = int(input('Введите целое положительное число: '))

max = n % 10

while (n // 10) != 0:
    if (n // 10) < 10:
        last_num = n // 10
    else:
        last_num = n % 10
    n = n // 10
    if last_num > max:
        max = last_num

print(f"Наибольшая цифра в данном числе: {max}")

