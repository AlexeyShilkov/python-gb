from abc import ABC, abstractmethod

class Clothes(ABC):
    @abstractmethod
    def fabric_consumtion(self, param):
        pass


class Coat(Clothes):
    def __init__(self, v):
        self.v = v

    @property
    def fabric_consumtion(self):
        return f'Расход ткани для пошива пальто {self.v} размера составляет {self.v / 6.5 + 0.5:.2f}'

class Suit(Clothes):
    def __init__(self, h):
        self.h = h

    @property
    def fabric_consumtion(self):
        return f'Расход ткани для пошива костюма на человека ростом {self.h}м  составляет {self.h * 2 + 0.3:.2f}'

coat = Coat(54)
print(coat.fabric_consumtion)

suit = Suit(1.82)
print(suit.fabric_consumtion)
