'''Considere uma lista de tuplas em que cada tupla representa informações sobre um 
aluno, contendo o nome e a nota de uma disciplina. Escreva um programa que recebe 
essa lista e imprime o nome do aluno que obteve a maior nota.
'''

alunos = [("João", 8.0), ("Maria", 9.5), ("Pedro", 7.5), ("Ana", 8.5)]

maior_nota = float()
aluno_maior_nota = ''

for aluno, nota in alunos:
    if nota > maior_nota:
        maior_nota = nota
        aluno_maior_nota = aluno

print(aluno_maior_nota)

       