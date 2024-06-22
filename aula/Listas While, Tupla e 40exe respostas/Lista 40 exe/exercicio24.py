'''Elabore um algoritmo que calcule o que deve ser pago por um produto, 
considerando  o  preço  normal  de  etiqueta  e  a  escolha  da  condição  de 
pagamento. Utilize os códigos da tabela a seguir para ler qual a condição 
de pagamento escolhida e efetuar o cálculo adequado. Código Condição de 
pagamento:  
a. 1 À vista em dinheiro ou cheque, recebe 10% de desconto  
b. 2 À vista no cartão de crédito, recebe 15% de desconto  
c. 3 Em duas vezes, preço normal de etiqueta sem juros  
d. 4 Em três vezes, preço normal de etiqueta mais juros de 10%'''

produto = float(input('Valor do produto: R$'))
print('1º - À vista em dinheiro ou cheque, recebe 10% de desconto')
print('2º - À vista no cartão de crédito, recebe 15% de desconto')
print('3º - Em duas vezes, preço normal de etiqueta sem juros')
print('4º - Em três vezes, preço normal de etiqueta mais juros de 10%')
pagamento = input('Escolha um método de pagamento: ')

pagamento_a_vista = produto - (produto*0.10)
pagamento_credito = produto - (produto*0.15)
pagamento_em_duas = produto/2
pagamento_em_tres = (produto + (produto*0.10))/3

if pagamento == "1":
    print(f'O valor a pagar é R${produto} e com desconto fica R${pagamento_a_vista}')
elif pagamento == '2':
    print(f'O valor a pagar é R${produto} e com desconto fica R${pagamento_credito}')
elif pagamento == '3':
    print(f'O valor a pagar é R${produto} e a parcela fica R${pagamento_em_duas}')
elif pagamento == '4':
    print(f'O valor a pagar é R${produto} e a parcela fica R${pagamento_em_tres}')
else:
    print('Escolha uma opção de pagamento válida')

