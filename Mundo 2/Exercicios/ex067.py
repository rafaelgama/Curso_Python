# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. 
# O programa será interrompido quando o número solicitado for negativo. 

cores =  {'limpa':'\033[m',
            'bverde':'\033[1;32m',
            'roxo':'\033[35m',
            'bvermelho': '\033[1;31m',
            'pretoebranco':'\033[7:30m'}

print('-=-'*8)
print(cores['pretoebranco']+'_____INICIO_____'+cores['limpa'])
print('-=-'*8) 
print('{:=^40}'.format(' TABUADA 3 ')) # centraliza(^) o texto no meio do caracteres de '='

num = -1
while True:
    num = int(input('Quer ver a tabuada de qual valor? '))
    if num > 0:
        res = 0
        for  c in range(1,11):
            res = num * c
            print(f' {num} X {c} = {res}')
    else:
        break
    print('-~-'*8)
print('Programa de tabuada encerrado!')


print('-=-'*8)
print(cores['pretoebranco']+'______FIM_______'+cores['limpa'])
print(cores['pretoebranco']+'_Code by Rafael_'+cores['limpa'])
print('-=-'*8)