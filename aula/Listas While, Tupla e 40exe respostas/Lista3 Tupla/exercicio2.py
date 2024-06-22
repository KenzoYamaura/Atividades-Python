'''Escreva um programa que recebe uma tupla de números inteiros e imprime o maior número 
da tupla. (SEM USAR FUNÇÃO)
tupla = (3, 6, 2, 9, 1, 7, 5)
'''

tupla = (3, 6, 2, 9, 1, 7, 5)

m = 0

for i in tupla:
    if i > m:
        m = i
print(m)

