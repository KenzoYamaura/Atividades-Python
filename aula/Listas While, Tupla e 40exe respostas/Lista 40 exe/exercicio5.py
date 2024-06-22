'''Escreva um algoritmo capaz de somar duas frações, informadas do seguinte 
modo: 𝑥
𝑦 +𝑎
𝑏 . O resultado deve ser expresso na forma de uma fração'''

x = int(input("insira o x: "))
y = int(input("insira o y: "))
a = int(input("insira o a: "))
b = int(input("insira o b: "))

resultado = ((x*b) + (y*a)) / (y*b)
print(resultado)
