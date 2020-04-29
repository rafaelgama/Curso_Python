#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
cores =  {'limpa':'\033[m',
            'azul':'\033[34m',
            'amarelo':'\033[33m',
            'vermelho': '\033[31m',
            'pretoebranco':'\033[7:30m'}

print('='*10)
print(cores['pretoebranco']+'_INICIO_'+cores['limpa'])
print('='*10)

n1 = float(input(cores['limpa']+'Primeiro Valor:'+cores['azul']+' '))
n2 = float(input(cores['limpa']+'Segundo Valor:'+cores['azul']+' '))
n3 = float(input(cores['limpa']+'Terceiro Valor:'+cores['azul']+' '))
# Verificando quem é menor
if n1<n2 and n1<n3:
    menor = n1
if n2<n1 and n2<n3:
    menor = n2
if n3<n1 and n3<n2:
    menor = n3
print(cores['limpa']+'O menor valor digitado foi {}{}{}'.format(cores['amarelo'], menor, cores['limpa']))
# Verificando quem é maior
# Eliminando um if da condição
maior = n1
if n2>n1 and n2>n3:
    maior = n2
if n3>n1 and n3>n2:
    maior = n3
print('O maior valor digitado foi {}{}{}'.format(cores['vermelho'], maior, cores['limpa']))

print('='*10)
print(cores['pretoebranco']+'___FIM___'+cores['limpa'])
print('='*10)