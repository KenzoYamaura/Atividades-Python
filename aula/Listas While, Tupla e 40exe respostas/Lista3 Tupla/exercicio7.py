'''Faça um algoritmo que efetue a soma dos valores de uma matriz 3x3 e exiba o 
resultado da soma. R=45
'''

matriz = [[1, 2, 3], 
          [4, 5, 6], 
          [7, 8, 9]]

s = 0
for i in matriz:
    for j in i:
        s += j
print(s)