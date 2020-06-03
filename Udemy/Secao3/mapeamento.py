from dados import produtos, pessoas, lista

print('-=-'* 20)
print(f'{" MAP com listas ":=^40}')
print(lista)

# map() sempre recebe uma função como primeiro parâmetro.
# map retorna sempre um iterador.
nova_lista = map(lambda x: x * 2, lista) 
# utilizando o list comprehenson no lugar de map()
nova_lista = [x * 2 for x in lista]
print(list(nova_lista))

print('-=-'* 20)

#Utilizando MAP com dicionarios - produtos
print(f'{" MAP com dicionários 1 ":=^40}')

def aumenta_preco(p):
    p['preco'] = round(p['preco'] * 1.05, 2)
    return p

novo_prd = map(aumenta_preco, produtos)

for prod in novo_prd:
    print(prod)

print('-=-'* 20)

#Utilizando MAP com dicionarios - pessoas
print(f'{" MAP com dicionários 2 ":=^40}')

nomes = map(lambda p: round(p['idade'] * 1.20,2), pessoas)

for pessoa in nomes:
    print(pessoa)

print('-=-'* 20)