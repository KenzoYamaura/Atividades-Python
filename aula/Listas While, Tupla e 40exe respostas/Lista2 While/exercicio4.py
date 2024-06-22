''' Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm' ou 'o';
Estado Civil: 's', 'c', 'v', 'd';
'''

nome = input('Insira seu Nome: ')
while len(nome) < 3:
    print('Nome Inválido')
    nome = input('Insira seu Nome: ')

idade = int(input('Insira sua Idade: '))
while idade <= 0 or idade >= 150:
    print('Idade Inválida')
    idade = input('Insira sua Idade: ')

salario = float(input('Insira seu salário: R$'))
while salario < 0:
    print('Salário inválido')
    salario = float(input('Insira seu salário: R$'))

sexo = input('Insira seu Sexo: ')
while sexo != 'F' and sexo != 'M' and sexo != 'Outro':
    print('Sexo Inválido')
    sexo = input('Insira seu Sexo: ')

e_civil = input('Insira seu Estado Civil: ')
while e_civil != 'S' and e_civil != 'C' and e_civil != 'D' and e_civil != 'V':
    print('Estado Civil Inválido')
    e_civil = input('Insira seu Estado Civil: ')