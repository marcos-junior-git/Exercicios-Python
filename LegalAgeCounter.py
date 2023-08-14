def count_legal_age():
    from datetime import date
    todays = date.today()
    year = todays.year
    a = 0
    b = 0
    for c in range(1, 8):
        var = int(input(f'type the birth year of the {c}º person'))
        if (year - var >= 18):
            a = a + 1
        else:
            b = b + 1
    print(f'There are {a} peoples of age and {b} minor')
