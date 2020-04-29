# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato. 


cores =  {'limpa':'\033[m',
            'bverde':'\033[1;32m',
            'roxo':'\033[35m',
            'bvermelho': '\033[1;31m',
            'pretoebranco':'\033[7:30m'}

print('-=-'*8)
print(cores['pretoebranco']+'_____INICIO_____'+cores['limpa'])
print('-=-'*8) 

print('{:=^40}'.format(' LOJINHA ')) # centraliza(^) o texto no meio do caracteres de '='

totprc = prdmil = prcbrt = 0
barato = ' '
while True:
    prod = str(input('Nome do produto: '))
    preco = float(input('Preço R$: '))
    totprc += preco

    if preco >= 1000:
        prdmil += 1
    if preco < prcbrt or prcbrt == 0:
        barato = prod
        prcbrt = preco
    cont = ' '
    while cont not in 'SN':
        cont = str(input('Deseja continuar [S/N]? ')).upper().strip()[0]
    if cont == 'N':
        break
    print('-~-'*10)
print(f"{cores['bvermelho']}{'FIM das COMPRAS!':=^40}{cores['limpa']}")
print(f'O valor total das compras foram R${totprc:.2f} reais')
print(f'Temos {prdmil} produtos custando mais de R$1000.00 reais.')
print(f'O produto mais barato foi {barato} que custa R${prcbrt:.2f} reais.')

print('-=-'*8)
print(cores['pretoebranco']+'______FIM_______'+cores['limpa'])
print(cores['pretoebranco']+'_Code by Rafael_'+cores['limpa'])
print('-=-'*8)