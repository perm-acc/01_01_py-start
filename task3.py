month = input('Введите номер месяца: ')

winter = [1, 2, 12]
spring = [3, 4, 5]
season = {
6 : 'Лето',
7 : 'Лето',
8 : 'Лето',
9 : 'Осень',
10 : 'Осень',
11 : 'Осень'
}

if season.get(int(month)) != None:
    print(season.get(int(month)))
if int(month) in winter:
    print('Зима')
elif int(month) in spring:
    print('Весна')