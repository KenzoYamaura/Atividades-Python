'''Faça um Programa que pergunte quanto você ganha por hora e o número 
de horas trabalhadas no mês. Calcule e mostre o total do seu salário no 
referido mês, sabendo-se que são descontados 11% para o Imposto de 
Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos 
dê: 
a. salário bruto. 
b. quanto pagou ao INSS. 
c. quanto pagou ao sindicato. 
d. o salário líquido. 
e. calcule os descontos e o salário líquido, conforme a tabela abaixo:
1 - quanto vc ganha por hora
2 - e o numero de horas trabalhadas
3 - 
'''

hora_trabalhada = float(input("Insira sua hora trabalhada por mês: "))
valor_trabalhada = float(input("Valor da sua hora: "))

salário_bruto = (hora_trabalhada*valor_trabalhada)

p_sindicato = salário_bruto*0.05
p_inss = salário_bruto*0.08
p_iof = salário_bruto*0.11

salario_final = salário_bruto - (p_sindicato + p_inss + p_iof)
print(f"+ Salário Bruto: {salário_bruto}")
print(f"- Sindicato: {p_sindicato}")
print(f"- INSS: {p_inss}")
print(f"- IOF: {p_iof}")
print(f"= Salário Liquido: {salario_final}")


 

