insert_seconds = int(input('Введите время в секундах: '))

hours = insert_seconds // 3600
minutes = (insert_seconds % 3600) // 60
seconds = (insert_seconds % 3600) % 60

if len(str(hours)) == 1:
	hours = '0'+ str(hours)
if len(str(minutes)) == 1:
	minutes = '0' + str(minutes)
if len(str(seconds)) == 1:
	seconds = '0' + str(seconds)

print(hours, ':', minutes, ':', seconds)