'''
Dada uma sequência de n números reais, determinar o número de vezes 
que cada um deles ocorre. A contagem deve parar quando digitar -1. Para 
exemplificar, considere: 
Entrada-1: 1, 2 e 3 
Entrada-2: 1, 1, 4, 5, 6, 7, 3, 2, 2, -1 
Saída: 
1: ocorreu 2 vezes 
2: ocorreu 2 vezes 
3: ocorreu 1 vez
'''

lista1 = []
lista2 = []
cont1 = 0
cont2 = 0
cont3 = 0
j = 0
for i in range(3):
    lista1.append(int(input('Digite uns numero: ')))

while True:
    lista2.append(int(input('Digite outros número: ')))
    if lista2[j] == -1:
        break
    elif lista2[j] == lista1[0]:
        cont1 += 1
    elif lista2[j] == lista1[1]:
        cont2 += 1
    elif lista2[j] == lista1[2]:
        cont3 += 1
    j +=1

print(cont1)
print(cont2)
print(cont3)