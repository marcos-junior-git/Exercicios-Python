def unique_numbers():
    lista = []
    while True:
        var1 = int(input('Type a number without repeat'))
        if (var1 not in lista):
            lista.append(var1)
            print('Number added')
        else:
            print('You already typed it')
        var2 = input('Do you want to continue? Y/N')
        if (var2 == 'N') or (var2 == 'n'):
            break
    print(f'You typed these numbers {sorted(lista)}')

