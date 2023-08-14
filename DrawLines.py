def draw_lines():
    def lines(var):
        print('-' * len(var))
        print(var)
        print('-' * len(var))
    while True:
        var = input('Type something')
        lines(var)
        brea = input('Do you want to keep typing? Y/N')
        if brea == 'N':
            break

