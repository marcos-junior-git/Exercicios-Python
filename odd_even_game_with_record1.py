def odd_even_game_with_record():
    from random import randint
    cont = 0
    cont1 = 0
    while True:
        va = int(input('type your number'))
        pi = input('type odd (O) or even (E)').strip().upper()[0]
        rand = randint(1, 10)  # ['O', 'E']
        if (pi == 'E') and ((va + rand) % 2 == 0):
            print(f'You typed {va} and the machine {rand}')
            print(f'you won')
            cont += 1
            print(f'Its your {cont}º victory')
        else:
            print(f'You typed {va} and the machine {rand}')
            print(f'you lost, try again')
            cont1 += 1
            print(f'Its your {cont1}º loss')
        print(f'you have {cont} wins and {cont1} losses')
