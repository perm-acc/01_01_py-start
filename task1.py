from sys import argv

filepath, cost_per_hour, workhours = argv

estimate = int(cost_per_hour) * int(workhours) 

print(f'Ставка за час: {cost_per_hour}')
print(f'Рабочих часов: {workhours}')
print(f'Заработок составляет: {estimate}')
