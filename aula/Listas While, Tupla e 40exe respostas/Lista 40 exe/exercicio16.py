'''
Faça um Programa para uma loja de tintas. O programa deverá pedir o 
tamanho em metros quadrados da área a ser pintada. Considere que a 
cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é 
vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 
litros, que custam R$ 25,00. Informe ao usuário as quantidades de tinta a 
serem compradas e os respectivos preços em 3 situações: 
a. comprar apenas latas de 18 litros; 
b. comprar apenas galões de 3,6 litros; 
c. misturar latas e galões, de forma que o desperdício de tinta seja 
menor. Acrescente 10% de folga e sempre arredonde os valores 
para cima, isto é, considere latas cheias.
'''

metros = float(input('Quantidades de metros da área: '))

litros = metros / 6
print('Quantidade de litros necessários: ', litros)

#Calculando a quantidade de latas para pintar a área desejada.
#O // (só pegando a parte inteira da divisão)
qtdLatas = litros // 18
if litros  % 18 != 0:
    qtdLatas = qtdLatas + 1

print('Quantidade de latas de 18 litros: ', qtdLatas)

preco_latas = qtdLatas * 80.00
print('Valor da compra de latas: ', preco_latas)

qtdGaloes = litros // 3.6
if litros  % 3.6 != 0:
    qtdGaloes = qtdGaloes + 1

print('Quantidade de galoes de 3,6 litros: ', qtdGaloes)

preco_galoes = qtdGaloes * 25.00
print('Valor da compra de galoes: ', preco_galoes)

#cobertura de area com uma lata de 18l
cobertura_latas = 18 * 6
#cobertura de area com um galão de 3,6l
cobertura_galoes = 3.6 * 6

#
qtd_latas_mistura = int(metros / cobertura_latas)

area_contemp = qtd_latas_mistura * cobertura_latas

#tamanho da area que falta
area_falta = metros - area_contemp

litros_galao_mistura = area_falta / 6

qtd_galao_mistura = int(litros_galao_mistura / 3.6)
if litros_galao_mistura % 3.6 != 0:
    qtd_galao_mistura = qtd_galao_mistura + 1

print('Quantidade de galoes da mistura: ', qtd_galao_mistura)

print('PREÇO: R$', ((qtd_latas_mistura * 80.00) + (qtd_galao_mistura * 25.00)))