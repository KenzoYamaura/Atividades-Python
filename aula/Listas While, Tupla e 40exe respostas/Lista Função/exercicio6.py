'''Escreva uma função para contar a quantidade de vogais de uma frase. A função deve 
receber uma string como parâmetro e retorna o número de vogais presentes na string.
Vogais: a,e,i,o,u
frase = "aqui programamos em python"
# para frase acima, saida = 9'''
 

def fun(word):
    vogais = ['a','e','i','o','u','A','E','I','O',]
    cont = 0    
    for i in word:
        if i in vogais:
            cont += 1
    print(f'Existem {cont} vogais nessa frase')

word = input("Digite uma frase: ")
fun(word)
        
