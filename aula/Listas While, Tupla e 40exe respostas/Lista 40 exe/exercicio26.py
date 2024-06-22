'''
Refaça o exercício anterior, acrescentando o recurso de mostrar que tipo 
de triângulo será formado: 
a. EQUILÁTERO: todos os lados iguais 
b. ISÓSCELES: dois lados iguais 
c. ESCALENO: todos os lados diferentes  
'''

a, b, c = map(float, input('Digete os seguimentos de reta.').split())
print(a,b,c)

if a < b + c or b < a + c or c < a + b:   
    if a == b == c:
        print("É um triângulo Equilátero")
    elif a != b == c or b != a == c or c != a == b:
        print("É um triângulo Isósceles")
    else:
        print("É um triângulo Escaleno")
else:
    print("Não forma um triangulo")