# Dataclasses em python
"""
O que são dataclasses? O módulo Dataclasses fornece um decorador e funções
para criar automaticamente métodos, como __init__(), __repr__(), __eq__ (etc)
em classes definidas pelo usuário.
Basicamente, dataclasses são syntax sugar para criar classes normais.
Foi originalmente descrito na PEP 557.
Adicionado na versão 3.7 do Python.
Leia a documentação: https://docs.python.org/pt-br/3/library/dataclasses.html
"""

from dataclasses import dataclass

# para desabilitar algum método que ja está embutido, declara ele como falso
# dentro do @dataclass, por ex: @dataclass(eq=False,  repr=False)
@dataclass
class Pessoa:
    nome: str
    sobrenome: str

    def __post_init__(self):
         self.nome_completo = f'{self.nome} {self.sobrenome}'

    #@property
    #def nome_completo(self):
    #    return f'{self.nome} {self.sobrenome}'

p1 = Pessoa('Rafael','Gama')
p2 = Pessoa('Rafael','Gama')

print(p1 == p2) # utiliza o metodo __eq__

print(p1.nome)
print(p1.sobrenome)
print(p1.nome_completo)
