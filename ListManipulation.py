def list_manipulation():
    tup = ('Pen', 1, 'Pencil', 0.5, 'Eraser', 2, 'Notebook', 10)
    print(tup, end='.................$\n')

    a = []
    for c in range(1, 6):
        a.append(int(input('type some number')))
    print(f'You typed {a}')
    for co, v in enumerate(a):
        print(f'In the {co}º was find the value {v}')
    print(f'The higher number is {max(a)}')
    print(f'The higher number is {min(a)}')

