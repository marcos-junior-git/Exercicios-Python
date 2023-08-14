#!/usr/bin/env python3

import datetime
from datetime import date

an = int(input('Enter your year of birth: '))
Hoje = date.today()
anoHoje = Hoje.year
a = anoHoje - an

if a == 18:
    print(f'If you were born in {an}, you are {a} years old.')
    print('You should enlist this year.')
elif a < 18:
    years_remaining = 18 - a
    print(f'If you were born in {an}, you are {a} years old.')
    print(f'You have {years_remaining} years left. You should enlist in {(years_remaining) + anoHoje}.')
else:
    years_missed = a - 18
    enlistment_year = an + 18
    print(f'If you were born in {an}, you are {a} years old.')
    print(f'You should have enlisted {years_missed} years ago.')
    print(f'Your enlistment year was {enlistment_year}.')

