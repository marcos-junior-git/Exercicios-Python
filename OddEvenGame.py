from random import randint
cont = 0
while True:
        va = int(input('type your number'))
        pi = input('type odd (O) or even (E)').strip().upper()[0]
        rand = randint(1, 10)  #['O', 'E']
        if (pi == 'E') and ((pi + rand) % 2 == 0):
            print(f'You typed {va} and the machine {rand}')
            print(f'you won')
            cont += 1
            print(f'It\'s your {cont}º victory')
        else:
            print(f'You typed {va} and the machine {rand}')
            print(f'you lost, try again')
