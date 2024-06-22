'''
Desenvolver um programa para verificar a nota do aluno em uma prova com 
10  questões,  o  programa  deve  perguntar  ao  aluno  a  resposta  de  cada 
questão e ao final comparar com o gabarito da prova e assim calcular o total 
de acertos e a nota (atribuir 1 ponto por resposta certa). Após cada aluno 
utilizar o sistema deve ser feita uma pergunta se outro aluno vai utilizar o 
sistema. Após todos os alunos terem respondido informar: 
a. Maior e Menor Acerto; 
b. Total de Alunos que utilizaram o sistema; 
c. A Média das Notas da Turma.
Gabarito da Prova: 01 – A, 02 – B, 03 – C, 04 – D, 05 – E, 06 – E, 07 - D 
08 – C, 09 - B e 10 – A
'''
print('-'*10, 'Prova', '-'*10)

gabarito = ["A", "B", "D", "D", "E", "E", "D", "C", "B", "A"]
aluno = 0
prova = []
nota = 0
s_n = ""
lista = []
while s_n != "Não":
    aluno += 1
    prova = [] 
    nota = 0
    for i in range(10):
        prova.append(input("Insira sua resposta: "))    
    for j in range(10):
        if gabarito[j] == prova[j]:
            nota += 1
    s_n = input('Deseja Continuar? (Sim/Não): ')
print('Sua nova é', float(nota))
lista.append(nota)
soma = sum(lista)
print(max(nota), min(nota))
