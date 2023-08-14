#!/usr/bin/env python3

from random import randint

num = randint(1, 10)
k = 0

c = int(input('Type a number between 1 and 10: '))

while c != num:
    if c > num:
        c = int(input('Less. You are WRONG. Try again: '))
    else:
        c = int(input('More. You are WRONG. Try again: '))
    
    k += 1

print(f'Congratulations! The number is {num}. You won after {k} tries.')

