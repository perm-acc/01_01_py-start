def my_func():
    while True:
        x = int(input('Введите положительное число: '))
        if x > 0:
            break
    while True:
        y = int(input('введите отрицательное чесло: '))
        if y < 0:
            break
    i = abs(y)
    x_d = []
    while i > 1:
        x_d.append(x)
        i -= 1
        x_f = x
    for val in x_d:
        x_f = val * x_f
    return f'введено {x}, {y}, {1/x_f}'
print(my_func())