num = input('Введите целое положительное число: ')

x = int(num[0])
i = 1

while i < len(num):
    if int(num[i]) >= x:
        x = int(num[i])
        i += 1
    else:
        i += 1

print('Наибольшая цифра в числе', num, ', это —', x)