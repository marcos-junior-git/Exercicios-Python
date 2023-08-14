def register_people():
    people = list()
    temp = list()
    higher = lower = 0
    amount = 0
    while True:
        temp.append(input('Type your name'))
        temp.append(float(input('type your weight')))
        if people:
            if temp[1] > higher[1]:
                higher = temp[:]
            if temp[1] < lower[1]:
                lower = temp[:]
        else:
            higher = lower = temp[:]
        people.append(temp[:])
        temp.clear()
        amount += 1
        answer = input('Do you want to continue? Y/N')
        if (answer in 'nN'):
            break
    print(f'You signed up {amount} people')
    print(f'higher weight {higher}')
    print(f'Lower weight {lower}')

