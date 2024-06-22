'''Crie  um  programa  que  simule  as  operações  de  um  caixa  eletrônico.  O 
usuário deve poder verificar o saldo, depositar e sacar dinheiro da conta. O 
programa deve continuar funcionando até que o usuário escolha sair.'''

saldo = float(input('Dinheiro na sua conta: R$'))
print('--- BANCO ---')
print('1 - Verificar Saldo')
print('2 - Depositar')
print('3 - Sacar Dinheiro')
print('0 - Sair')
operacao = int(input('Oque deseja?: '))

while operacao != 0:
        
    if operacao == 1:
        print(f'Seu Saldo em conta R${saldo}')

    elif operacao == 2:
        deposito = float(input('Qual quantia deseja depositar?: R$'))
        saldo += deposito
        print(f'Seu deposito de R${deposito} realizado com sucesso. Seu Saldo atual é R${saldo}')      

    elif operacao == 3:
        if saldo > 0:
            print(f'Deseja sacar quando do seu saldo atual R${saldo}?')
            saque = float(input('Qual quantia deseja sacar?: R$'))
            if saque <= saldo:
                saldo -= saque
                print(f'Seu saque de R${saque} realizado com sucesso. Seu Saldo atual é R${saldo}')
            else:
                print('Não tem saldo para saque')
        else:
            print('Saldo Insuficiente')

    elif operacao == 0:
        print('Saindo da conta')

    else:
        print('Operação Inválida')
    operacao = int(input('O que deseja?: '))

print('Obrigado por utilizar os serviços do nosso Banco')
