#!/usr/bin/env python3

from datetime import date

year = int(input('Type the year you were born: '))
today_year = date.today().year
age = today_year - year

print(f'Your age is {age}')

if age <= 9:
    print('You will compete in the Mirim category')
elif age <= 14:
    print('You will compete in the Children category')
elif age <= 19:
    print('You will compete in the Junior category')
elif age <= 25:
    print('You will compete in the Senior category')
else:
    print('You will compete in the Master category')

