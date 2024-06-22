'''
Elaborar um algoritmo que lê 3 valores a,b,c e verifica se eles formam ou 
não um triângulo. Supor que os valores lidos são inteiros e positivos. Caso 
os valores formem um triângulo, calcular e escrever a área deste triângulo. 
Se não formam triângulo escrever os valores lidos. (se a > b + c não formam 
triângulo algum)
'''

a = int(input("Primeiro valor: "))
b = int(input("Segundo valor: "))
c = int(input("Terceiro valor: "))

if a > b + c or b > a + c or c >= a + b:
    print("não formam triângulo algum")
else:
    sp = (a+b+c)/2
    area_triangulo = (sp*(sp - a)*(sp - b)*(sp - c))**0.5
    area_triangulo = round(area_triangulo, 2)
    print(area_triangulo)