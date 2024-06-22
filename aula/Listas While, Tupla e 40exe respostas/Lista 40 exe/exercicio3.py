'''
A padaria Pão&Bão tem um fluxo diário de vendas de pães franceses e 
broas. Cada pão é vendido por R$ 0,12 e cada broa por R$ 1,50. No final 
de cada dia, o proprietário deseja saber quanto foi arrecadado com a venda 
total de pães e broas e quanto ele deve guardar em uma conta poupança, 
correspondente a 10% desse valor arrecadado. Para ajudar o proprietário, 
você foi contratado para fazer os cálculos. Faça um algoritmo para ler as 
quantidades de pães e de broas, e depois efetue o cálculo.
'''

pães = float(input("Quantidade de pães vendidos hoje: " ))*0.12
broas = float(input("Quantidade de broas vendidos hoje: " ))*1.50

soma =  (pães + broas)*0.1

print(f"No seu dia R${soma}")