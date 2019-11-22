# utf-8

answer = ''
i = 1
my_list = []

while answer != 'n':
    answer = input('Хотите ли Вы добавить новый товар? y/n ')
    if answer == 'y':
        product = input('Введите наименование товара: ')
        try:
            price = int(input('Введите цену товара: '))
        except ValueError:
            print('Введено некорректное значение.')
            continue
        try:
            lot = int(input('Введите количество товара: '))
        except ValueError:
            print('Введено некорректное значение.')
            continue
        unit = input('Введите единицы измерения: ')
        my_dict = {'Название': product, 'Цена': price, 'Количество': lot, 'Ед': unit}
        my_tuple = (i, my_dict)
        i += 1
        my_list.append(my_tuple)

    elif answer == 'n':
        break
    else:
        print('Вы ввели некорректное значение.')

for el in my_list:
    print(el)

# Вторая часть задания

analiz = {}
names = []
prices = []
lots = []
units = []

for el in my_list:
    my_dict = dict(el[1])
    name = my_dict.get("Название")
    names.append(name)
    analiz["Название"] = names

    price = my_dict.get("Цена")
    prices.append(price)
    analiz["Цена"] = prices

    lot = my_dict.get("Количество")
    lots.append(lot)
    analiz["Количество"] = lots

    unit = my_dict.get("Ед")
    units.append(unit)
    analiz["Ед"] = units


for key, value in analiz.items():
    print(f'{key}: {value} ')


