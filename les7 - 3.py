class Cell:
    def __init__(self, unit):
        self.unit = unit

    def __add__(self, other):
        return f'Результат объединения двух клеток - клетка с количеством ячеек {self.unit + other.unit}'

    def __sub__(self, other):
        if self.unit - other.unit > 0:
            return f'Результат вычитания второй клетки из первой - клетка с количеством ячеек {self.unit - other.unit}'
        else:
            return f'Вычитание невозможно.'

    def __mul__(self,other):
        return f'Результат умножения двух клеток - клетка с количеством ячеек {self.unit * other.unit}'

    def __truediv__(self, other):
        return f'Результат деления двух клеток - клетка с количеством ячеек {self.unit // other.unit}'

    def make_order(self, unit_row):
        return '\n'.join(['*' * unit_row for i in range(self.unit // unit_row)]) + '\n' + '*' * (self.unit % unit_row)

c_1 = Cell(22)
c_2 = Cell(4)

print(c_1 + c_2)
print(c_1 - c_2)
print(c_1 * c_2)
print(c_1 / c_2)
print(c_1.make_order(7))
