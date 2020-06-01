# Expressões lambda (funções anônimas)


# exemplo de uma função anônima, para multiplicar dois valores
val = lambda x, y: x * y
print(val(2,3))

lista = [['P1',13], ['P2',6], ['P3',7], ['P4',50], ['P5',8]]

# modo padrão, sem o lambda
"""def func(item):
    return item[1]

lista.sort(key=func,reverse=True)
print(lista)"""

# modo alternativo com o lambda
lista.sort(key=lambda item: item[1],reverse=True)
print(lista)

# Outro exemplo de usar a ordenção
print(sorted(lista, key=lambda i: i[1],reverse=True ))