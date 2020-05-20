#Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
#- O primeiro valor é maior
#- O segundo valor é maior
#- Não existe valor maior, os dois são iguais
cores =  {'limpa':'\033[m',
            'bazulm':'\033[1;36m',
            'roxo':'\033[35m',
            'bvermelho': '\033[1;31m',
            'pretoebranco':'\033[7:30m'}

print('-=-'*8)
print(cores['pretoebranco']+'__INICIO__'+cores['limpa'])
print('-=-'*8)

val1 = int(input(cores['limpa']+'Digite o primeiro valor:'+cores['roxo']+' '))
val2 = int(input(cores['limpa']+'Digite o segundo valor:'+cores['roxo']+' '))

if val1 > val2:
    print(cores['bazulm']+'O primeiro valor é maior!'+cores['limpa'])
elif val1 < val2:
    print(cores['bazulm']+'O segundo valor é maior!'+cores['limpa'])
else:
    print(cores['bvermelho']+'Não existe valor maior, os dois são iguais!'+cores['limpa'])


print('-=-'*8)
print(cores['pretoebranco']+'___FIM___'+cores['limpa'])
print('-=-'*8)