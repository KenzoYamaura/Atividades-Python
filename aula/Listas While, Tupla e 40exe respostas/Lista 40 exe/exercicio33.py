'''A  prefeitura  de  uma  cidade  fez  uma  pesquisa  entre  seus  habitantes, 
coletando dados sobre o salário e número de filhos. A prefeitura deseja 
saber:
  
a) média do salário da população;  
b) média do número de filhos; 
c) maior salário; 
d) percentual de pessoas com salário até R$100,00. 
O final da leitura de dados se dará com a entrada de um salário negativo. 
(Use o comando ENQUANTO-FAÇA).
'''
'''populacao = int(input('População da Cidade: '))
salario_H = float(input('Digite seu Salário: R$'))
numero_filhos = int(input('Quanto filhos tem?: '))'''

populacao = int(input("Digite a população: "))

s_media = 0
f_media = 0
m_salario = 0
salario_abaixo_100 = 0

cont = 1
while cont <= populacao:
    salario = float(input(f'Salário da População {cont}: '))
    m_salario += salario
    if salario > m_salario:
        m_salario = salario
    if salario <= 100:
        salario_abaixo_100 += 1


    filhos = int(input(f"Quantos filhos o cidadão {cont} tem? :"))
    f_media += filhos
    cont += 1

print("-"*20)

media1 = s_media / populacao
print(f"A media dos salário é {media1}")

media2 = f_media / populacao
print(f"A média dos filhos é {media2}")
print(f"O Maior salário = {m_salario}")
print(f"O menor salário é {salario_abaixo_100}")