from sys import argv

def my_def():
    try:
        working_hours, rate, bonus = map(int, argv[1:])
        print(f'Заработная плата = {working_hours * rate + bonus} рублей')
    except ValueError:
        print('Правильно введите параметры.')

my_def()


