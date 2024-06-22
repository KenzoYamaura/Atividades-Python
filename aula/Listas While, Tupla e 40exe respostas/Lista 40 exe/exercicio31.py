'''Elabore um algoritmo que apresente os números pares maiores que 10 no 
intervalo fechado [A, B]. Sendo que A e B serão números inteiros escolhidos 
pelo usuário. Um número é par quando este satisfaz a seguinte condição: 
(NÚMERO mod 2 = 0)'''


a = int(input('Digite um número: '))
b = int(input('Digite outro número: '))

element= 0

if a > 10 and b > 10:
    if a > b:
        resultado = a - b
    else:
        resultado = b - a

    while resultado >= 0:
        if resultado % 2 == 0:
            element += 1
            resultado -= 1
        else:
            resultado -= 1

    if a > b:
        print(f'Existem {element} números pares entre intervalos de {b,a}')
    elif b > a:
        print(f'Existem {element} números pares entre intervalos de {a,b}')
else:
    print('os números devem ser maiores que 10:')