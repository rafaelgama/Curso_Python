#Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

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
termo = pri
cnt = 1
while cnt <= 10:
    print('{}'.format(termo), end=' -> ')
    termo += raz
    cnt += 1
print('ACABOU')


print('-=-'*8)
print(cores['pretoebranco']+'______FIM_______'+cores['limpa'])
print(cores['pretoebranco']+'_Code by Rafael_'+cores['limpa'])
print('-=-'*8)