''' Escreva  um  programa  que  calcula  o  desconto  previdenciário  de  um 
funcionário. Dado um salário, o programa deve retornar o valor do desconto 
proporcional ao mesmo. O cálculo segue a regra: o desconto é de 11% do 
valor do salário, entretanto, o valor máximo de desconto é 334,29.'''

salario_bruto = float(input('Insira seu salário: R$'))
desconto = salario_bruto*0.11

if desconto >= 334.29:
    desconto = 334.29
    print(f'Seu salário final é {salario_bruto - desconto}')
    print(f'oque foi descontado {desconto}')
else:
    print(f'Seu salário final é {salario_bruto - desconto}')
    print(f'oque foi descontado {desconto}')
