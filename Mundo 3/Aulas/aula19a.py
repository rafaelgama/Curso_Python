# Nessa aula, vamos aprender o que são DICIONÁRIOS e como utilizar dicionários em Python. 
# Os dicionários são variáveis compostas que permitem armazenar vários valores em uma mesma estrutura, acessíveis por chaves literais.

print(f'{"Listas com dicionários":=^40}')
bra = list()
estado1 = {'uf':'Rio de Janeiro', 'sigla':'RJ'}
estado2 = {'uf':'São Paulo', 'sigla':'SP'}
bra.append(estado1)
bra.append(estado2)

print(f'{"Print Normal":=^40}')
print(bra)

print(f'{"Print com indice e dicionario":=^40}')
print(bra[1]['uf'])

print(f'{"Laços - Listas com dicionários":=^40}')
estado = dict()
brasil = list()
for c in range(0,3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    # Para dicionários, não pode fatiar ([:]), tem que utilizar o método copy()
    brasil.append(estado.copy())
print(f'{"Print Normal":=^40}')
print(brasil)
print(f'{"Print com o laço":=^40}')
for e in brasil:
    print(f'{e}')

print(f'{"Print com o laço dentro do laço":=^40}')
for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem o valor {v}')

