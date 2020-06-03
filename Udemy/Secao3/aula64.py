# Geradores, Iteradores e Iteráveis em Python.

# para ter certeza que um objeto é Iterável use comando:
import sys
import time

lista = [1,2,3,4,5,6] 
lis01 = 123

print(hasattr(lista,'__iter__')) # Se for iteravel, retorna True
print(hasattr(lis01,'__iter__')) 

# o for transforme a lista em um Iteradore
# Para saber se objeto é um Iterador, use o comando:
print(hasattr(lista, '__next__'))

# para adicionar no objeto o iterador, sem usar o For
lista = iter(lista)

# quando o objeto possue o iterador, vc pode usar a função NEXT
print(next(lista))
print(next(lista))

print(hasattr(lista, '__next__'))

print('-=-'*20)
# Geradores 
# Exemplo 1
def gera():
    for n in range(10):
        yield n
        #time.sleep(0.1)

g = gera()

print(hasattr(g,'__iter__')) 
print(hasattr(g,'__next__')) 

for v in g:
    print(v)

print('-=-'*20)

lista2 = list(range(100))

# Quantidade de memória utilizada na variável em bytes.
print(sys.getsizeof(lista2))

print('-=-'*20)

# Exemplo 2
# criar uma lista normal
lista3 = [x for x in range(100)]
print(type(lista3))
lista4 = (x for x in range(100)) # Geradores não guardam tudo na memória.
print(type(lista4))

print(sys.getsizeof(lista3))
print(sys.getsizeof(lista4))

