a = float(input('Введите результат первого дня в километрах (параметр a) в км: '))
b = float(input('Введите необходимый общий результат в километрах (параметр b) в км: '))
one_percent = a / 100
day_number = 1
overall_day = float(0)
while overall_day <= b:
    overall_day = float(one_percent * 110)
    one_percent = overall_day / 100
    day_number += 1
print(f'На {int(day_number)}-й день спортсмен достигнет результата не менее {int(b)} км')