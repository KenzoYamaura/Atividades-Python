''' Faça um algoritmo que lê dois pontos P1 = (x1, y1) e P2 = (x2, y2) e, calcule 
e  imprima  a  distância  entre  esses  dois  pontos,  cujo  valor  é  dado  pela 
seguinte fórmula:
'''
px1 = float(input("Valor de x1: "))
py1 = float(input("Valor de y1: "))
px2 = float(input("Valor de x2: "))
py2 = float(input("Valor de y2: "))

distância = ((px2 - px1)**2 + (py2 - py1)**2)**0.5

print(f"A distância entre dois pontos é {distância}")
