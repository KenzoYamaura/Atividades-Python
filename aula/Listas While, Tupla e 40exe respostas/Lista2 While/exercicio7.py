'''Faça um programa que leia 4 notas de um aluno e armazene em uma lista (usando while). 
Se o usuário digitar -1, a leitura de notas será interrompida e calculará a média. Para cada 
nota digitada, deve-se verificar se está entre o intervalo de 0 a 10, caso não esteja, deve 
informar que a nota é inválida e realizar a leitura novamente. Ao final, o programa deve 
mostrar a média obtida e se nenhuma nota foi informada, então deve mostrar ao usuário 
uma mensagem falando que nenhuma nota foi informada.
'''


notas = []

while True:
    nota = float(input('Digite a nota (ou digite -1 para parar): '))
    if nota == -1:
        break
    notas.append(nota)

if notas:
    media = sum(notas) / len(notas)
    print("A média das notas é:", media)
else:
    print("Nenhuma nota foi digitada.")



    