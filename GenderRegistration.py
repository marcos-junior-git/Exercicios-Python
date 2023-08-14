#!/usr/bin/env python3

c = input('Input your sex (M/F): ').strip().upper()[0]

while c not in 'MF':
    c = input('Invalid option, please type again: ').strip().upper()[0]

print('It is registered now.')

