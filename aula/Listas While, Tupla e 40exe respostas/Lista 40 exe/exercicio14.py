''' Deseja-se  fazer  um  levantamento  a  respeito  da  ausência  de  alunos  na 
primeira prova de programação de computadores, para cada uma das 14 
turmas existentes. Para cada turma é fornecido um conjunto de valores, 
sendo  que  os  dois  primeiros  valores  do  conjunto  correspondem  à 
identificação da turma (A, B, C ...) e ao número de alunos matriculados. Os 
demais valores deste conjunto correspondem ao número da matrícula do 
aluno e a letra A ou P para o caso de o aluno estar ausente ou presente, 
respectivamente. Faça um algoritmo que:  
a. Calcule a porcentagem de ausência e escreva a identificação da 
turma com a respectiva porcentagem. '''


lista_turma = []

n = int(input("Quantidade de turmas: "))

for i in range(n):
    turma = input("Qual a Letra da turma? ")
    matricula = int(input('Quantos alunos tem mastriculados: '))
    presenca = int(input('Quantos alunos estavam na aula: '))

    if matricula > 0:
        alunos = (presenca/matricula) * 100
    else: 
        alunos = 0
    
    lista_turma.append(f'A Turma {turma} tem {matricula}, tiveram {presenca} presentas na aula.')


print(lista_turma)