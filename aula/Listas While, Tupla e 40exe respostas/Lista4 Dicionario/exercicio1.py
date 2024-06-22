'''
1- Problema: Sistema de Gerenciamento de Estoque:
Você foi contratado para desenvolver um sistema simples de gerenciamento de estoque para 
uma pequena loja. A loja vende diversos produtos e precisa de uma forma de rastrear o 
estoque de cada item, bem como atualizar o estoque conforme os produtos são vendidos ou 
novas remessas chegam.
Requisitos do Sistema:
•Adicionar   Produto:  Adicionar   um   novo   produto   ao   estoque   com   seu   nome   e 
quantidade inicial.
•Atualizar Estoque: Atualizar a quantidade de um produto específico (adicionando ou 
removendo unidades).
•Consultar Estoque: Consultar a quantidade disponível de um produto específico.
•Listar Produtos: Listar todos os produtos e suas quantidades disponíveis.
'''
estoque = []

def menu():
    print("-"*40)
    print("1 - Adicionar produtos")
    print("2 - Atualizar estoque")
    print("3 - Consultar quantidade do estoque")
    print("4 - Listar produtos")
    print("0 - Sair")
    print("-"*40)

def opcao1():
    produtos = {}
    produtos["nome"] = input("Digite o nome do produto: ")
    produtos["quantidade"] = int(input("Digite a quantidade: "))
    estoque.append(produtos)

def opcao2():
    atualizar = input("Deseja Adicionar ou Remover: ")
    if atualizar == "Adicionar":
        n_produto = input("Digite o número do produto: ")
        for i in estoque:
            if i["nome"] == n_produto:
                entrada = int(input("Quantidade para atualizar: "))
                i["quantidade"] += entrada
            else:
                n_produto = input("Digite o número do produto")
                for i in estoque:
                    if i["nome"] == n_produto:
                        saida = int(input("Quantidade de saída: "))
                        i["quantidade"] -= saida
    elif atualizar == "Remover":
        nome_produto = input("Digite o produto que quer remover: ")
        for i, produto in enumerate(estoque): 
            if produto["nome"] == nome_produto:                
                del estoque[i] 
                print(f"O produto {nome_produto} foi deletado com sucesso")
            else:
                print(f"O produto {nome_produto} não encontrado")

def opcao3():
    nome_produto = input("Digite o nome do produto: ")
    for i in estoque:
        if i["nome"] == nome_produto:
            print(f'No estoque tem {i["quantidade"]} de {nome_produto}')

print("Mercadinho")
while True:       
    menu()
    
    opcao = int(input("Escolha umas das opções: "))

    if opcao == 0:
        break

    elif opcao == 1:
        opcao1()

    elif opcao == 2:
        opcao2()

    elif opcao == 3:
        opcao3()
    
    elif opcao == 4:
        for x in estoque:
            print(x)
