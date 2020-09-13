def card(name, surname, b_year, city , email, p_num):
    return f'{name}, {surname}, {b_year}, {city}, {email}, {p_num}'
print(card(name = input('Bведите имя: '), surname = input('Введите фамилию: '), b_year = input('Введите год рождения: '), city = input('Введите город проживания: '), email = input('Введите электронную почту: '), p_num = input('Введите номер телефона: ')))