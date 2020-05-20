# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

cores =  {'limpa':'\033[m',
            'bverde':'\033[1;32m',
            'roxo':'\033[35m',
            'bvermelho': '\033[1;31m',
            'pretoebranco':'\033[7:30m'}

print('-=-'*10)
print(cores['pretoebranco']+'_____INICIO_____'+cores['limpa'])
print('-=-'*10)

pessoas = list()
dado = list()
maior = menor = 0
while True:
    dado.append(str(input('Nome: ')))
    dado.append(float(input('Peso: ')))
    pessoas.append(dado[:])

    if dado[1] > maior or maior == 0:
        maior = dado[1]
    if dado[1] < menor or menor == 0:
        menor = dado[1]

    dado.clear()
    cont = ' '
    while cont not in 'SN':
        cont = str(input('Deseja continuar [S/N]? ')).upper().strip()[0]
    if cont == 'N':
        break
print(f'Ao todo voce cadastrou {len(pessoas)} pessoas.')
print(f'O Maior peso foi {maior}Kg, das pessoas ', end=' ')
for i, v  in enumerate(pessoas): # forma de fazer com enumerate
    if v[1] == maior:
        print(f'{v[0]}...', end='')

print(f'\nO Menor peso foi {menor}Kg, das pessoas ', end=' ')
for c in range(0,len(pessoas)): # forma de fazer sem o enumerate
    if pessoas[c][1] == menor:
        print(f'{pessoas[c][0]}...', end='')
print('')
# terceira forma de fazer isso
for p in pessoas:
    if p[1] == menor:
        print(f'{p[0]} * ', end='')

print('')
print('-=-'*10)
print(cores['pretoebranco']+'______FIM_______'+cores['limpa'])
print(cores['pretoebranco']+'_Code by Rafael_'+cores['limpa'])
print('-=-'*10)