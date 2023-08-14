def separate_even_odd():
    a = []
    b = 0
    while True:
        a.append(int(input('Type a number')))
        ask = input('Do you want to continue Y/N')
        b += 1
        if (ask in 'Nn'):
            break
    pair = []
    odd = []
    for num in a:
        if num % 2 == 0:
            pair.append(num)
        else:
            odd.append(num)
    print(f'The full list is {a}')
    print(f'The pair list is {pair}')
    print(f'The odd list is {odd}')

