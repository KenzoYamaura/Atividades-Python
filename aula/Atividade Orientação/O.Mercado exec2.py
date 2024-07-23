'''Você foi contratado para desenvolver um sistema de gerenciamento escolar em Python 
que   permita   aos   professores   gerenciar   turmas   e   alunos.   O   sistema   deve   oferecer 
funcionalidades para cadastrar turmas, adicionar alunos e suas notas, atualizar informações 
dos alunos, remover alunos e visualizar as informações das turmas e alunos cadastrados.'''

class Escola:
    def __init__(self, nomeTurma):
        self.nomeTurma = nomeTurma
        self.listaDeTurma = []
    
    def AdicionarTurma(self, turma):
        if turma not in self.listaDeTurma:
            self.listaDeTurma.append(turma)
        else:
            print("Aluno Ja existente")


class Turma:
    def __init__(self, nomeAluno):
        self.nomeAluno = nomeAluno
        self.alunos = []

    def AdicionarAluno():
        pass




class Aluno:
    def __init__(self, nome):
        self.nome = nome
        self.notas = []
    
    def AddNotas(self, notas):
        self.notas.append(notas)


escola = Escola("Turma A")

