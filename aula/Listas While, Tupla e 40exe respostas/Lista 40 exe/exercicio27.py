'''Leia um número inteiro maior que 1 e escreva se ele é primo ou não. Um 
número é primo se ele é divisível apenas por 1 e por ele mesmo'''

n = int(input("Digite um número: "))
i = 2
primo = True

while i < n:
    if n % i == 0:
        primo = False
        print(n, i)
    i += 1
if primo:
    print('É primo')
else:
    print('Não é Primo')
    