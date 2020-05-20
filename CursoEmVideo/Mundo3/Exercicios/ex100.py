# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). 
# A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar 
# a soma entre todos os valores pares sorteados pela função anterior.

from random import randint
from time import sleep
cores =  {'limpa':'\033[m',
            'bverde':'\033[1;32m',
            'bvermelho': '\033[1;31m',
            'pretoebranco':'\033[7:30m'}

print('-=-'*10)
print(cores['pretoebranco']+'_____INICIO_____'+cores['limpa'])
print('-=-'*10)

# função sorteia()
def sorteia(numeros):
    print('Sorteando 5 valores da lista: ', end='')    
    for c in range(0,5):
        numeros.append(randint(1,10))
        print(numeros[c], end=' ', flush=True) #função utilizada para não fazer o Buff com a função sleep na hora de executar o print dentro de uma repetição.
        sleep(0.3)
    print('PRONTO!')

# função somaPar()
def somaPar(lista):
    print(f'Somando os valores pares de {lista} é igual a: ', end='' )
    soma = 0
    for v in lista:
        if v % 2 == 0:
            soma += v
    print(soma)

# chamada das funções
numeros = list()
sorteia(numeros)
somaPar(numeros)





print()
print('-=-'*10)
print(cores['pretoebranco']+'______FIM_______'+cores['limpa'])
print(cores['pretoebranco']+'_Code by Rafael_'+cores['limpa'])
print('-=-'*10)
