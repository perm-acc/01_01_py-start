class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed #int(input('Введите стартовую скорость: '))
        self.color = color #input('Введите цвет авто: ')
        self.name = name #input('Введите марку авто: ')
        self.is_police = is_police

        print(f'{self.speed}, {self.color}, {self.name}, {self.is_police}')

    def go(self):
        return(f'Авто едет')

    def stop(self):
        return(f'Авто остановилось')

    def turn(self, direction):
        self.direction = direction
        return(f'Авто повернуло {self.direction}')

    def show_speed(self):
        return(f'скорость: {show_speed}')

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name, is_police)

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f'Скорость больше 60, снизьте скорость!'

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f'Скорость больше 40, снизьте скорость!'

class SportCar(Car):
    pass

c_1 = TownCar(70, 'grey', 'Mazda')
print(c_1.go())
print(c_1.show_speed())
print(c_1.turn('налево'))
print(c_1.stop())

print()

c_2 = WorkCar(70, 'black', 'Toyota')
print(c_2.go())
print(c_2.show_speed())
print(c_2.turn('направо'))
print(c_2.stop())

print()

c_3 = SportCar(120, 'red', 'Porsche')
print(c_3.go())

print()

c_4 = PoliceCar(80, 'black', 'Ford')
print(c_4.go())
print(c_4.turn('обратно'))
print(c_4.go())
print(c_4.turn('обратно'))
print(c_4.go())
print(c_4.stop())