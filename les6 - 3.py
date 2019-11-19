class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income

class Position(Worker):
    def __init__(self, name, surname, position, income):
        Worker.__init__(self, name, surname, position, income)

    def get_full_name(self):
        print(f'Сотрудник: {self.name} {self.surname}')

    def get_total_income(self):
        self.total_income = int(self._income['wage']) + int(self._income['bonus'])
        print(f'Общий доход сотрудника: {self.total_income} рублей.')

position = Position('Алексей', 'Шилков', 'программист', {'wage': 100000, 'bonus': 50000})
position.get_full_name()
position.get_total_income()
