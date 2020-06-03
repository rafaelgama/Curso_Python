# Agrupando Valores - Groupby

from itertools import groupby
# Para o Groupby funcionar, sempre será necessários ordenar os dados.

alunos = [
    {'nome':'Rafael','nota':'A'},
    {'nome':'Luiz','nota':'B'},
    {'nome':'Gama','nota':'B'},
    {'nome':'Macedo','nota':'C'},
    {'nome':'João','nota':'D'},
    {'nome':'André','nota':'A'},
    {'nome':'Eduardo','nota':'B'},
    {'nome':'José','nota':'D'},
    {'nome':'Anderson','nota':'E'},
    {'nome':'Maria','nota':'C'},
]
# sem variavael de ordenação
"""alunos.sort(key=lambda item: item['nota'])
for aluno in alunos:
    print(aluno)
alunos_agrp = groupby(alunos, lambda item: item['nota'])
"""
# com variável de ordenação
ordena = lambda item: item['nota']
alunos.sort(key=ordena)
alunos_agrp = groupby(alunos,ordena)

for grupo, valor in alunos_agrp:
    print(f'Grupo: {grupo}')
    quant = len(list(valor))
    print(f'{quant} alunos tiraram a nota {grupo}')
    #for aluno in valor:
    #    print(aluno)






