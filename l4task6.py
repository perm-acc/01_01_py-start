from itertools import count, cycle

num_input = int(input('Введите целое число, с которого необходимо начать отсчет: '))
num_end = int(input('Введите целое число, до которого необходимо выполнить генерацию: '))

for i in count(num_input, 1):
    if i > num_end:
        break
    print(i)
print()

list = []
while True:
    print('Для перехода к количеству итераций, введите значение «N»')
    items = input('Введите элементы списка: ')
    list += items.split()

    if items == 'n':
        list.remove('n')
        break
    elif items == 'N':
        list.remove('N')
        break

iterations = int(input('Введите количество итераций: '))

i = 0
for el in cycle(list):
    if i > iterations:
        break
    print(el)
    i += 1