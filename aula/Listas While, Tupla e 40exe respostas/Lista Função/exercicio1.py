'''crie uma função que necessite de três parâmetros, e que imprima o produto desses três argumentos'''

'''def mult(a,b,c):
    return a*b*c

a, b, c = map(int,input().split())

print(mult(a,b,c))'''

'''Crie uma função que solicite uma expressão de soma como parâmetro, e que imrima o resultado da soma. Valores de 1 a 9'''

def calcular_soma(a):
    lis = a.split("+")
    s = 0
    for i in lis:
        s += int(i)
    print(s)