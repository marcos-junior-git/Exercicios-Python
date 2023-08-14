def calculate_rectangle_area():
    def area(larg, comp):
        are = larg * comp
        print(f'The width is {larg}')
        print(f'The length is {comp}')
        print(f'The area is {are}')
    larg = float(input('Type the width'))
    comp = float(input('Type the length'))
    area(larg, comp)

