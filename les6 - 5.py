class Stationery:
    title = "stationery"

    def draw(self):
        print(f'Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print(f'Запуск отрисовки. Рисуем ручкой.')

class Pencil(Stationery):
    def draw(self):
        print(f'Запуск отрисовки. Рисуем карандашом.')

class Handle(Stationery):
    def draw(self):
        print(f'Запуск отрисовки. Рисуем маркером.')

stationery = Stationery()
stationery.draw()

pen = Pen()
pen.draw()

pencil = Pencil()
pencil.draw()

handle = Handle()
handle.draw()
