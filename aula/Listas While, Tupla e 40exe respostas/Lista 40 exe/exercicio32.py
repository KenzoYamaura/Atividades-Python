'''Elabore  um  algoritmo  para  fazer  cálculo  de  potenciação.  Ou  seja,  x^y. 
(Exemplo: 3^4 = 3 x 3 x 3 x 3). Seu algoritmo deverá solicitar que o usuário 
entre com o valor da base (x) e do expoente (y) e apresentar o resultado do 
cálculo  sem  utilizar  os  operadores  (por  exemplo  **).  Para  resolver  o 
problema utilize estrutura de repetição
'''

numero_base = int(input('Insira o número base: '))
expoente = int(input('Insira o expoente: '))

resultado = 1
exp = 0

while exp < expoente:
    resultado *= numero_base
    exp += 1
    print(resultado)

print(f'{numero_base} elevado a {expoente} = {resultado}')
   