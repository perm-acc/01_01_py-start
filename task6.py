file = open('text_6.txt', 'r', encoding = 'utf-8')

list = []
dict = {}

for i in file:
     list += i.split()
#print(list) #проверка

for item in range(len(list)):
    z = ''
    a = list[item]
    for el in a:
        if el.isdigit() == True:
            z += el
        elif el == '-':
            list[item] = 0
            break
        else:
            continue
    if z.isdigit() == True:
        list[item] = int(z)

for item in range(len(list)):
    if item % 4 == 0:
        dict[list[item]] = list[item+1] + list[item+2] + list[item+3]
#print(list) #проверка
print(dict)
file.seek(0)
file.close()