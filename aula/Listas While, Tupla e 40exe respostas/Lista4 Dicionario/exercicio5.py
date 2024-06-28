'''Escreva uma função que recebe duas listas de palavras como argumentos. A função 
deve retornar uma nova lista contendo todas as palavras que possuem a primeira letra 
em comum. Por exemplo, se as duas listas de palavras forem:
Saída:
'''
palavras1 = ['casa', 'carro', 'computador', 'banana']
palavras2 = ['cadeira', 'mesa', 'cachorro', 'tomate']

def words():
    lista = []
    a = palavras1[0][0]

    for i in palavras1:
        if i[0][0] == a:
            lista.append(i)            
    
    for j in palavras2:
        if j[0][0] == a:
            lista.append(j)
    print(lista)

words()