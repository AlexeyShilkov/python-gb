# utf - 8

revenue = int(input('Введите сумму выручки вашей компании: '))
costs = int(input('Введите сумму издержек вашей компании: '))

if revenue > costs:
    print('Ваша компания работает с прибылью')
    profit = revenue - costs
    rent = (profit / revenue) * 100
    print(f"Рентабельность вашей компании составляет: {rent:.2f}%")
    staff = int(input('Введите количество сотрудников вашей компании: '))
    profit_stuff = profit / staff
    print(f"Прибыль на одного сотрудника составляет: {profit_stuff:.2f}")
elif revenue < costs:
    print('Ваша компания работает с убытками')
elif revenue == costs:
    print('Ваша прибыль равна издержкам')