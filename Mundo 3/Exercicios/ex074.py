# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. 
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
from random import randint
cores =  {'limpa':'\033[m',
            'bverde':'\033[1;32m',
            'roxo':'\033[35m',
            'bvermelho': '\033[1;31m',
            'pretoebranco':'\033[7:30m'}

print('-=-'*8)
print(cores['pretoebranco']+'_____INICIO_____'+cores['limpa'])
print('-=-'*8)

num = (randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10))

for n in num:
    print(f'{n} ', end='')
print(f'\nO maior valor sorteado foi {max(num)}.')
print(f'O menor valor sorteado foi {min(num)}.')


print('-=-'*8)
print(cores['pretoebranco']+'______FIM_______'+cores['limpa'])
print(cores['pretoebranco']+'_Code by Rafael_'+cores['limpa'])
print('-=-'*8)