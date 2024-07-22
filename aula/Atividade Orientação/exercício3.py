class Livro:
    def __init__(self, nome, autor, editora, paginas):
        self.nome = nome
        self.autor = autor
        self.editora = editora
        self.paginas = paginas
    
    def mostrarDetalhes(self):
        print(f"O livro {self.nome} \nautor {self.autor} \neditora {self.editora}")
    
    def alterarEditora(self, novaEditora):
        self.editora = novaEditora
        self.mostrarDetalhes()
    
    def listarQuantidadePag(self):
        print(f"o Livro {self.nome} tem {self.paginas} páginas")

livro1 = Livro("O Sangue dos Elfos - The Witcher", "Andrzej Sapkowski", "WMF Martins", 300)
livro2 = Livro("O último desejo - The Witcher", "Andrzej Sapkowski", "WMF Martins", 220)
livro3 = Livro("A espada do destino - The Witcher", "Andrzej Sapkowski", "WMF Martins", 430)
livro4 = Livro("Tempo do Desprezo - The Witcher", "Andrzej Sapkowski", "WMF Martins", 330)

livro1.mostrarDetalhes()
print("-"*30)
livro2.mostrarDetalhes()
print("-"*30)
livro3.mostrarDetalhes()
print("-"*30)
livro4.mostrarDetalhes()
print("-"*30)
livro1.listarQuantidadePag()
livro1.alterarEditora(input("Outra editora: "))