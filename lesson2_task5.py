rating = [7, 5, 3, 3.0, 2]
while True:
    print('Для того чтобы выйти введите любое отрицательное значение')
    num = input('Введите числа больше 0:')
    final_rate = [0]
    if int(num) < 0:
        break
    rating.append(int(num))
    i = 0
    while i < len(rating):
        print(rating[i], rating.index(rating[i]))
        z = 0
        while z < len(rating):
            if rating[i] > final_rate[z]:
                final_rate.insert(final_rate.index(final_rate[z]), rating[i])
                mem = 0
                break
            z += 1
        i += 1
    final_rate.remove(0)
    print(final_rate)
    print(sorted(rating, reverse=True), ' — проверка')