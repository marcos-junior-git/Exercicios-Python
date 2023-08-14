def arithmetic_progression():
    ft = int(input('Type the first term\n'))
    r  = int(input('Type the reason\n'))
    ten= ft + (10 -1) * r
    for c in range(ft, ten + r, r):
        print(f'{c} ->', end=' ')
    print('End')
