#!/usr/bin/env python3

from random import randint
from time import sleep

obj = ['Rock', 'Paper', 'Scissors']
pc = randint(0, 2)

print('[ 0 ] Rock')
print('[ 1 ] Paper')
print('[ 2 ] Scissors')

var = int(input('Type your play: '))

print(f'Your computer chose {obj[pc]}')

if pc == 0:
    if var == 0:
        print('It\'s a tie!')
    elif var == 1:
        print('You win!')
    elif var == 2:
        print('You lose!')
    else:
        print('Your choice is invalid')
elif pc == 1:
    if var == 1:
        print('It\'s a tie!')
    elif var == 2:
        print('You win!')
    elif var == 0:
        print('You lose!')
    else:
        print('Your choice is invalid')
elif pc == 2:
    if var == 2:
        print('It\'s a tie!')
    elif var == 0:
        print('You win!')
    elif var == 1:
        print('You lose!')
    else:
        print('Your choice is invalid')

for countdown in range(10, 0, -1):
    print(countdown)
    sleep(1)

print('BUM BUM POW!!!!!!!!!!!')

