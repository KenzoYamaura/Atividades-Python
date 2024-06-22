'''Escreva um programa que recebe uma tupla de números inteiros e imprime apenas os 
números pares.
'''

tupla = []

for i in range(1, 101):
    if i % 2 == 0:
        tupla.append(i)
print(tuple(tupla))