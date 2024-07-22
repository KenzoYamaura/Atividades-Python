class Funcionario():
    def __init__(self, nome, sobrenome, horas_trabalhas, valor_hora):
        self.nome = nome
        self.sobrenome = sobrenome
        self.horasTrab = horas_trabalhas
        self.valor_hora = valor_hora

    def NomeCompleto(self):
        print(f"Nome completo do Funcionário é {self.nome + ' ' + self.sobrenome} ")
    
    def CalcularSalario(self):
        salario = self.horasTrab * self.valor_hora
        print(f"Seu salário é R${salario:.2f}")

    def IncrementarHoras(self, valor_h):
        self.valor_hora += valor_h 


funcionario1 = Funcionario(input("Nome: "), input("Sobrenome: "), int(input("Horas Trabalhadas: ")), float(input("Valor das horas: ")))

funcionario1.NomeCompleto()
funcionario1.CalcularSalario()
funcionario1.IncrementarHoras(3)
funcionario1.CalcularSalario()