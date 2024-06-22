'''Em uma eleição presidencial existem quatro candidatos. Os votos são informados através de códigos. Os 
dados utilizados para a contagem dos votos obedecem à seguinte codificação: 
1,2,3,4 = voto para os respectivos candidatos; 
5 = voto nulo; 
6 = voto em branco; 
Elabore um programa que leia o código votado por vários eleitores. Como finalizador da entrada de dados, 
considere o código zero. 
Ao final, calcule e escreva: 
total de votos para cada candidato; 
total de votos nulos; 
total de votos em branco;'''

print('Candidato 1 - 1')
print('Candidato 2 - 2')
print('Candidato 3 - 3')
print('Candidato 4 - 4')
print('Voto Nulo - 5')
print('Em Branco - 6')
print('Sair do sistema - 0')
c1 = 0
c2 = 0
c3 = 0
c4 = 0
vn = 0
vb = 0
while True:
    candidato = input('Escolha um candidato: ')                         
    if candidato == '1':
        c1 += 1
    elif candidato == '2':
        c2 += 1
    elif candidato == '3':
        c3 += 1
    elif candidato == '4':
        c4 += 1
    elif candidato == '5':
        vn += 1
    elif candidato == '6':
        vb += 1
    elif candidato == '0':
        break
print(f'Votos para o Candidato 1: {c1}')
print(f'Votos para o Candidato 2: {c2}')
print(f'Votos para o Candidato 3: {c3}')
print(f'Votos para o Candidato 4: {c4}')
print(f'Votos Nulos: {vn}')
print(f'Votos em Branco: {vb}')   