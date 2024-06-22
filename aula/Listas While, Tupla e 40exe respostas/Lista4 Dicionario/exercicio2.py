
turmas = {}
usuarios = {"usuario1": "senha1", "usuario2": "senha2"}

def login():
    while True:
        usuario = input("Digite o usuário: ")
        senha = input("Digite a senha: ")
        if usuario in usuarios and usuarios[usuario] == senha:
            print("Login bem sucedido.")
            return True
        else:
            print("Usuário ou senha incorretos. Tente novamente.")

def menu():
    print("\n=== MENU ===")
    print("1. Cadastrar Turma")
    print("2. Cadastrar Aluno")
    print("3. Atualizar Informações de Aluno")
    print("4. Remover Aluno")
    print("5. Visualizar Informações")
    print("0. Sair")

def op1():    
    nome_turma = input("Digite o nome da turma: ")
    if nome_turma in turmas:
        print("Essa turma já está cadastrada.")
    else:
        turmas[nome_turma] = []
        print("Turma cadastrada com sucesso.")

def op2():
    nome_turma = input("Digite o nome da turma: ")
    if nome_turma in turmas:
        nome_aluno = input("Digite o nome do aluno: ")
        notas = input("Digite as notas do aluno separadas por vírgula: ").split(",")
        aluno = {'Nome': nome_aluno, 'Notas': notas}
        turmas[nome_turma].append(aluno)
        print("Aluno cadastrado com sucesso.")
    else:
        print("Turma não encontrada.")

def op3():
    nome_turma = input("Digite o nome da turma: ")
    if nome_turma in turmas:
        nome_aluno = input("Digite o nome do aluno: ")
        for aluno in turmas[nome_turma]:
            if aluno['Nome'] == nome_aluno:
                novo_nome = input("Digite o novo nome do aluno (ou deixe em branco para manter o mesmo): ")
                novas_notas = input("Digite as novas notas do aluno separadas por vírgula (ou deixe em branco para manter as mesmas): ").split(",")
                if novo_nome:
                    aluno['Nome'] = novo_nome
                if novas_notas:
                    aluno['Notas'] = novas_notas
                print("Informações do aluno atualizadas com sucesso.")
                break
        else:
            print("Aluno não encontrado na turma.")
    else:
        print("Turma não encontrada.")

def op4():
    nome_turma = input("Digite o nome da turma: ")
    if nome_turma in turmas:
        nome_aluno = input("Digite o nome do aluno: ")
        for aluno in turmas[nome_turma]:
            if aluno['Nome'] == nome_aluno:
                turmas[nome_turma].remove(aluno)
                print("Aluno removido com sucesso.")
                break
        else:
            print("Aluno não encontrado na turma.")
    else:
        print("Turma não encontrada.")

def op5():
    for nome_turma, alunos in turmas.items():
        print(f"Turma: {nome_turma}")
        for aluno in alunos:
            print(f"Nome: {aluno['Nome']}, Notas: {aluno['Notas']}")

if login():
    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            op1()
        elif opcao == "2":
            op2()
        elif opcao == "3":
            op3()
        elif opcao == "4":
            op4()
        elif opcao == "5":
            op5()

        elif opcao == "0":
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")