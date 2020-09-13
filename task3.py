def my_func(a, b, c):
    final_sum = sum([a,b,c]) - min([a,b,c])
    return f'Сумма двух наибольших аргументов равна {final_sum}'
print(my_func(10, 11, 12))