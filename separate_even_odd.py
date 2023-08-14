def separate_even_odd():
    pair = list()
    odd = list()
    for c in range(1, 8):
        var = int(input(f'Type the {c}º number'))
        if (var % 2 == 0):
            pair.append(var)
            pair.sort()
        else:
            odd.append(var)
            odd.sort()
    print(f'The pair list is {pair}')
    print(f'The odd list is {odd}')

