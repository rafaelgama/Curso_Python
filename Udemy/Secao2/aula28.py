"""
Formatando valores com modificadores - Aula 28

:s - Texto (strings)
:d - Inteiros (int)
:f - numeros de ponto flutuante (float)
:.(numero)f - Quantidade de casas decimais (float)
:(CARACTERE)(> ou < ou ^)(QUANTIDADE)(TIPO - s, d ou f)

> - Esquerda
< - Direita
^ - Centro
"""

num_1 = 1
print(f'{num_1:0>10}')

num_2 = 1150
print(f'{num_2:0<10}')

num_2 = 1150
print(f'{num_2:.2f}')

num_2 = 1150
print(f'{num_2:0>10.2f}')

nome = 'Rafael Gama'
print(f'{nome:#^50}')
nome = nome.rjust(40,'@')
print(nome)
nome2 = 'Rafael Gama'
nome2 = nome2.center(35,'%')
print(nome2)