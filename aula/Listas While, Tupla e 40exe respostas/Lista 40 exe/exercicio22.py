''' Construa  um  programa  que  receba  um  número  e  verifique  se  ele  é  um 
número triangular. (Um número é triangular quando é resultado do produto 
de três números consecutivos. Exemplo: 24 = 2 x 3 x 4)'''


numero = int(input('Digite um número: '))

x = 0
y = 1
z = 2
produto = x*y*z

controle = True

while produto <= numero and controle:
    if produto == numero:
        controle = False
    else:
        x += 1
        y += 1
        z += 1
        produto = x*y*z

if (not controle):
    print('é um triângulo')
else:
    print('Não é um triângulo')