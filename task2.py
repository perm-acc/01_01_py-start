insert_seconds = int(input('Введите время в секундах: '))

hours = insert_seconds // 3600
minutes = (insert_seconds % 3600) // 60
seconds = (insert_seconds % 3600) % 60

print(hours, ':', minutes, ':', seconds)