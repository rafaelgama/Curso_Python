# dicionários em Python

import copy

d1 = { 1: 'a', 2: 'b', 3:'c', 'd':['Rafael','Gama'] }
#v = d1.copy() # exemplo de cópia rasa.
v = copy.deepcopy(d1) # cópia profunda, copia para outro ponto de memória.

v[1] = 'Rafa'
v['d'][0] = 'Jão'

print(d1)
print(v)


