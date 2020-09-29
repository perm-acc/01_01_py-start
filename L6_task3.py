class Worker:
    def __init__(self, name='Ivan', surname='Ivanov', position='junior', wage=20000, bonus=5000): #можно убрать серые позиции
        self.name = input('Введите имя: ')
        self.surname = input('Введите фамилию: ')
        self.position = position
        self.wage = int(input('Введите размер зарплаты: '))
        self.bonus = int(input('Введите размер бонуса: '))
        self._income = {'Зарплата': self.wage, 'Бонус': self.bonus}

        print(f' Имя — {self.name} \n Фамилия — {self.surname} \n Должность — {self.position} \n Доход — {self._income}')

class Position(Worker):
    def fullname(self):
        self.f_n = self.name + ' ' + self.surname
        print(self.f_n)

    def income(self):
        print(sum(self._income.values()))

a_1 = Position()
print()
a_1.fullname()
a_1.income()