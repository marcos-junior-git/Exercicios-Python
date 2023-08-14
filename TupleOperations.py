def tuple_operations():
    from random import randint
    tup = (randint(0,10),randint(0,10),randint(0,10),randint(0,10),randint(0,10))
    print(f'The values are {tup}',end='')
    print(f'The higher number is {max(tup)}')
    print(f'The lower number is {min(tup)}')

