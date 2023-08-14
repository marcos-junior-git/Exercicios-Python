def prime_number_check():
    m = 0
    v = int(input('Type a number\n'))
    for c in range(1, v + 1):
        if (v % c == 0):
            print(f'can be divided for {c}')
            m = m + 1
    if (m == 2):
        print(f'it was divided {m} time, so this number is prime')
    else:
        print(f'it was divided {m} time, so this number is not prime')

