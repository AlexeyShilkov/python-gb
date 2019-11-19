class Road:
    _lenght = 'lenght'
    _width = 'width'

    def _asphalt(self, lenght, width):
        return lenght * width * 0.025 * 5

road = Road()
try:
    lenght = int(input('Введите ширину дороги: '))
    width = int(input('Введите длину дороги: '))
    print(f'Для асфальтирования данного участка необходимо {road._asphalt(lenght, width):.2f} тонн асфальта.')
except ValueError:
    print('ValueError')