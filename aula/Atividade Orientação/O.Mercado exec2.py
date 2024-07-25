class Escola:
    def __init__(self):
        self.turmas = []
    
    def AdicionarTurmas(self):
        nome = input("Digite o nome da turma: ")
        turma = Turmas(nome)
        self.turmas.append(turma)
    
    def AdicionarAlunosEmTurma(self):
        nomeTurma = input("Digite o nome da turma: ")
        turma = self.BuscarTurmas(nomeTurma)

        if turma:
            turma.AdicionarAluno()
        else:
            print("Turma não encontrada")

    def BuscarTurmas(self, nomeTurma):
        for i in self.turmas:
            if i.nome == nomeTurma:
                return i
        
    def Detalhe(self):
        for i in self.turmas:
            print(f"{i.nome}")
            for j in i.alunos:
                print(f"{j.nome} - {j.notas}")
    
class Turmas:
    def __init__(self, nome):
        self.nome = nome
        self.alunos = []
    
    def AdicionarAluno(self):
        nome = input("Digite o nome do Aluno: ")
        aluno = Alunos(nome)
        aluno.AdicionarNotas()
        self.alunos.append(aluno)
    
class Alunos:
    def __init__(self, nome):
        self.nome = nome
        self.notas = []
    
    def AdicionarNotas(self):
        qtd = int(input("Digite a quantidade de notas: "))
        for i in range(qtd):
            nota = float(input(f"Digite a {i+1}ª nota do aluno {self.nome}: "))
            self.notas.append(nota)

escola = Escola()

while True:
    print("1 - Adicionar Turma")
    print("2 - Adicionar Alunos em uma turma")
    print("3 - Detalhes das turmas")

    opcao = int(input("Digite uma das opções: "))

    if opcao == 1:
        escola.AdicionarTurmas()
    
    elif opcao == 2:
        escola.AdicionarAlunosEmTurma()
    
    elif opcao == 3:
        escola.Detalhe()