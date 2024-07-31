class Usuario:
    def __init__(self, login, senha):
        self.login = login
        self.senha = senha
    
    def visualizar_vendas(self) -> None: pass

class Vendedor(Usuario):
    def __init__(self, login, senha, rgv):
        super().__init__(login, senha)
        self.rgv = rgv
    
    def Vender(self, nome_cliente, nome_prod):
        venda1 = Vendas(self, cliente = Cliente(nome_cliente), produto = Produto(nome_prod))

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
    
class Produto:
    def __init__(self, nome, preco, descricao):
        self.nome = nome
        self.preco = preco
        self.descricao = descricao