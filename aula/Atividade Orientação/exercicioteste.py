class Usuario:
    def __init__(self, login, senha):
        self.login = login
        self.senha = senha
    
    def visualizar_vendas(self) -> None: pass

class Vendedor(Usuario):
    def __init__(self, login, senha, RGV):
        super().__init__(login, senha)
        self.rgv = RGV
    
    def Vender(self, cliente1, produto1):
        venda1 = Vendas(self, cliente1, produto1)
        return venda1
    
class Cliente(Usuario):
    def __init__(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco
        
class Gerente(Usuario):
    def __init__(self, login, senha):
        super().__init__(login, senha)
    
    def Visualizar_Vendar(self):
        pass

class Vendas:
    def __init__(self, vendedor, cliente, produto):
        self.vendedor = vendedor
        self.cliente = cliente
        self.produto = produto
    
    def mostrar_Dados_Venda(self):
        print(self.vendedor.login)
        print(self.cliente.nome)
        print(self.produto.nome)
        print(self.produto.preco)
    
class Produto:
    def __init__(self, nome, preco, descricao):
        self.nome = nome
        self.preco = preco
        self.descricao = descricao

    
venderdor1 = Vendedor("Um cara", "123", 1)
cliente1 = Cliente("Joo", "Rua tal")
produto1 = Produto("Caneta", 1.5, "bic")

vend = venderdor1.Vender(cliente1, produto1)
vend.mostrar_Dados_Venda()