class Conta:
    def __init__(self, nome, cpf, numero, saldo):
        self.nome = nome
        self.cpf = cpf
        self.numero = numero
        self.saldo = saldo
    
    def DepositarConta(self):
        print(f"Saldo Atual R${self.saldo}")
        depositar = float(input("Quanto deseja depositar? R$"))
        if depositar > 0:
            self.saldo += depositar
        else:
            print(f"O valor do depósito tem que ser positivo")

    def SacarSaldo(self):
        print(f"Saldo atual R${self.saldo}")
        saque = float(input("Quanto deseja sacar? R$"))
        if saque > 0:
            if saque >= saque:
                self.saldo -= saque
                print(f"Saque realizado com sucesso")
            else:
                print("Saldo insuficiente para saque")
        else:
            print("O valor deve se positivo")
    
    def ImprimirSaldo(self):
        print(f"Seu saldo Atual é R${self.saldo}")
    
contaBanco1 = Conta("Kenzo", "566.548.948-74", "41423", 0)

contaBanco1.DepositarConta()
contaBanco1.SacarSaldo()
contaBanco1.ImprimirSaldo()

