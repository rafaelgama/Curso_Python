# Herança Simples - POO

from classes import *

c1 = Cliente('Rafael', 39)
print(c1.nome)
c1.falar()
c1.comprar()

a1 = Aluno('Gama',40)
print(a1.nome)
a1.falar()
a1.estudar()

p1 = Pessoa('João',43)
p1.falar()
