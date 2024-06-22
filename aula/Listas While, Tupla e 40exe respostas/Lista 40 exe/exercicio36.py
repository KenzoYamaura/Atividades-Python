'''Faça um programa que leia uma cadeia de caracteres (string) e determine 
a quantidade de caracteres. Não é permitido o uso de nenhuma função ou 
biblioteca do Python'''

'''texto = 'Jujutsu no Kaisen'
cont = 0 

for i in texto:
    print(i)
    cont += 1

print(f'Quantidades de Caracteres é {cont}')'''


texto = input('Digite um texto: ')
cont = 0

while texto:
    print(texto)
    cont += 1
    texto = texto[1:]
print(cont)


