# utf-8

rating = [8, 6, 5, 3]
answer = ()

while answer != 'n':
    answer = input('Хотите ли вы добавить новый элемент рейтинга? y/n: ')

    if answer == 'y':
        try:
            new_el = int(input('Введите новый элемент рейтинга: '))
        except ValueError:
            print('Введено некорректное значение.')
            continue

        for i in rating:
            if new_el > int(i):
                rating.insert(rating.index(i), new_el)
                print(f'Текущий рейтинг: {rating}')
                break
        if new_el < int(rating[-1]):
            rating.append(new_el)
            print(f'Текущий рейтинг: {rating}')
    elif answer == 'n':
        print(f'Текущий рейтинг: {rating}')
        break
    else:
        print('Введите корректный ответ.')

