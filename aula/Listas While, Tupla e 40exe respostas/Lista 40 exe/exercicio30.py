'''Escrever um algoritmo que leia uma quantidade desconhecida de números 
e conte quantos deles estão nos seguintes intervalos: [0-25], [26-50], [51-
75] e [76-100]. A entrada de dados deve terminar quando for lido um número 
negativo.'''

entre_0_e_25 = 0
entre_26_e_50 = 0
entre_51_e_75 = 0
entre_76_e_100 = 0

numero = int(input('Insira um número: '))
contador = numero

while contador > 0:    
    contador = int(input('Insira um número: '))    
    if 0 <= contador <= 25:
        entre_0_e_25 += 1
    elif 26 <= contador <= 50:
        entre_26_e_50 += 1
    elif 51 <= contador <= 75:
        entre_51_e_75 += 1
    elif 76 <= contador <= 100:
        entre_76_e_100 += 1
        
print(f'Quantidade de número entre 0 e 25: {entre_0_e_25}')
print(f'Quantidade de número entre 26 a 50: {entre_26_e_50}')
print(f'Quantidade de número entre 51 a 75: {entre_51_e_75}')
print(f'Quantidade de número entre 76 a 100: {entre_76_e_100}')