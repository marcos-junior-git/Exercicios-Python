def register_people():
    ofLegalAge = 0
    mens = 0
    yw = 0
    while True:
        age = int(input('Age'))
        sex = input('Sex').upper()
        if (age > 18):
            ofLegalAge += 1
        if (sex in 'M'):
            mens += 1
        if (sex in 'Ff') and (age < 20):
            yw += 1
        con = input('do you want to continue? Y/N')
        if (con not in 'Yy'):
            print(f'There are {ofLegalAge} people of Legal Age, {mens} mens, {yw} women minor than 20')
            break

