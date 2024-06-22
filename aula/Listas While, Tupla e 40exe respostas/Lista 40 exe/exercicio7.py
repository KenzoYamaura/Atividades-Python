'''Escreva um algoritmo que leia o peso e a altura de uma pessoa, calcule e 
imprima  o  seu  IMC.  o  IMC  é  dado  pela  seguinte  fórmula:  𝐼𝑀𝐶 =
𝑝𝑒𝑠𝑜/𝑎𝑙𝑡𝑢𝑟𝑎2.'''

peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

imc = peso / altura**2
print(f'O Resultado do IMC = {imc:.2f}')