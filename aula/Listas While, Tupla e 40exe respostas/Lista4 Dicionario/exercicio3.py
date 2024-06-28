'''Escreva um programa, com uma função que necessite de um argumento. A função retornar o valor "P",
se seu argumento for positivo. e "N". se seu argumento for zero ou negativo'''


def positivo(n):
    if n > 0:
        return "P"
    elif n <= 0:
        return "N"

res = positivo(int(input("Digite um número: ")))
print(res)