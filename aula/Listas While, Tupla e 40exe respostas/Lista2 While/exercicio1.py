'''Faça um programa que peça duas notas, entre zero e dez e mostre uma mensagem caso o 
valor seja inválido. O programa deve continuar pedindo até que o usuário informe um valor 
válido. No final, mostre o resultado da média.'''


while True:
    n1 = float(input("Insira a primeira nota: "))
    n2 = float(input("Insira a segunda nota: "))
    if n1 >= 0 and n1 <= 10 and n2 >= 0 and n2 <= 10:
        print(f"A média é {(n1+n2)/2}")
        break        
    else:
        print("Insira uma nota válida")
    
