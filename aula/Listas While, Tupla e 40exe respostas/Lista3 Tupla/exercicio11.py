'''Dada uma matriz 4 x 4, imprima a matriz e retorne a localização 
(linha e a coluna) do maior valor. (SEM USAR FUNÇÃO)
'''

matriz = [[1, 2, 11, 13], 
          [4, 15, 16, 60], 
          [7, 8, 19, 200], 
          [20, 100, 5, 3]]

maior = 0
linha = 0
coluna = 0

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if matriz[i][j] > maior:
            maior = matriz[i][j]
            linha = i
            coluna = j

print(f"o maior termo {maior} na posição '''[{linha}][{coluna}]'''")