# utf-8

result_1 = float(input('Введите результат спортсмена в 1 день '))
result_2 = float(input('Введите результат, которого должен достичь спортсмен '))
day = 1

while result_1 < result_2:
    result_1 = result_1 * 1.1
    day += 1

print(f'На {day}-й день спортсмен достиг результата не менее {result_2}км')

