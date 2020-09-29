class Stationery:
    def __init__(self, title='Название'):
        self.title = title

    def draw(self):
        print('Запуск отрисовки:')

class Pencil(Stationery):
    def draw(self):
        return f'рисуем грифелем {self.title}'

class Pen(Stationery):
    def draw(self):
        return f'рисуем чернилами {self.title}'

class Handle(Stationery):
    def draw(self):
        return f'рисуем перманентным {self.title}'

begin = Stationery()
begin.draw()

s_p = Pen('ручки')
print(s_p.draw())

s_pe = Pencil('карандаша')
print(s_pe.draw())

s_h = Handle('маркером')
print(s_h.draw())