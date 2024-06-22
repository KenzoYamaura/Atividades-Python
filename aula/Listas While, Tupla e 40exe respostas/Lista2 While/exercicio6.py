'''Faça um programa que solicite ao usuário um número inteiro positivo e some os 
números digitados. Ao digitar um número negativo, o programa deve informar que o 
número é inválido e solicitar outro valor, se o valor digitado for o número neutro, ou 
seja, zero, o programa deve finalizar e mostrar o resultado da soma.
'''

soma = 0
while True:
    numero = input('Digite um número: ')
    if int(numero) == 0:
        print(soma)
        break
    elif int(numero) > 0:
        while numero != "":
            soma = soma + int(numero[0])
            numero = numero[1:]
    else:
        print("Número inválido!")
