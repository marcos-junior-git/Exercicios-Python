def validate_expression():
    expression = input('Type the expression')
    stack = []
    for char in expression:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if len(stack) == 0:
                print('Invalid expression: Extra closing parenthesis')
                return
            stack.pop()
    if len(stack) == 0:
        print('Valid expression')
    else:
        print('Invalid expression: Extra opening parenthesis')
