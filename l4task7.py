def fact(n):
    fct = 1
    if n == 0:
        yield f'факториал 0 = 1'
    for el in range(1, n+1):
        fct *= el
        yield f'факториал {el} = {fct}'

for el in fact(int(input('Введите число: '))):
    print(el)