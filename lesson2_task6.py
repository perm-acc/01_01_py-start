#формируем список
warehouse = [0]
# warehouse.append([1, {'Название': 'Джем', 'Цена': 100, 'Количество': 5, 'Мера': 'банки'}])
# warehouse.append([2, {'Название': 'Вафли', 'Цена': 120, 'Количество': 20, 'Мера': 'штуки'}])
# warehouse.append([3, {'Название': 'Мармелад', 'Цена': 90, 'Количество': 30, 'Мера': 'упаковки'}])
# warehouse.append([4, {'Название': 'Конфеты', 'Цена': 30, 'Количество': 90, 'Мера': 'штуки'}])
#меню
menu = 0
while True:
    print('-'*10,'Меню','-'*10)
    print('1. Добавить позицию')
    print('2. Убрать позицию')
    print('3. Вывести все товары')
    print('4. Просмотр аналитики')
    print('5. Выход')
    print('-'*24)
    menu = input('Введите пункт меню: ')
    print()
# Выход_________________________________________
    if int(menu) == 5:
        print('-'*10,'Выход','-'*10)
        break
# Добавить позицию______________________________
    elif int(menu) == 1:
        print('-'*2,'Ввод новой позиции:','-'*2)
        item = []
        card = {}
        #id = input('введите ячейку товара')
        item.append(len(warehouse))
        card['Название'] = input('Введите название товара: ')
        card['Цена'] = int(input('Введите цену товара: '))
        card['Количество'] = int(input('Введите количество товара: '))
        card['Мера'] = input('Введите меру товара: ')
        item.append(card)
        current_item = item #tuple(item) — если сделаю кортеж, то это не даст возможность редактировать позиции
        warehouse.append(current_item)
        print('-'*5,'Позиция успешно добавлена!','-'*5)
        print()
# Вывести все товары____________________________
    elif int(menu) == 3:
        for positions in warehouse:
            print(positions)
        print('_'*70)
# Убрать позицию________________________________
    elif int(menu) == 2:
        print()
        print('Вот все текущие позиции:')
        for positions in warehouse:
            print(positions)
        print()
        while True:
            print('для отмены введите 0')
            del_position_num = int(input('Введите id позиции для удаления: '))
            print(warehouse[del_position_num][0])
            if del_position_num == 0:
                break
            elif del_position_num < len(warehouse):
                del warehouse[del_position_num]
                i = len(warehouse)
                while i > del_position_num:
                    warehouse[i-1][0] = i-1
                    i -= 1
                print()
                break
# Аналитика________________________________
    elif int(menu) == 4:
        print('-'*5,'Просмотр аналитики','-'*5)
        analytics = {}
        an_pos = []
        an_price = []
        an_amount = []
        an_units = []
        i = 1
        while True:
            if i < len(warehouse):
                an_pos_ind = str(warehouse[i][1]['Название'])
                an_pos.append(an_pos_ind)

                an_price_ind = int(warehouse[i][1]['Цена'])
                an_price.append(an_price_ind)

                an_amount_ind = int(warehouse[i][1]['Количество'])
                an_amount.append(an_amount_ind)

                an_units_ind = str(warehouse[i][1]['Мера'])
                an_units.append(an_units_ind)
                i += 1

            elif i == len(warehouse):
                break

        analytics.update({'Названия позиций': an_pos})
        analytics.update({'Цены': an_price})
        analytics.update({'Количество': an_amount})
        analytics.update({'Мера': an_units})

        for k, v in analytics.items():
            print(k, v)
        print()