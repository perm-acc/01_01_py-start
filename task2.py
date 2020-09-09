mylist = input('Введите значения списка через запятую: ')
mylist = mylist.split(',')
#mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
a = mylist[1::2]
b = mylist[0::2]
overall_list = []
i = 0
if len(a)< len(b):
    while i < len(a):
        overall_list.append(a[i])
        overall_list.append(b[i])
        i += 1
else:
    while i < len(b):
        overall_list.append(a[i])
        overall_list.append(b[i])
        i += 1
if len(mylist) % 2 != 0:
    last = mylist[-1]
    overall_list.append(last)
print(overall_list)