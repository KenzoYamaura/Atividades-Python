'''
1- Problema: Sistema de Gerenciamento de Estoque:
Você foi contratado para desenvolver um sistema simples de gerenciamento de estoque para 
uma pequena loja. A loja vende diversos produtos e precisa de uma forma de rastrear o 
estoque de cada item, bem como atualizar o estoque conforme os produtos são vendidos ou 
novas remessas chegam.
'''

class Produto:
    def __init__(self, nome, quantidade):
        self.nome = nome  
        self.quantidade = quantidade

class Estoque:
    def __init__(self):
        self.estoque = []
    
    def AdicionarEstoque(self, produto):
        self.estoque.append(produto)
    
    def AdicionarProduto(self):
        nome = input("Nome do Produto: ")
        quantidade = int(input("Quantidade do Produto: "))
        produto = Produto(nome, quantidade)
        estoque1.AdicionarEstoque(produto)
        print(f"Produto '{nome}' adicionado com sucesso.")
            
    def AdicionarEstoque(self):        
        nomeProd = input("Qual produto deseja alterar?: ")
        for prod in self.estoque:
            if prod.nome == nomeProd:
                qtd = int(input("Qual quantidade deseja alterar? "))
                prod.quantidade += qtd
                print(f"A quantidade do produto {prod.nome} foi atualizado para {prod.quantidade} Unidades")
                return
        print(f"O Produto {nomeProd} não encontrado!")
    
    def RemoverEstoque(self):
        nomeProd = input("Qual produto deseja remover?: ")
        for prod in self.estoque:
            if prod.nome == nomeProd:
                qtdRemover = int(input("Qual quantidade deseja remover?: "))
                prod.quantidade -= qtdRemover
                print(f"A quantidade do produto {prod.nome} foi atualizado para {prod.quantidade} Unidades")
                return
        print("Opção inválida")

    def ConsultarEstoque(self):
        consultarProd = input("Qual produto deseja consutar? ")
        for produto in self.estoque:
            if produto.nome == consultarProd:
                print(f"O produto {produto.nome} tem {produto.quantidade}")
                return
        print(f"Opção Inválida")
    
    def ListarProduto(self):
        for produto in self.estoque:
            print(f"O Produto {produto.nome} tem {produto.quantidade} Unidades")
                   
estoque1 = Estoque()

while True:
    print("-"*40)
    print("Mercadin")
    print("1 - Adicionar Produto ")
    print("2 - Adicionar Estoque ")
    print("3 - Remover Estoque ")
    print("4 - Consultar Produto ")
    print("5 - Listar Produto ")
    print("0 - Sair")
    print("-"*40)
    opcao = input("Digite uma das opções: ")

    if opcao == "1":
        estoque1.AdicionarProduto()
    
    elif opcao == "2":
        estoque1.AdicionarEstoque()
    
    elif opcao == "3":
        estoque1.RemoverEstoque()

    elif opcao == "4":
        estoque1.ConsultarEstoque()
    
    elif opcao == "5":
        estoque1.ListarProduto()
    
    elif opcao == "0":
        break