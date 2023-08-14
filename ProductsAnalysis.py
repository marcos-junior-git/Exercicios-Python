def products_analysis():
    m1000 = 0
    tot = 0
    cont = 0
    cheap = ''
    while True:
        product = input('Type a product')
        price = float(input('Type the price'))
        cont += 1
        tot += price
        if (price > 1000):
            m1000 += 1
        if (cont == 1):
            small = price
        else:
            if(price < small):
                small = price
        yn = input('Do you want to continue? Y/N').upper()[0]
        if (yn == 'N'):
            break
    print(f'The total price is R${tot}')
    print(f'There are {m1000} that cost more than')
    print(f'and the cheapest is R${small}')

