'''
Faça um programa que calcule e imprima o gasto de uma viagem de carro 
de uma cidade a outra, sabendo que: 
a. o carro utilizado roda 15 Km com 1 litro de gasolina; 
b. o preço médio da gasolina é de R$5,30; 
c. o valor de cada pedágio é de R$8,00. 
 
Seu algoritmo precisa ler a distância entre as cidades e a quantidade de 
pedágios entre as cidades.
'''

distância = int(input("Digite a distância da viagem em KM: "))
pedágio = int(input("Digite a quantidade de pegágios: "))

print(round(5.30 * (distância / 15 + pedágio * 8), 2))