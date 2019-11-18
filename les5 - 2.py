
with open("text_2.txt") as f:
    content = f.readlines()
    print(f'Файл содержит {len(content)} строки.')

    for num, el in enumerate(content, 1):
        a = list(el.split())
        print(f'Строка - {num}, количество слов - {len(a)}.')


