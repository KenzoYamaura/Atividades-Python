'''Faça um algoritmo que calcule a matriz transposta de M, ou seja, o que é linha vira 
coluna. Ao final exiba a transposta.''' 

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

transposta = []
for i in range(len(matriz)):
    transposta_row = []
    for j in matriz:
        transposta_row.append(j[i])
    transposta.append(transposta_row)

print("Matriz Original:")
for row in matriz:
    print(row)

print("\nMatriz Transposta:")
for row in transposta:
    print(row)
