#Desenvolva um programa que leia o primeiro termo e a razão de uma PA. 
# No final, mostre os 10 primeiros termos dessa progressão.

cores =  {'limpa':'\033[m',
            'bverde':'\033[1;32m',
            'roxo':'\033[35m',
            'bvermelho': '\033[1;31m',
            'pretoebranco':'\033[7:30m'}

print('-=-'*8)
print(cores['pretoebranco']+'_____INICIO_____'+cores['limpa'])
print('-=-'*8) 

print('{:=^40}'.format(' PROGRESSAO ARITIMETICA ')) # centraliza(^) o texto no meio do caracteres de '='

pri = int(input('Primeiro termo: '))
raz = int(input('Razão: '))
dec = pri + (10 - 1) * raz
for c in range(pri,dec,raz):
    print('{}'.format(c), end=' -> ')
print('ACABOU')

print('-=-'*8)
print(cores['pretoebranco']+'______FIM_______'+cores['limpa'])
print(cores['pretoebranco']+'_Code by Rafael_'+cores['limpa'])
print('-=-'*8)