def my_f(d_1, d_2):
    try:
        int(d_1)
    except ValueError as err:
        print ('У делимого нецифровое значение')
    try:
        int(d_2)
    except ValueError as err:
        print ('У делителя нецифровое значение')
    try:
        d = int(d_1) / int(d_2)
    except (ZeroDivisionError,  ValueError) as err:
        print ('Нельзя делить на 0 или нецифровые значения')
    try:
        print(f'Результат: {d}')
    except (UnboundLocalError) as err:
        print ('Результат не определен')
    return
my_f(input('Делимое: '), input('Делитель: '))