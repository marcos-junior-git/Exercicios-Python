def count_steps():
    import time
    def step1():
        print('~' * 20)
        print('Count one by one')
        print('~' * 20)
        for c in range(1, 11):
            print(f'{c}', end=' ')
            time.sleep(0.2)
        print('')
    def step2():
        print('~' * 21)
        print('Regressing two by two')
        print('~' * 21)
        for b in range(10, -1, -2):
            print(b, end=' ')
            time.sleep(0.2)
        print('')
    def step3(var1, var2, var3):
        print('=' * 20)
        print(f'Counting from {var1} to {var2} for {var3} by {var3}')
        for a in range(var1, var2+1, var3):
            print(a, end=' ')
            time.sleep(0.2)
        print('End')
    print("Now it's your time to choose the counting")
    step1()
    step2()
    var1 = int(input('Start'))
    var2 = int(input('Finish'))
    var3 = int(input('Step'))
    step3(var1, var2, var3)
