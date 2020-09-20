file = open('text_3.txt', 'r', encoding = 'utf-8')
list = []
for i in file:
    list += i.split('\n')
try:
    for i in range(len(list)):
        if list[i] == '':
            del list[i]
        else:
            continue
except:
    pass
s = ' '
s = s.join(list)
list = s.split(' ')
for i in range(len(list)):
    try:
        list[i] = float(list[i])
    except ValueError:
        pass
dict = {}
for i in range(len(list)):
    if i % 2 == 0:
        dict[list[i]] = list[i+1]
    elif i % 2 == 1:
        continue
for i in dict :
    print(i, dict[i])
less = []
for i in dict :
    if float(dict[i]) < 20000.0:
        less.append(i)
middle = 0
res = 0
people = 0
for i in dict :
    middle += float(dict[i])
    people += 1
res = middle / people
print( f'Повышать заработную плату необходимо сотрудникам: {", ".join(less)}')
print( f'Средняя ЗП: {res}')
file.seek(0)
file.close()