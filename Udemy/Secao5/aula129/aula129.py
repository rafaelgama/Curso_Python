# Random - números aleatórios e mais.

import random
import string

# gera um número int entre os valores dos parametros
#inteiro = random.randint(10,20)

# Gerar um numero aleratório usando a função range()
inteiro = random.randrange(900, 1000, 10)

# Gera um numero float entre os valores dos parametros
#flutuante = random.uniform(10, 20)
flutuante = random.random() # outra forma de pegar um numero float de 0 a 1

print(inteiro)
print(flutuante)

print('-=-=' *20)


lista = ['Rafael', 'Gama', 'Maria', 'Rose', 'Jenny', 'Danilo', 'Felipe']
# choice = pega um valor aleatório da lista
#sorteio = random.choice(lista)
# choices = com um parametro a mais, vc define quantos valores retornam
#sorteio = random.choices(lista, k=2)
# sample = ele não repete os valores, o parametro 2 define quantos valores retornam
#sorteio = random.sample(lista,2)
# shuffle = embaralha a lista
random.shuffle(lista)

# gera senha aleatória
letras = string.ascii_letters # Retorna letras Maisculas e Minusculas
digitos = string.digits # retorna os numeros
caracteres = '!@#$%&*._-'
geral = letras + digitos + caracteres
senha = "".join(random.choices(geral, k=20))

print(senha)



