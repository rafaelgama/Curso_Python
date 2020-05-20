# Crie um programa que simule o funcionamento de um caixa eletrônico. 
# No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) 
# e o programa vai informar quantas cédulas de cada valor serão entregues.
# OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

cores =  {'limpa':'\033[m',
            'bverde':'\033[1;32m',
            'roxo':'\033[35m',
            'bvermelho': '\033[1;31m',
            'pretoebranco':'\033[7:30m'}

print('-=-'*8)
print(cores['pretoebranco']+'_____INICIO_____'+cores['limpa'])
print('-=-'*8) 

print('{}{:=^40}{}'.format(cores['bverde'],' CAIXA ELETRÔNICO ',cores['limpa'])) # centraliza(^) o texto no meio do caracteres de '='

valor = float(input('Qual o valor R$ que você quer sacar? '))

valaux = ced50 = ced20 = ced10 = ced01 = 0
while True:
    while (valaux + 50) <= valor:
        valaux += 50
        ced50 += 1
    
    while (valaux + 20) <= valor:
        valaux += 20
        ced20 += 1
    
    while (valaux + 10) <= valor:
        valaux += 10
        ced10 += 1
    
    while (valaux + 1) <= valor:
        valaux += 1
        ced01 += 1

    if valaux == valor:
        break
if ced50 > 0:
    print(f'Total de {ced50} cedulas de R$50 reais.')
if ced20 > 0:
    print(f'Total de {ced20} cedulas de R$20 reais.')
if ced10 > 0:
    print(f'Total de {ced10} cedulas de R$10 reais.')
if ced01 > 0:
    print(f'Total de {ced01} cedulas de R$1 real.')

print('{}{:=^40}{}'.format(cores['roxo'],' VOLTE SEMPRE ',cores['limpa']))

print('-=-'*8)
print(cores['pretoebranco']+'______FIM_______'+cores['limpa'])
print(cores['pretoebranco']+'_Code by Rafael_'+cores['limpa'])
print('-=-'*8)