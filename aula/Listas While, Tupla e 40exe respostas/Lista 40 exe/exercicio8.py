'''Faça  um  algoritmo que  leia  o  preço  de  custo  de um  produto,  calcule  e 
imprima o preço final do mesmo, sabendo que: 
a. o preço final é calculado através da soma do preço de custo, o valor 
dos impostos e o lucro esperado; 
b. o valor dos impostos é de 45% do valor do preço de custo; 
c. o lucro esperado é de 50% do valor do preço de custo.
'''

preço = float(input("O preço de custo: "))

print("Valor final: ", preço + (preço * 0.5) + (preço * 0.45))