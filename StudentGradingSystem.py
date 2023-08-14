#!/usr/bin/env python3

a1 = float(input('Type your first grade: '))
a2 = float(input('Type your second grade: '))
a3 = float(input('Type your third grade: '))
ave = (a1 + a2 + a3) / 3

print(f'Your final grade is {ave:.2f}')

if ave < 5.0:
    print('Disapproved')
elif ave >= 5.0 and ave <= 6.9:
    print('Recovery')
else:
    print('Approved')

