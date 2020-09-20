file = open('text_01.txt', 'w', encoding = 'utf-8')
while True:
    print('Для выхода нажмите «ввод»')
    data = input('Введите строку: ')
    if data == '':
        break
    file.write(f'{data} \n')
file.close()
# проверка ввода:
file = open('text_01.txt', 'r', encoding = 'utf-8')
list = []
for i in file:
    list += i.split(' ')
    ind = 0
line = 0
for ind in range(len(list)):
    if list[ind] == '\n':
        line += 1
print( f'в файле {len(list)-line} слов')
print(f'В файле {line} строки')
file.seek(0)
print(f'вот что находится в файле:')
print('_'*30)
for form in file:
    print(form, end='')
print('_'*30)
file.close()