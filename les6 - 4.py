class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'Автомобиль {self.name} начал движение.')

    def stop(self):
        print(f'Автомобиль {self.name} остановился.')

    def turn(self, direction):
        print(f'Автомобиль {self.name} повернул {direction}')

    def show_speed(self):
        print(f'Автомобиль {self.name} движется со скоростью {self.speed} км/ч.')


class TownCar(Car):

    def __init__(self, speed, color, name, is_police):
        Car.__init__(self, speed, color, name, is_police)
        self.speed = speed
    def show_speed(self):
        if self.speed > 60:
            print(f'Автомобиль {self.name} движется со скоростьб {self.speed} км/ч.\nВы превысили скорость!')
        else:
            print(f'Автомобиль {self.name} движется со скоростью {self.speed} км/ч.')

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        Car.__init__(self, speed, color, name, is_police)

class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        Car.__init__(self, speed, color, name, is_police)
    def show_speed(self):
        if self.speed > 60:
            print(f'Автомобиль {self.name} движется со скоростьб {self.speed} км/ч.\nВы превысили скорость!')
        else:
            print(f'Автомобиль {self.name} движется со скоростью {self.speed} км/ч.')

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        Car.__init__(self, speed, color, name, is_police)

towncar = TownCar(90, 'синий', 'Lada Vesta', False)
towncar.go()
towncar.show_speed()
towncar.turn('направо')
towncar.stop()

sportcar = SportCar(200, 'красный', 'Ferrary F60', False)
sportcar.go()
sportcar.show_speed()
sportcar.turn('налево')
sportcar.stop()

workcar = WorkCar(60, 'серый', 'Ford Tranzit', False)
workcar.go()
workcar.show_speed()
workcar.turn('налево')
workcar.stop()

policecar = PoliceCar(150, 'серый', 'BMW 5', True)
policecar.go()
policecar.show_speed()
policecar.turn('направо')
policecar.stop()