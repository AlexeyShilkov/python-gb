try:
    with open("text_3.txt") as f:
        content = f.readlines()
        list_20000 = []
        my_sum = []
        for el in content:
            my_list = list(el.split())
            my_sum.append(int(my_list[1]))
            if int(my_list[1]) < 20000:
                list_20000.append(my_list[0])
        print(f'Зарплату менее 20000 рублей получают следующие сотрудники: {", ".join(list_20000)}')
        print(f'Средняя зарплата составляет {sum(my_sum) / len(my_sum):.2f} рублей.')
except ValueError:
    print("Проверьте правильность значений в файле text_3.txt")
except IndexError:
    print("Не заполнены все данные в файле text_3.txt")
except FileNotFoundError:
    print("Файл с данными не найден.")
