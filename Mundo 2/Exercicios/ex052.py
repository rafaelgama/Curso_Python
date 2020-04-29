#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

cores =  {'limpa':'\033[m',
            'bverde':'\033[1;32m',
            'roxo':'\033[35m',
            'bvermelho': '\033[1;31m',
            'pretoebranco':'\033[7:30m'}

print('-=-'*8)
print(cores['pretoebranco']+'_____INICIO_____'+cores['limpa'])
print('-=-'*8) 

num = int(input('Digite um número inteiro: '))
div = 0
for c in range(1, num+1):
    if num % c == 0:
        div += 1
        print('{}{}{}'.format(cores['bverde'], c,cores['limpa']), end=' ' )
    else:
        print('{}{}{}'.format(cores['roxo'], c, cores['limpa']), end=' ')
print('')
print('O número {} foi divisível por {} vezes.'.format(num,div) )
if div == 2:
    print('Portanto o Número é PRIMO')
else: 
    print('Portanto o Número NÃO é PRIMO')

print('-=-'*8)
print(cores['pretoebranco']+'______FIM_______'+cores['limpa'])
print(cores['pretoebranco']+'_Code by Rafael_'+cores['limpa'])
print('-=-'*8)