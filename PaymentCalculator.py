#!/usr/bin/env python3

var = float(input('Type the price of the product: '))
print('========== Payment Methods ==========')
print('[ 1 ] Cash Payment / Check')
print('[ 2 ] Cash Payment / Card')
print('[ 3 ] 2x in Card')
print('[ 4 ] 3x or more in card')

var2 = input('Type the payment method: ')

if var2 == '1':
    discounted_price = var - (var * 0.10)
    print(f'Your purchase was R${var:.2f}, now it is R${discounted_price:.2f}')
elif var2 == '2':
    discounted_price = var - (var * 0.05)
    print(f'Your purchase was R${var:.2f}, now it is R${discounted_price:.2f}')
elif var2 == '3':
    print(f'Your purchase remains R${var:.2f}')
else:
    par = int(input('Type how many parcels: '))
    total = var + (var * 0.20)
    parcels = total / par
    print(f'Your purchase was R${var:.2f}, now it is R${total:.2f}')

