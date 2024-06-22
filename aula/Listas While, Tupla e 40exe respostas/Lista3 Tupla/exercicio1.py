'''Escreva um programa que recebe uma tupla de números inteiros e verifica se algum deles é 
igual a 0. Se houver, o programa deve imprimir "Zero encontrado!" e encerrar a execução. 
Caso contrário, o programa deve imprimir "Nenhum zero encontrado." 
'''
tupla = (1, 2, 3, 4, 0, 5, 6)

for i in tupla:
    if i == 0:
        print("Zero encontrado!")
    else:
        print('Nenhum zero encontrado.')