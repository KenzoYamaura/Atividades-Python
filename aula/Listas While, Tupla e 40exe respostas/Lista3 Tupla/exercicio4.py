'''Escreva um programa que recebe uma tupla de números inteiros e imprime a soma de todos os 
números pares da tupla.'''

tupla = (2, 3, 8, 9, 7, 9, 40, 62, 100)

s = 0
for i in tupla:
    if i % 2 == 0:
        s += i
        print(s)

