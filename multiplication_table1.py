def multiplication_table():
    term = int(input('Type the first term'))
    reas = int(input('Type the reason'))
    cont = 0
    while cont != 10:
        print(f'{term}', end=' -> ')
        term = term + reas
        cont = cont + 1
    print('End')
