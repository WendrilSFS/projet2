class Aluno:
    def __init__(self,nome,ra,n1,n2,n3,n4):
        self.nome = nome
        self.ra = ra
        self.nota1 = n1
        self.nota2 = n2
        self.nota3 = n3
        self.nota4 = n4

    def mostrarsituacao(self):
        media = (self.nota1 + self.nota2 + self.nota3 + self.nota4) / 4
        if media <5:
            return "reprovdo"
        elif media >=5 and media <= 6.9:
            return "exame"
        else:
            return "aprovado"
        

aluno1 = Aluno("Wendril",1127,7.8,8.5,8.9,9.5)

print(aluno1.nome, aluno1.mostrarsituacao())