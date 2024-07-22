class Pessoa:
    def __init__(self, nome, idade, endereco):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco

    def mostrarPessoa(self):
        print(f"Meu nova é {self.nome} idade {self.idade} e moro na {self.endereco}")

    def alterarIdade(self, novaIdade):
        self.idade = novaIdade

pessoa1 = Pessoa("Kenzo", 30, "Vila Carvalho")

pessoa1.mostrarPessoa()
pessoa1.alterarIdade(input("Digite a nova idade: "))
pessoa1.mostrarPessoa()
