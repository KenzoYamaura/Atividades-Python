'''Crie um programa que leia o tamanho de três segmentos de reta. Analise 
seus comprimentos e diga se é possível formar um triângulo com essas 
retas.  Matematicamente,  para  três  segmentos  formarem  um  triângulo,  o 
comprimento de cada lado deve ser menor que a soma dos outros dois.'''

a = float(input("Insira o primeiro segmento de reta: "))
b = float(input("Insira o segundo segmento de reta: "))
c = float(input("Insira o terceiro segmento de reta: "))

if a < b + c and b < a + c and c < a + b:
    print("Formam um triangulo")
else:
    print("Não formam um triângulo")