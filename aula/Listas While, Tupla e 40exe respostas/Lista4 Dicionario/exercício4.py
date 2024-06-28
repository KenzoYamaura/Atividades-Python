'''O gestor de uma rede de shoppings, precisa contratar um sistema para administrar o
estacionamento, a principal função do sistema é calcularTemp(). Considere o valor
mínimo de R$9,00 por hora e R$1,50 por hora adicional. O principal argumento da 
função é o tempo utilizado em minutos, a função deve retornar o valor total. Caso o 
usuário fique no estacionamento por menos de 15 minutos, o tempo utilizado não será cobrado.'''


def calcularTemp(tempo_m):
    v_minimo = 9.00

    if tempo_m < 15:
        return 0.0
    
    horas = tempo_m // 60    

    if horas > 0:        
        v_total = v_minimo
        horas -= 1
        if horas > 0:
            v_total += horas * 1.5 
    else:
        v_total = v_minimo

    return v_total

temp = float(input("Horas no estacionamento: "))

print(f"Você ficou {temp:.0f} minutos, valor a pagar é R$ {calcularTemp(temp):.2f}")
    