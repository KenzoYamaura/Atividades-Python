'''
Faça um algoritmo para ler três notas de um aluno em uma disciplina e 
imprimir a sua média ponderada (as notas têm pesos respectivos de 1, 2 e 
3).
'''

nota_1, nota_2, nota_3 = map(float, input('Digite as suas notas: ').split())

media = ((nota_1*1)+(nota_2*2)+(nota_3*3))/6

print(f"Sua média é: {media:.2f}")
