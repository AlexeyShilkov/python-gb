import time

class TrafficLight:
    __color = ['красный', 'желтый', 'зеленый']

    def running(self, color):
        while True:
            print(color[0])
            time.sleep(7)
            print(color[1])
            time.sleep(2)
            print(color[2])
            time.sleep(7)
            print(color[1])
            time.sleep(2)

a = TrafficLight()
a.running(a._TrafficLight__color)


