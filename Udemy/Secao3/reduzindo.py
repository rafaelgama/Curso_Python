from dados import produtos, pessoas, lista
from functools import reduce


print('-=-'* 20)
print(f'{" reduce com listas ":=^40}')
print(lista)

# a função reduce() é um acumulador
# exemplo de acumulador normal
'''acumula = 0
for item in lista:
    acumula += item
print(acumula)'''

soma_lista = reduce(lambda ac, i: i + ac, lista,0)
print(soma_lista)

print('-=-'* 20)
#Utilizando reduce com dicionarios - produtos
print(f'{" reduce com dicionarios 1 ":=^40}')

soma_preco = reduce(lambda ac, p: p['preco'] + ac, produtos, 0)
print(soma_preco)

print('-=-'* 20)
#Utilizando reduce com dicionarios - pessoas
print(f'{" reduce com dicionarios 2 ":=^40}')

soma_idade = reduce(lambda ac, p: p['idade'] + ac, pessoas, 0)
print(soma_idade / len(pessoas)) # media de idade

print('-=-'* 20)

