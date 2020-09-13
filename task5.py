def summary():
    i = 0
    inp = []
    save = []
    while True:
        i += 1
        print('для выхода введите x')
        print ('')
        inp = input('вводите числа через пробел: ').split()
        save += inp
# модуль выхода и удаления знака x
        if 'x' in inp:
            inp.remove('x')
            save.remove('x')
            for m in range(len(inp)):
                inp[m] = int(inp[m])
            for m in range(len(save)):
                save[m] = int(save[m])
            break
# модуль продолжения подсчета
        else:
            for m in range(len(inp)):
                inp[m] = int(inp[m])
            for m in range(len(save)):
                save[m] = int(save[m])
            print(f'промежуточная общая сумма: {sum(save)}, сумма итерации {i}: {sum(inp)}')
            print('-'*40)
    return f'Финальная сумма {sum(save)}, сумма завершающей итерации {i}: {sum(inp)}'
print(summary())