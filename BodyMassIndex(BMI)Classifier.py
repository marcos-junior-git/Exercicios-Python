#!/usr/bin/env python3

w = float(input('Type your weight in kg: '))
h = float(input('Type your height in cm: ')) / 100  # Convert height to meters
imc = w / (h * h)

print(f'Your BMI is {imc:.2f}')

if imc <= 18.5:
    print('You are underweight')
elif 18.5 < imc <= 25:
    print('You are in the ideal weight range')
elif 25 < imc <= 30:
    print('You are overweight')
elif 30 < imc <= 40:
    print('You are obese')
else:
    print('You are morbidly obese')

