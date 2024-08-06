
class Barbearia:
    def __init__(self):
        self.agendamentos = []
    
    def Agendar(self):
        nomeCliente = input("Digite o Nome do Cliente: ")
        data = input("Digite o Dia que foi marcado: ")
        hora = input("Digite a Hora que foi marcada: ")
        servico = input("Digite o Serviço: ")
        agenda = Agendamento(nomeCliente, data, hora, servico)
        self.agendamentos.append(agenda)
        print(f"O Agendamento de {nomeCliente} foi realizado com sucesso")

    def Cancelar(self):
        nomeCancelamento = input("Qual cliente gostaria de cancelar o serviço? ")
        for i in self.agendamentos:
            if i.nomeCliente == nomeCancelamento:
                self.agendamentos.remove(i)
        print("Cancelamento feito com sucesso")

    def VisualizarAgenda(self):
        for i in self.agendamentos:
            print("-" * 40)
            print(f"Nome do Cliente: {i.nomeCliente} \nData: {i.data} \nHora: {i.hora} \nServiço: {i.servico}")
            print("-" * 40)

class Agendamento:
    def __init__(self, nomeCliente, data, hora, servico):
        self.nomeCliente = nomeCliente
        self.data = data
        self.hora = hora
        self.servico = servico
    
barbearia = Barbearia()

while True:
    print("Barbearia")
    print("-" * 40)
    print("1 - Agendar")
    print("2 - Cancelar")
    print("3 - Visualizar Agenda")
    print("0 - Sair")
    print("-" * 40)

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        barbearia.Agendar()
    elif opcao == 2:
        barbearia.Cancelar()    
    elif opcao == 3:
        barbearia.VisualizarAgenda()
    elif opcao == 0:
        print("Saindo...")
        break
        


    
    
