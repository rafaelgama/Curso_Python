# Herança Simples - POO
# Sobreposição de membros

from classes import *

c1 = Cliente('Rafael', 39)
print(c1.nome)
c1.falar()
c1.comprar()

c2 = ClienteVip('Rose', 25, 'Miranda')
c2.falar()
