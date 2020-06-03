# combinations, Permutations e Product - itertools
# Combinação - Ordem não importa
# Permutação - Ordem importa
# Ambos não repetem valores únicos
# Produto - Ordem importa e repete valores únicos

from itertools import combinations, permutations, product

# Combinations - Faz as combinações sem repetir as duplas, ou triplas.. etc..
# A ordem não importa nesse caso.
pessoas = ['Luiz','André','Eduardo','Letícia','Fabrício','Rose']

'''for grupo in combinations(pessoas, 2):
    print(grupo)'''

# Permutations - Faz as combinção da mesma forma para todos, Repetindo os pares.
# A ordem importa nesse caso.
"""for grupo in permutations(pessoas, 2):
    print(grupo)"""

# Product - Faz todas as combinações possíveis, repetindo o mesmo valor.
# A ordem não importa nesse caso.
for grupo in product(pessoas, repeat=2):
    print(grupo)











