'''Classe Triangulo: Crie uma classe que modele um triangulo: ​
	– Atributos: LadoA, LadoB, LadoC​
	– Métodos: calcular Perímetro, getMaiorLado; ​
Crie instâncias desta classe. Ele deve pedir ao usuário que informe as medidas de um triangulo. Depois, deve criar um objeto com as medidas e imprimir sua área e maior lado.​'''

class Triangulo:
    def __init__(self, ladoA, ladoB, ladoC):
        self.ladoA = ladoA
        self.ladoB = ladoB
        self.ladoC = ladoC
    
    def Perimetro(self):
        perimetro = self.ladoA + self.ladoB + self.ladoC
        print(f"O Perimetro = {perimetro}")
    
    def getMaiorLado(self):
        maiorLado = max(self.ladoA, self.ladoB, self.ladoC)
        print(f"O maior lado é {maiorLado}")

triA = float(input("Lado A: "))
triB = float(input("Lado B: "))
triC = float(input("Lado C: "))
triangulo = Triangulo(triA, triB, triC)

triangulo.Perimetro()
triangulo.getMaiorLado()
