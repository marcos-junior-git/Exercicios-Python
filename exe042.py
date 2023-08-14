#!/usr/bin/env python3

a = float(input("Digite o lado A do triangulo\n"))
b = float(input("Digite o lado B do triangulo\n"))
c = float(input("Digite o lado C do triangulo\n"))
if (a < b + c) and (b < a + c) and (c < a + b):
    print('Pode formar um triângulo', end=' ')
    if (a != b) and (a != c) and (b != c):
       print('Escaleno')
    elif (a == b) and (a == c) and (b == c):
         print('Equilátero')
    else:
        print('Isósceles')
else:
    print('Não pode formar um triangulo')

