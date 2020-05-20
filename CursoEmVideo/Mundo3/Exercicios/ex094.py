# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. 
# No final, mostre: 
# A) Quantas pessoas foram cadastradas
# B) A média de idade
# C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média

cores =  {'limpa':'\033[m',
            'bverde':'\033[1;32m',
            'bvermelho': '\033[1;31m',
            'pretoebranco':'\033[7:30m'}

print('-=-'*10)
print(cores['pretoebranco']+'_____INICIO_____'+cores['limpa'])
print('-=-'*10)

pessoas = dict()
galera = list()
soma = media = 0
while True:
    pessoas.clear()
    pessoas['nome'] = str(input('Nome: '))    
    while True:
        pessoas['sexo'] = str(input('Sexo: [M/F] ')).upper().strip()[0]
        if pessoas['sexo'] in 'MF':
            break
        print('ERRO! Digite M ou F.')
    pessoas['idade'] = int(input('Idade: '))
    soma += pessoas['idade'] 
    galera.append(pessoas.copy())
    cont = ' '
    while cont not in 'SN':
        cont = str(input('Deseja Continua [S/N]? ')).upper().strip()[0]
    if cont == 'N':
        break

media = soma /len(galera)
print('-~-'*20)
print(f'A) Ao todo temos {len(galera)} pessoas cadastradas. ')
print(f'B) A média de idade são {media} anos.')
print('C) As mulheres cadastradas foram', end ='')
for p in galera:
    if p['sexo'] == 'F':
        print(f' {p["nome"]}', end=' ')
print('')
print('D) Lista das pessoas acima da média de idade')
for p in galera:
    if p['idade'] >= media:
        print('  ', end='')
        for k, v in p.items():
            print(f' {k} = {v};', end=' ')
print()

print('-~-'*20)
print(galera)

print('')
print('-=-'*10)
print(cores['pretoebranco']+'______FIM_______'+cores['limpa'])
print(cores['pretoebranco']+'_Code by Rafael_'+cores['limpa'])
print('-=-'*10)