#Faça um programa que leia um número qualquer e mostre o seu fatorial.
from math import factorial
cores =  {'limpa':'\033[m',
            'bverde':'\033[1;32m',
            'roxo':'\033[35m',
            'bvermelho': '\033[1;31m',
            'pretoebranco':'\033[7:30m'}

print('-=-'*8)
print(cores['pretoebranco']+'_____INICIO_____'+cores['limpa'])
print('-=-'*8) 
            
#Utilizando o modulo que ja existe de para calcular o Fatorial
num = int(input('Digite um número para calcular o Fatorial: '))
fator = factorial(num)
print('O Fatorial (math) de {} é {}.'.format(num,fator))

#Fazendo da maneira tradicial sem o modulo e com while para calcular o Fatorial
num = int(input('Digite um número para calcular o Fatorial: '))
calc = num
fator = 1
print('Calculando o Fatorial (WHILE) de {}! = '.format(num), end='')
while calc > 0:
    print('{} '.format(calc), end='')
    print(' X ' if calc > 1 else ' = ', end='')
    fator = fator*calc
    calc -= 1
print(fator)

#Fazendo da maneira tradicial sem o modulo e com FOR para calcular o Fatorial
num = int(input('Digite um número para calcular o Fatorial: '))
fator = 1
print('Calculando o Fatorial (FOR) de {}! = '.format(num), end='')
for calc in range(num,0,-1):
    print('{} '.format(calc), end='')
    print(' X ' if calc > 1 else ' = ', end='')
    fator = fator*calc   
print(fator)


print('-=-'*8)
print(cores['pretoebranco']+'______FIM_______'+cores['limpa'])
print(cores['pretoebranco']+'_Code by Rafael_'+cores['limpa'])
print('-=-'*8)