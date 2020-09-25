class Road:
    
    def __init__(self, length, width, weight=25, thickness=5):
        self._length = int(input('Введите длину дороги: '))
        self._width = int(input('Введите ширину дороги: '))
        self._weight = weight
        self._thickness = thickness

    def form_r(self):
        formula = self._length * self._width * self._weight * self._thickness
        if len(str(formula)) > 5:
            formula = str(formula // 1000) + 'т'
        print(f'Округленный результат: {formula}')


r_1 = Road(5000, 20, 25, 5)
r_1.form_r()