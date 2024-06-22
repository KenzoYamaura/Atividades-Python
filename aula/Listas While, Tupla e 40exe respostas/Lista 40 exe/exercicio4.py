'''Um motorista deseja colocar no seu tanque X reais de gasolina. Escreva um 
algoritmo para ler o preço do litro da gasolina e o valor do pagamento, e 
exibir quantos litros ele conseguiu colocar no tanque
'''

gasolina = float(input("Quantos reais colocou: "))
valor = float(input("Quantos o preço da gasolina por por litro: "))

custo = (gasolina/valor)
print(custo)

