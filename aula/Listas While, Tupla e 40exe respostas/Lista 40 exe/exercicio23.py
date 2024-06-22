'''
Faça um Programa que leia 2 números e em seguida pergunte ao usuário 
qual  operação  ele  deseja  realizar.  O  resultado  da  operação  deve  ser 
acompanhado de uma frase que diga se o número é: 
a. par ou ímpar; 
b. positivo ou negativo; 
c. inteiro ou decimal.
'''

n1 = int(input("Insira um número: "))
n2 = int(input("Insira outro número: "))
operacao = input("Que operação deseja realizar: 1º - Soma , 2º - Subtração , 3º - Multiplicação , 4º - Divisão:  ")

if operacao == "1":
    resultado = n1 + n2
elif operacao == "2":
    resultado = n1 - n2
elif operacao == "3":
    resultado = n1 * n2
elif operacao == "4":
    resultado = n1 / n2
else:
    print("Operação Inválida")
    
print(f'O resultado é {resultado}')

if resultado % 2 == 0:
    print("O resultado é Par ")
else:
    print("O resultado é Impar")

if resultado > 0:
    print("O resultado é Positivo")
elif resultado < 0:
    print("O resultado é negativo")
else:
    print("O resultado é neutro")

if resultado == int(resultado):
    print("O resultado é inteiro ")
else:
    print("O resultado é decimal ") 






