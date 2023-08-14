def sum_numbers_until_999():
    c = a = b = 0
    a = int(input('type a number, if you want to stop type 999'))
    while a != 999:
        b += a
        c += 1
        a = int(input('type a number, if you want to stop type 999'))
    print(f'you typed {c} numbers the sum is {b}')

