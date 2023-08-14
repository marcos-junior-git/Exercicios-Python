def ordered_numbers():
    a = []
    while True:
        a.append(int(input('Type a number')))
        ask = input('Do you want to continue Y/N')
        if ask == 'N':
            break
    print(f'You typed {len(a)} numbers')
    a.sort(reverse=True)
    print(f'The ordered values are {a}')
    if 5 in a:
        print('The number 5 is inside the list')
    else:
        print('The number 5 is not in the list')
