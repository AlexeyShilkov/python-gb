# utf-8

def my_func(my_list):
    new_list =[]
    for i in my_list:
        new_list.append(int(i))
    return sum(new_list)

sum_1 = 0

while True:
    list_1 = list(input('Введите числа, разделяя их пробелами. Введите q для завершения. ').split())
    list_2 = []
    for el in list_1:
        if el != 'q':
            list_2.append(el)
        elif el == 'q':
            break
    sum_1 = sum_1 + my_func(list_2)
    print(f'Сумма: {sum_1}')
    if el == 'q':
        break












