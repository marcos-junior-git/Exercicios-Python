def even_or_odd_game():
    s = 0
    r = 0
    while True:
        a = int(input('Enter a number'))
        if a == 999:
            break
        s = s + 1
        r += a
    print(f'you typed {s} numbers, the sum of them is {r}')
