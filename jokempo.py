#!/usr/bin/env python3

from random import randint
obj = ['Rock','Paper','scissors']
pc = randint(0,2)
print('[ 0 ] Rock')
print('[ 1 ] Paper')
print('[ 2 ] scissors')
var = int(input('type your play\n'))
print(f'Your computer chose {obj[pc]}')
if (var == 0):
    if(var == pc):
        print('a tie')
    elif (0 < var < pc):
          print('you lose')
    elif (0 < var > pc):
          print('you win')
