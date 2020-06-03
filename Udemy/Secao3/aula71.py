# count - Itertools

from itertools import count

contador = count(start=5, step=0.1) # conta do maior para o menor = count(start=10, step=-1) 

for valor in contador:
    print(round(valor,2))
    if valor >= 10:
        break

print('-=-' *20)
# indexar uma lista
cont = count()
lista = ['Rafael','Gama','Macedo']
lista = zip(cont,lista)
print(list(lista))



