''' Faça um programa capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. O 
usuário deve informar de qual número ele deseja ver a tabuada. A saída deve ser conforme o 
exemplo abaixo, tabuada do 5:
5 X 1 = 5
5 X 2 = 10
 ...
5 X 10 = 50
'''
numero = int(input("Insira um número: "))
multiplicador = 0

if 0 <= numero <= 10:
    while multiplicador < 10:   
        tabuada = numero * multiplicador    
        print(f'{numero} X {multiplicador} = {tabuada}')
        multiplicador += 1 
else:
    print('Não é entre 0 e 10')