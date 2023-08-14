def ordered_numbers():
    a = []
    b = 0
    while True:
        a.append(int(input('Type a number')))
        c = input('Do you want to continue Y/N')
        b += 1
        if (c in 'Nn'):
            break
    print(f'You typed {b} numbers')
    d = sorted(a, reverse=True)
    print(f'The ordered values are {d}')
    if (5 in a):
        print(f'The number 5 is inside the list')
    else:
        print(f'The number 5 is not in the list')

