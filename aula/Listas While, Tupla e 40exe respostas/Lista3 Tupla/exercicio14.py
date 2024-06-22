'''Suponha que você tenha duas matrizes A e B, ambas com tamanho 3x3. Faça um 
programa que calcule a soma das duas matrizes. (SEM USAR FUNÇÃO)
soma = [[101, 21, 10],
        [10, 50, 71],
        [10, 105, 19]]'''

a = [[1, 13, 3],
     [4, 45, 67],
     [7, 80, 9]]

b = [[100, 8, 7],
     [6, 5, 4],
     [3, 25, 10]]

cc = []

for i in range(len(a)):
    f_matriz = []
    for j in range(len(b)):
        c = a[i][j] + b[i][j]
        f_matriz.append(c)
    cc.append(f_matriz)

for x in cc:
    print(x)

        
