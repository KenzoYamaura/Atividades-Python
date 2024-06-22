'''Faça um programa que leia um nome de usuário e a sua senha. 

O programa não deve aceitar a senha igual ao nome do usuário,mostrando uma mensagem de erro caso isso ocorra. 

O programa deve solicitar as informações novamente a cada mensagem de erro.

Depois o programa deve validar a senha, pedindo para o usuário digitar a senha novamente,

se  atingir  12  tentativas,  o  programa  deve  apresentar  a  mensagem  que  o  número  de 
tentativas foi excedido e o mesmo deve ser encerrado o programa.
'''


nome_usuario = input("Digite seu usuário: ")
senha_usuario = input("Digite sua senha: ")
while True:
    if nome_usuario == senha_usuario:
        print("ERRO! Digite Novamente")
    