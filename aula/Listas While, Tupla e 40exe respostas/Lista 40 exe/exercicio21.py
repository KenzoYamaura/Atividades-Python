'''Escreva um programa que leia um carracter e diga se ele é uma vogal, 
consoante, número ou um símbolo (qualquer outro caracter, que não uma 
letra ou número).
 
Vogais = a, e, i, o, u,
consoantes: b, c, d, f, g, h, j, k, l, m, n, p, q, r, s, t, v, x, y, w, z.
numeros = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
'''
lista = (['a', 'e', 'i', 'o', 'u'],['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'x', 'y', 'w', 'z'],['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
a = False

caracter= input('Digite um caracter: ')
for i in range(len(lista)):
    for j in range(len(lista[i])):
        if caracter in lista[i][j]:
            a = True
            break
    if a:
        break

if a:
    if i == 0:
        print('É uma Vogal.')
    elif i == 1:
        print('É uma Consoante.')
    elif i == 2:
        print('É um número')
else:
    print('É um símbolo')
    
