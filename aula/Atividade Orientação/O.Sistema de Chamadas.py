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

class Login:
    def __init__(self, login, senha):
        self.login = login
        self.senha = senha

class Administrativo(Login):
    def __init__(self, login, senha, matricula):
        super().__init__(login, senha)
        self.matricula = matricula
    
class Cliente(Login):
    def __init__(self, login, senha, ):
        super().__init__(login, senha)
        

class CadastroChamados:
    def __init__(self):
        chamados = []
    
    def AbrirChamado(self):
