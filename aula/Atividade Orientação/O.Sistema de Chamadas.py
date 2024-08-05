'''Objetivo: Desenvolver um sistema de chamados utilizando Python, onde usuários podem relatar problemas e acompanhar o status de seus chamados, enquanto administradores (ADMs) têm a capacidade de visualizar e concluir os chamados. 

Funcionalidades do Sistema 

Login do Usuário: 

O sistema deve permitir que o usuário faça login com um nome de usuário e senha. 
Após o login, o usuário pode acessar suas funcionalidades. 

Cadastro de Chamado: 

O usuário pode informar um problema, selecionando o tipo do problema (por exemplo, "Técnico", "Administrativo", "Financeiro", etc.).
O sistema deve permitir ao usuário descrever o problema detalhadamente. 

Monitoramento de Chamados: 

O usuário pode visualizar o status dos chamados abertos (por exemplo, "Aberto", "Em Andamento", "Concluído"). 
O usuário pode consultar o histórico de todos os chamados que ele criou, visualizando as informações do problema e seu status atual.
Acesso Administrativo: 

O administrador (ADM) pode fazer login e visualizar todos os chamados registrados no sistema. 
O ADM pode alterar o status de um chamado para "Em Andamento" ou "Concluído", conforme o progresso da resolução do problema. 

'''

class Usuario:
    def __init__(self, login, senha, admin = False):
        self.login = login
        self.senha = senha
        self.admin = admin

    def autenticar(self, login, senha):
        return self.login == login and self.senha == senha

class Chamados:
    cont_chamados = 0

    def __init__(self, usuario, tipo_problema, descricao):
        Chamados.cont_chamados += 1
        self.id = Chamados.cont_chamados
        self.usuario = usuario
        self.tipo_problema = tipo_problema
        self.descricao = descricao
        self.status = "Aberto"
    
    def __str__(self):
        return (f"Id: {self.id}, \nTipo do problema {self.tipo_problema}, \nDescrição: {self.descricao} \nStatus do Chamado: {self.status}")

class SistemaChamados:
    def __init__(self):
        self.usuarios = []
        self.chamados = []
        self.usuario_atual = None
        self.criarUsuarios()
        
    def criarUsuarios(self):
        self.usuarios.append(Usuario("admin", "admin", True))
        self.usuarios.append(Usuario("user1", "123"))
    
    def login(self):
        login = input("Login: ")
        senha = input("Senha: ")
        for usuario in self.usuarios:
            if usuario.autenticar(login, senha):
                self.usuario_atual = usuario
                print(f"Bem-Vindo, {usuario.login}")
                return True
        print("Login Incorreto")
        return False
    
    def criarChamado(self):
        categoria = input("Qual o tipo do problema? (Técnico / Administrativo / Financeiro): ")
        descricao = input("Descreva o problema: ")
        novo_chamado = Chamados(self.usuario_atual, categoria, descricao)
        self.chamados.append(novo_chamado)
        print("Seu Chamado foi criado com sucesso")
    
    def visualizarChamados(self):
        if self.usuario_atual.admin:
            for chamado in self.chamados:
                print("-" * 40)
                print(f"ID: {chamado.id} \nTipo de Problema: {chamado.tipo_problema} \nDescrição: {chamado.descricao} \nStatus do Chamado: {chamado.status}")
                print("-" * 40)
        else:
            for chamado in self.chamados:
                if chamado.usuario == self.usuario_atual:
                    print("-" * 40)
                    print(f"ID: {chamado.id} Tipo de Problema: {chamado.tipo_problema} \nDescrição: {chamado.descricao} \nStatus do Chamado: {chamado.status}")
                    print("-" * 40)
    
    def atualizarChamados(self):
        if not self.usuario_atual.admin:
            print("Acesso Negado")
            return
        id_chamado = int(input("Digite o número do ID do chamado: "))
        for chamado in self.chamados:
            if chamado.id == id_chamado:
                novo_status = input("Digite o Atual Status do problema: ('Em Aberto' / 'Em Progresso' / 'Concluído') ")
                chamado.status = novo_status
                print("Chamado Atualizado")
                return
        print("Chamado não encontrado")

    def Inicialização(self):
         while True:
            if not self.login():
                return 
            else:
                print("Deseja tentar novamente? (S/N)")
                if input().strip().upper() != 'S':
                    return
        
            while True:
                if self.usuario_atual.admin:
                    print("1. Visualizar Chamados")
                    print("2. Atualizar Chamados")
                    print("0. Sair")
                    opcao = input("Escolha uma opção: ")
                    if opcao == '1':
                        self.visualizarChamados()
                    elif opcao == '2':
                        self.atualizarChamados()
                    elif opcao == '0':
                        break
                    else:
                        print("Opção inválida.")
                else:
                    print("1. Criar Chamados")
                    print("2. Visualizar Chamados")
                    print("0. Sair")
                    opcao = input("Escolha uma opção: ")
                    if opcao == '1':
                        self.criarChamado()
                    elif opcao == '2':
                        self.visualizarChamados()
                    elif opcao == '0':
                        break
                    else:
                        print("Opção inválida.")


sistema = SistemaChamados()
sistema.Inicialização()

