'''
Escreva um algoritmo que leia um valor inicial A e imprima a sequência de 
valores do cálculo do fatorial: A! e o seu resultado. Ex: 5! = 5 X 4 X 3 X 2 X 
1 = 120
'''

numero = int(input('Insira um Número: '))
fatorial = 1
contador = numero

while contador > 1:
    fatorial *= contador
    contador -= 1

print(f'o resultado da fatorial {numero} é: {fatorial}')
