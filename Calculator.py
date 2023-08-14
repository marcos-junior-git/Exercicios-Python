#!/usr/bin/env python3

a = int(input('Type the first value: '))
b = int(input('Type the second value: '))
c = 0

while c != '5':
    print('[1] Add')
    print('[2] Subtraction')
    print('[3] Multiplication')
    print('[4] Division')
    print('[5] Get Out')

    c = input('Type the operation: ')

    if c == '1':
        print(f'The result is {a + b}')
    elif c == '2':
        print(f'The result is {a - b}')
    elif c == '3':
        print(f'The result is {a * b}')
    elif c == '4':
        print(f'The result is {a / b}')
    elif c == '5':
        print('Exiting...')
    else:
        print('Invalid Option')

