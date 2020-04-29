#Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, 
# indo de 10 até 0, com uma pausa de 1 segundo entre eles.

from time import sleep
cores =  {'limpa':'\033[m',
            'bverde':'\033[1;32m',
            'roxo':'\033[35m',
            'bvermelho': '\033[1;31m',
            'pretoebranco':'\033[7:30m'}

print('-=-'*8)
print(cores['pretoebranco']+'_____INICIO_____'+cores['limpa'])
print('-=-'*8)            

print('{:=^40}'.format(' CONTAGEM REGRESSIVA ')) # centraliza(^) o texto no meio do caracteres de '='

for c in range(10, -1, -1):
    print(c)
    sleep(0.5)
print(cores['bvermelho']+'BOOM! BOOM! POW!'+cores['limpa'])


print('-=-'*8)
print(cores['pretoebranco']+'______FIM_______'+cores['limpa'])
print(cores['pretoebranco']+'_Code by Rafael_'+cores['limpa'])
print('-=-'*8)