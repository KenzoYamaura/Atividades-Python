'''Neste exercício, você irá simular um sistema simples de gestão de uma
biblioteca utilizando listas em Python. O sistema permitirá adicionar livros à 
biblioteca,  emprestar  livros  para  usuários  e  registrar  a  devolução  dos 
mesmos.  Além  disso,  será  possível  listar  os  livros  disponíveis  para 
empréstimo. 
O exercício consiste nas seguintes funcionalidades: 
a. Adicionar Livros: Os livros serão representados por listas contendo 
informações como título, autor e disponibilidade para empréstimo. 
Eles serão adicionados a uma lista que representa a coleção da 
biblioteca. 
b. Listar  Livros  Disponíveis:  Uma  função  será  responsável  por 
percorrer  a  lista  de  livros  e  exibir  apenas  aqueles  que  estão 
disponíveis para empréstimo. 
c. Emprestar  Livro:  Outra  função  permitirá  emprestar  um  livro 
específico  para  um  usuário.  Será  verificado  se  o  livro  está 
disponível antes de concluir a operação. 
d. Devolver  Livro:  Uma  função  será  utilizada  para  registrar  a 
devolução de um livro previamente emprestado. Será verificado se 
o livro está emprestado antes de marcar sua devolução. 
e. Este exercício visa praticar conceitos de manipulação de listas em 
Python, bem como o uso de estruturas de controle e condicionais 
para implementar as funcionalidades de um sistema simples de 
biblioteca. Para sair do sistema, o usuário deve digitar -1.'''


livros = ["0 - Livro A", "1 - Livro B", "2 - Livro C", "3 - Livro D"]
emprestimo = []
emp = 0
cont1 = 0
print("SELECIONE UMAS DAS OPÇÕES: ")
print("1 - Adicionar Livros: ")
print("2 - Listar Livros: ")
print("3 - Emprestar Livros: ")
print("4 - Devolver Livro: ")
print("-1 - Sair: ")

opcao = ''

while opcao != "-1":
    opcao = input('Digite umas das opções: ')

    if opcao == "1":
        livros.append(input('Digite o livro: '))

    elif opcao == "2":
        for i in livros:
            print(f"Livros Disponíveis: {i}")
            cont1 += 1
        
    elif opcao == "3":
        print(livros)
        livro_emp = int(input('Deseja emprestar qual dos Livros?: '))
        if 0 <= livro_emp <= len(livros):              
            emp = livros.pop(livro_emp)
            emprestimo.append(emp)
            print(f"O livro '{livro_emp}' foi emprestado com sucesso!")
        else:
            print("Indice Inválido")

    elif opcao == "4":  
        print(emprestimo)
        livro_devolver = int(input('Deseja emprestar qual dos Livros?: '))
        if 0 <= livro_devolver <= len(emprestimo):
            emp = emprestimo.pop(livro_devolver)
            emprestimo.append(emp)
            print(f"O livro '{livro_devolver}' foi devolvido com sucesso!")
        else:
            print("Indice Inválido")

    else:
        print("Saindo do Sistema")
        



