"""
Spli, Join, Enumerate em Python
* Split - Dividir uma string #str
* Join - Juntar uma lista # str
* Enumerate - Enumerar elementos da lista # iteraveis
"""


string = 'O Brasil é o país do futebol, o Brasil é penta.'
lista_1 = string.split(' ')
lista_2 = string.split(',')


# exemplo 1
#for valor in lista_1:
#    print(f'A palavra {valor} apareceu {lista_1.count(valor)}x na frase. ')

# exemplo 2
'''palavra = ' '
contagem = 0
for valor in lista_1:
    qtd_vezes = lista_1.count(valor)

    if qtd_vezes > contagem:
        contagem = qtd_vezes
        palavra = valor
print(f'A Palavra que apareceu mais vezes é a {palavra} ({contagem}x)')
'''
# Exemplo de Join
'''print(string)
print(lista_1)
string2 = ','.join(lista_1)
print(string2)
'''
# Exemplo de Enumerate
'''for indice, valor in enumerate(lista_1):
    print(indice, valor, lista_1[indice])
'''
lista = [ [3,'Luiz'], [4,'João'], [5,'Maria'] ]
for indice, nome in enumerate(lista):
    print(indice, nome)



