file = open('text_05.txt', 'w', encoding = 'utf-8')
data = []
overall = []
while True:
    print('Для выхода нажмите «ввод»')
    data = input('Введите через пробел значения: ')
    overall += data.split()
    print(overall)

    if data == '':
        break
for i in range(len(overall)):
    overall[i] = int(overall[i])

print(overall)
print(f'{sum(overall)} \n')

file.write(f'{overall} \n Сумма всех чисел: {sum(overall)}')
file.close()