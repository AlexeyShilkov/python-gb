my_dict ={"one": "один", "two": "два", "three": "три", "four": "четыре"}

with open("text_4_2.txt", 'w') as f_2:
    with open("text_4_1.txt") as f_1:
        line = f_1.read().split("\n")
        for el in line:
            el = el.split(" - ")
            f_2.writelines(my_dict[el[0]] + ' - ' + el[1] + '\n')
