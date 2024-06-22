'''Declare uma matriz 5 x 5. Preencha com 1 a diagonal principal e com 0 os demais 
elementos. Escreva ao final a matriz obtida. Saída:
[1, 0, 0, 0, 0]
[0, 1, 0, 0, 0]
[0, 0, 1, 0, 0]
[0, 0, 0, 1, 0]
[0, 0, 0, 0, 1]'''

matriz = [[1, 2, 3, 4, 5],
          [6, 7, 8, 9, 10],
          [11, 12, 13, 14, 15],
          [16, 17, 18, 19, 20],
          [21, 22, 23, 24, 25]]

a = []

for i in range(len(matriz)):
    f_matriz = []
    for j in range(len(matriz[i])):
        if j == i:
            f_matriz.append(1)
        else:
            f_matriz.append(0)
    a.append(f_matriz)

for x in a:
    print(x)