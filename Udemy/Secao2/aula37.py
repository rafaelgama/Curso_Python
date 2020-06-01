# Desempacotamento de listas em Python

lista = ['Luiz','João','Maria','Jose','Paulo']

n1, n2, *outra_lista, ultimo_lista = lista  # coloca um * com o restante dos valores. 

print(n2, outra_lista)