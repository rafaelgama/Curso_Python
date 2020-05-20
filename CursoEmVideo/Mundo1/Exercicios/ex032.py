#Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
import datetime # ou utilizar o formato: from datetime importe date
cores =  {'limpa':'\033[m',
            'azul':'\033[34m',
            'amarelo':'\033[33m',
            'vermelho': '\033[31m',
            'pretoebranco':'\033[7:30m'}

print('='*10)
print(cores['pretoebranco']+'_INICIO_'+cores['limpa'])
print('='*10)

verano = int(input('Que ano que você quer analisar? Coloque 0 para o ano atual: '))
#tratamento condicional IN LINE para o ano
ano = datetime.date.today().year if verano == 0 else verano
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano de {} é {}BISSEXTO{}'.format(ano, cores['amarelo'], cores['limpa'] ))
else:
    print('O ano de {} {}NÂO É BISSEXTO{}'.format(ano, cores['vermelho'], cores['limpa']  ))

print('='*10)
print(cores['pretoebranco']+'___FIM___'+cores['limpa'])
print('='*10)