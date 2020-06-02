# Dictionary Comprehension em Python - ( compreensão de dicionários)

print('-=-'* 30)
# exemplo 1
l1 = [ ('chave1','valor1'), ('chave2','valor2'), ] 
d1 = {x: y for x, y in l1}
print(d1)
print('-=-'* 30)

# exemplo 2 - Gerando SET
d1 = {x for x in range(5)}
print(d1, type(d1))
print('-=-'* 30)


# exemplo 2- Gerando DICT
d1 = {x: x**2 for x in range(5)}
print(d1, type(d1))
print('-=-'* 30)
