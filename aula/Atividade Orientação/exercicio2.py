from collections.abc import Iterable


class Aluno:    
    def __init__(self, nome, ra):
        self.nome = nome
        self.ra = ra
        self.lista = self.NotasAlunos()
 
    def NotasAlunos(self):
        qtd_notas = int(input("Quantas notas quer lançar? "))
        lista_notas = []
        for i in range(qtd_notas):
            notas = float(input(f"Digite a {i+1}º Nota: "))
            lista_notas.append(notas)
        return lista_notas

    def mostrarMedia(self):
        return sum(self.lista)/len(self.lista)
    
    def mostrarSituacao(self):
        media = self.mostrarMedia()
        if media >= 7:
            print("Aprovado")
        elif media < 5:
            print("Reprovado")
        else:
            print("Exame")

    
aluno1 = Aluno("Kenzo", "311123")

aluno1.mostrarMedia()
aluno1.mostrarSituacao()







