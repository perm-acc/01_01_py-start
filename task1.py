def my_f(d1 = input('Делимое: '), d2 = input('Делитель: ')):
    try:
        int(d1)
    except ValueError as err:
        print ('У делимого нецифровое значение')
    try:
        int(d2)
    except ValueError as err:
        print ('У делителя нецифровое значение')
    try:
        d = int(d1) / int(d2)
    except (ZeroDivisionError,  ValueError) as err:
        print ('Нельзя делить на 0 или нецифровые значения')
    try:
        print(f'Результат: {d}')
    except (UnboundLocalError) as err:
        print ('Результат не определен')
    return
my_f()