#!/usr/bin/env python3

# Input the house value, salary, and financing duration
house_value = float(input('Enter the house value: '))
salary = float(input('Enter your salary: '))
financing_years = float(input('Enter the financing duration (in years): '))

# Calculate the monthly installment
monthly_installment = house_value / (financing_years * 12)

# Print the monthly installment
print(f'For a house worth {house_value} over {financing_years} years, the monthly installment will be {monthly_installment:.2f}')

# Check if the mortgage is approved or denied
if monthly_installment > (salary * 0.30):
    print('Denied')
else:
    print('Approved')

