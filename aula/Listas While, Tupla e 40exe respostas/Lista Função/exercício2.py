'''Crie uma função que imprima a quantidade de dígitos de um determinado número inteiro informado.'''

def digitos(numero):
    cont = 0

    if numero == 0:
        return 1
    
    if numero < 0:
        numero = - numero
    
    while numero > 0:
        numero = numero//10
        cont += 1
    
    return cont

n = int(input("Digite um número inteiro: "))
quantidade = digitos(n)
print(quantidade)
