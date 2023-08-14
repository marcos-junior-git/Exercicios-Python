def separate_even_odd():
    a = []
    while True:
        a.append(int(input('Type a number')))
        ask = input('Do you want to continue Y/N')
        if ask == 'N':
            break
    even = [num for num in a if num % 2 == 0]
    odd = [num for num in a if num % 2 != 0]
    print(f'The full list is {a}')
    print(f'The even list is {even}')
    print(f'The odd list is {odd}')
