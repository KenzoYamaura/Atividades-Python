'''Faça um programa que leia uma matriz 3x3, como a do exemplo abaixo, e em seguida, 
mostrar a posição onde se encontram o maior e o menor valor. (SEM USAR FUNÇÃO)
'''

matriz = [[1, 120, -3], [4, 5, 250], [7, 0, 9]]

l = []
maior = 0
menor = 0
l_menor = 0
l_maior = 0
c_menor = 0
c_maior = 0
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if matriz[i][j] > maior:
            maior = matriz[i][j]
            l_maior = i
            c_maior = j
        if matriz[i][j] < menor:
            menor = matriz[i][j]
            l_menor = i
            c_menor = j

print(f'O Maior termo é {maior}, posição {l_maior} {c_maior}')
print(f'O Menor termo é {menor}, posição {l_menor} {c_menor}')


