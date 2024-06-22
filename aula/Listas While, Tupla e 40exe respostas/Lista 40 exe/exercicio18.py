'''Faça um programa para a leitura de duas notas parciais de um aluno. O 
programa deve calcular a média alcançada por aluno e apresentar: 
a. A mensagem "Aprovado", se a média alcançada for maior ou igual 
a sete; 
b. A mensagem "Reprovado", se a média for menor do que sete; 
c. A mensagem "Aprovado com Distinção", se a média for igual a dez.'''

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

if media == 10:
    print("Aprovado com Distinção")
elif 10 > media >= 7:
    print("Aprovado")
elif media < 7:
    print("Reprovado")
else:
    print("limite da nota é 10 ")