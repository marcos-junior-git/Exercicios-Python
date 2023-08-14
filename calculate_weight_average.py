def calculate_weight_average():
    sum_weights = 0
    for c in range(1, 6):
        weight = float(input(f'Type the weight of the {c} person'))
        sum_weights += weight
    average = sum_weights / 5
    print(f'The sum of all weights is {sum_weights}')
    print(f'The average of all weights is {average}')
