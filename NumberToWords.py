def number_to_words():
    c = ('Zero','One','Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Eleven','Twelve','Thirteen')
    while True:
        a = int(input('Type a number between 0 and 20'))
        if (a <= 20) and (a >= 0):
            break
        print('Try again ', end='')
    print(f'You typed {c[a]}')

