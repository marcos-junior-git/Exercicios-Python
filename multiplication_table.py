def multiplication_table():
    while True:
        b = int(input('type a number'))
        if b < 0:
            break
        for c in range(0, 11):
            r = b * c
            print(f'{b} X {c} = {r}')
        print('The End')

