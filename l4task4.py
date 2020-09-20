from random import randint
gen_list = [randint(-200, 200) for el in range(10)]
new = [item for item in gen_list if gen_list.count(item) == 1]
print(gen_list)
print(f'Список без повторения элементов {new}')