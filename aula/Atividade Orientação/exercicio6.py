'''5 - Classe Círculo: crie uma classe que represente um círculo. Esta classe deve possuir o seguinte atributo:​

raio​

A classe deve ter os seguintes métodos:​
imprimir o valor do raio;​
calcular a área do círculo;​
calcular a circunferência do círculo.​'''

class Circulo:
    def __init__(self, raio):
        self.raio = raio
    
    def ImprimirValorRaio(self):
        print(f"O raio é {self.raio}")

    def AreaCirculo(self):
        a =  3.14 * self.raio**2
        print(f"O valor da Área = {a}")
    
    def CircunferenciaCirculo(self):
        c = 2*(3.14)*(self.raio)
        print(f"O valor da Circunferência = {c:.2f}")
    
circulo = Circulo(5)
circulo.ImprimirValorRaio()
circulo.AreaCirculo()
circulo.CircunferenciaCirculo()
