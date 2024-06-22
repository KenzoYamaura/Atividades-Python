'''Escreva um programa que leia 3 valores e escreva a soma dos 2 maiores.'''

n1 = int(input("Insira um valor x: "))
n2 = int(input("Insira um valor y: "))
n3 = int(input("Insira um valor z: "))


if n1 > n2 > n3 or n2 > n1 > n3:
    print(f'A soma do 2 maiores numeros é {n1+n2}')
elif n3 > n2 > n1 or n1 > n3 > n2:
    print(f'A soma do 2 maiores numeros é {n3+n2}')
else:
    print(f'A soma do 2 maiores numeros é {n1+n3}')


