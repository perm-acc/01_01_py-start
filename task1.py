from time import sleep

class TrafficLight:
    __color = 'Красный'

    def running(self):
        print(f'{self.__color}')
        sleep(2)
        self.__color = 'Желтый'
        print(f'{self.__color}')
        sleep(2)
        self.__color = 'Зеленый'
        print(f'{self.__color}')
        sleep(2)

tl_1 = TrafficLight()

print(f'{tl_1.running()}')