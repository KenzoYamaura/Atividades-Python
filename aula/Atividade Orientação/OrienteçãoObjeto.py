class Coleira:
    def __init__(self, marca, cor):
        self.marca = marca
        self.cor = cor

    def mostrarMarca(self):
        print(self.marca)

class Cachorro:
    #metodo construtor
    def __init__(self, cor, raca, tamanho, sexo, coleira):
        self.cor = cor
        self.raca = raca
        self.tamanho = tamanho
        self.sexo = sexo
        self.coleira = coleira

    def mostrarCor(self):
        print(self.cor)
    
    def editarCor(self, nova_cor):
        self.cor = nova_cor
    
    def mostrarRaca(self):
        print(self.raca)
    
    def mostrarTamanho(self):
        print(self.tamanho)
    
    def mostrarSexo(self):
        print(self.sexo)


obj_coleira = Coleira("nikedog", "azul")
obj_pinscher = Cachorro("preto", "pinscher", 10, "macho", obj_coleira)
obj_Houndour = Cachorro("preto", "Pokemon", 60, "macho", obj_coleira)

obj_Houndour.mostrarCor()
obj_Houndour.mostrarRaca()
obj_Houndour.coleira.mostrarMarca()

