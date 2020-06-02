# list comprehension em Python. (Compreensão de lista)

print('-=-'* 30)

#Exemplo 1
l1 = [1,2,3,4,5,6,8,9]
ex1 = [variavel for variavel in l1]

print(ex1)
print('-=-'* 30)

# exemplo 2
l1 = [1,2,3,4,5,6,7,8,9]
ex2 = [v * 2 for v in l1]
print(ex2)
print('-=-'* 30)

# Exemplo 3 
l1 = [1,2,3,4,5,6,7,8,9]
ex3 = [(v,v2) for v in l1 for v2 in range(3)]
print(ex3)
print('-=-'* 30)

# Exemplo 4 
l2 = ['Rafael','Gama','Macedo']
ex4 = [v.replace('a','@') for v in l2]
print(ex4)
print('-=-'* 30)


# Exemplo 5
tupla = ( ('chave1','valor'),('chave2','valor2') )
ex5 = [(y,x) for x, y in tupla] # imprimindo invertido os valores da tupla
print(ex5)
#transforma a tupla em dicionário
ex5 = dict(ex5)
print(ex5)
print('-=-'* 30)

# exemplo 6 
l3 = list(range(100))
ex6 = [v for v in l3 if v % 2 == 0] # imprime apenas os valores pares.
print(ex6)
print('-=-'* 30)

# exemplo 7
ex7 = [v if v % 3 == 0 else 'Não é' for v in l3] # somente divisíveis por 3
print(ex7)
print('-=-'* 30)

# exemplo 7
ex8 = [v if v % 3 == 0 and v % 8 == 0 else 0 for v in l3] # somente divisíveis por 3 e 8
print(ex8)
print('-=-'* 30)