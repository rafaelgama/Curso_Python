# Herança sempre vem de cima para baixo na hierarquia.

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nomeClasse = self.__class__.__name__

    def falar(self):
        print(f'{self.nomeClasse} falando...')



class Cliente(Pessoa):
    def comprar(self):
        print(f'{self.nomeClasse} comprando...')

class Aluno(Pessoa):
    def estudar(self):
        print(f'{self.nomeClasse} estudando...')






