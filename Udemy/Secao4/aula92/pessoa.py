# Aula de Classes- Python orientado a Objetos

# quando uma função está dentro de uma classe, ela se torna um método
# da classe.
from datetime import datetime

# Exemplo 1
"""
class Pessoa:
    # self se refere a instancia da classe que está chamando o método.
    def falar(self):
        print('Pessoa está falando...')
"""

# Exemplo 2
# sempre que os métodos conter o self, todas as variaveis da classe são acessíveis
class Pessoa:
    ano_atual = int(datetime.strftime(datetime.now(), '%Y'))

    def __init__(self, nome, idade, comendo=False, falando=False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando
    
    def falar(self, assunto):
        if self.comendo:
            print(f'{self.nome} não pode falar comendo.')
            return

        if self.falando:
            print(f'{self.nome} já está falando.')
            return

        print(f'{self.nome} está falando sobre {assunto}.')
        self.falando = True

    def parar_falar(self):
        if not self.falando:
            print(f'{self.nome} não está falando.')
            return
        
        print(f'{self.nome} parou de falar.')
        self.falando = False
    
    def comer(self, alimento):
        # para controlar e não deixar comer duas vezes.
        if self.comendo:
            print(f'{self.nome} já está comendo.')
            return
        
        if self.falando:
            print(f'{self.nome} não pode comer falando.')
            return

        print(f'{self.nome} está comendo {alimento}')
        self.comendo = True

    def parar_comer(self):
        if not self.comendo:
            print(f'{self.nome} não está comendo.')
            return
        print(f'{self.nome} parou de comer.')
        self.comendo = False
    

    def get_ano_nascimento(self):
        return self.ano_atual - self.idade









