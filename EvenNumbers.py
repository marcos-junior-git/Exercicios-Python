#!/usr/bin/env python3

# Print even numbers between 2 and 50
for c in range(2, 50 + 1, 2):
    print(c, end=' ')

print('Acabou')

# Calculate the sum of odd numbers divisible by 3 between 1 and 500
a = 0
cont = 0

for c in range(1, 501, 2):
    if c % 3 == 0:
        a += c
        cont += 1

print(f'The sum of all {cont} values is {a}')

