#!/usr/bin/env python3

b = 0
q = 0

for a in range(1, 7):
    n = int(input(f'Type the {a} number: '))
    if n % 2 == 0:
        b += n
        q += 1

print(f'You typed {q} even numbers. The sum is {b}')

