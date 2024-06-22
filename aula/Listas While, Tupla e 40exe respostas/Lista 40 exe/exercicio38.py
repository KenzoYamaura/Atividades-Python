'''
Desafio das Sequências Numéricas: 
Você  é  desafiado  a  criar  um  programa  que  gera  sequências  numéricas 
especiais de acordo com as regras fornecidas. As regras são as seguintes: 
 
a. A sequência começa com dois números inteiros fornecidos pelo 
usuário: a e b. 
b. O próximo número na sequência é determinado pela soma dos dois 
números anteriores. 
c. Se  a  soma for  um número  ímpar,  esse  número  é  adicionado  à 
sequência e atualiza a para o valor de b e b para o valor da soma. 
Calcula o novo valor da soma. 
d. Se a soma for um número par, a soma é dividida por 2 e o resultado 
é adicionado à sequência. 
e. O processo de verificação continua até que a soma seja igual a 1. 
f. O programa deve exibir a sequência completa. 
Exemplo: se a=2 e b=3 
Saída: 2 3 5 8 4 2 1 '''

a = int(input('Digite A: '))
b = int(input('Digite B: '))

lista = [a, b]
soma = a + b

while soma != 1:
    print(lista)
    if soma % 2 == 1:
        lista.append(soma)
        a = b
        b = soma
        soma = a + b
    else:
        lista.append(soma)
        soma = soma // 2 

lista.append(soma)
print(lista)