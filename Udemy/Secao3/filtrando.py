from dados import produtos, pessoas, lista

print('-=-'* 20)
print(f'{" filter com listas ":=^40}')
print(lista)

# A função filter sempre começar com uma função e so retorna boolean.
# filter retorna sempre um iterador.
nova_lista = filter(lambda x: x > 5, lista )
# utilizando o list comprehenson no lugar de filter()
nova_lista = [x for x in lista if x > 5]
print(list(nova_lista))

print('-=-'* 20)

#Utilizando MAP com dicionarios - produtos
print(f'{" filter com dicionarios 1 ":=^40}')

#utilizando com uma função
def filtra(prod):
    if prod['preco'] > 50:
        return True
    else:
        return False

novo_prd = filter(filtra, produtos)

#utilizando com lambda
#novo_prd = filter(lambda p: p['preco'] > 50, produtos)

for produto in novo_prd:
    print(produto)

print('-=-'* 20)

#Utilizando MAP com dicionarios - pessoas
print(f'{" filter com dicionarios 2 ":=^40}')

nova_pes = filter(lambda p: p['idade'] >= 18, pessoas)

for pessoa in nova_pes:
    print(pessoa)

print('-=-'* 20)




