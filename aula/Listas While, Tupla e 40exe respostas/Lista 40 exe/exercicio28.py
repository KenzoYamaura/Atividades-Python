'''Escrever um algoritmo que leia um valor para uma variável N de 1 a 10 e 
calcule a tabuada de N. Mostre a tabuada na forma: 0 x N = 0, 1 x N = 1N, 
2 x N = 2N, ..., 10 x N = 10N
'''

numero = int(input('Insira um número: '))
multiplicador = 0

if 1 <= numero <= 10:
    while multiplicador <= 10:
        resultado = numero * multiplicador
        print(f'{numero} X {multiplicador} = {resultado}')
        multiplicador += 1
else:
    print('Não está entre os numero 0 a 10')