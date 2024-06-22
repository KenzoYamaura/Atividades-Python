'''
Escreva um programa que solicite um número inteiro positivo ao usuário e 
calcule a soma de seus dígitos
'''

numero = float(input('Digite um número: '))

if numero > 0:
    if numero == int(numero):
        soma = 0        
        while numero:
            digito = numero % 10
            soma += digito
            numero //= 10
        print(f'A soma é {int(soma)}')
    else:
        print('Não é um inteiro')
    
elif numero < 0:
    if numero == int(numero):
        print('É um número negativo')
    else:
        print('é um número inteiro e negativo') 





    
    
    
    
