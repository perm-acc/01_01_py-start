from random import randrange
#gen_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55] #проверка
gen_list = []
result = []

for i in range(13):
    gen_list.append(randrange(300))

for item in range(len(gen_list)):
    if item == 0:
        continue
    if gen_list[item] > gen_list[item-1]:
        result.append(gen_list[item])

print(f'Результат сортировки: {result}')
#проверка: [12, 44, 4, 10, 78, 123]