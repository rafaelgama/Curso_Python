# Herança sempre vem de cima para baixo na hierarquia.
# Sobreposição de membros

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nomeClasse = self.__class__.__name__

    def falar(self):
        print(f'{self.nomeClasse} falando...')

# Herda os atributos da classe Pessoa
class Cliente(Pessoa):
    def comprar(self):
        print(f'{self.nomeClasse} comprando...')

    # Se existir um método def falar() aqui, o super executa ele primeiro.

# Herda os atributos da classe Pessoa e da classe Cliente
'''class ClienteVip(Cliente):
    def falar(self):
        # super() ele executa os metodos da classe herdada até encontrar o método.
        super().falar() 
        # Pode chamar direto, colocando por exemplo: Pessoa.falar(self), mas não poderia ficar sem o self, 
        # para saber de qual instancia que ele veio.
        print(f'{self.nomeClasse} falando de novo...')'''

# Exemplo de Atributo exclusivo da classe
class ClienteVip(Cliente):
    def __init__(self, nome, idade, sobrenome):
        Pessoa.__init__(self, nome, idade)
        self.sobrenome = sobrenome

    def falar(self):
        Pessoa.falar(self)

        print(f'{self.nome} {self.sobrenome}')




