""" 
Tipos de Dados
str - string
int - inteiro
float - Real/Ponto flutuante
bool - booleano/lógico - True/False
"""

#comando type para descobir os Tipos
print("Rafael", type('Rafael'))
print(10, type(10))
print(25.60, type(25.60))
print(10==10, type(10==10))

# fazendo conversão
print('Luiz', type('Luiz'), bool('Luiz'))
print('10', type('10'), type(int('10')) )

# string nome
nome =str(input('Nome: '))
print(f'{nome}', type(nome))

# int idade
idade = int(input("Idade: "))
print(f'{idade}', type(idade))

# Float Altura
altura = float(input('Altura: '))
print(f'{altura} ', type(altura))

# bool É maior de idade?
print(idade > 18, type(idade > 18))