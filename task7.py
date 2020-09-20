import json
file = open('text_7.txt', 'r', encoding = 'utf-8')

list = []
dict = {}
final = []
average = {}

for i in file:
    list += i.split()
print(f'Cодержимое файла в списке: ')
print(list)

for i in range(len(list)):
    if list[i].isdigit() == True:
        list[i] = int(list[i])
    else:
        continue
print(f'Cодержимое файла c числительными: ')
print(list)

for i in range(len(list)):
    if i % 4 == 0:
        if list[i+2] - list[i+3] < 0:
            continue
        else:
            dict[list[i]] = list[i+2] - list[i+3]
print(f'Словарь: ')
print(f'{dict} — {type(dict)}, финальный')

all = 0
comp = 0
for val in dict:
    all += dict[val]
    comp += 1
av = all / comp
average['average_profit'] = int(av)
print(f'{average}')

final.append(dict)
final.append(average)

print(f'{final}')
file.close()

with open('text_7-conv.json', 'w', encoding = 'utf-8') as json_conv:
    json.dump(final, json_conv, sort_keys=True, indent=2, ensure_ascii=False)