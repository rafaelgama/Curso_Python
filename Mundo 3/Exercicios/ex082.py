# Crie um programa que vai ler vários números e colocar em uma lista. 
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. 
# Ao final, mostre o conteúdo das três listas geradas.

cores =  {'limpa':'\033[m',
            'bverde':'\033[1;32m',
            'roxo':'\033[35m',
            'bvermelho': '\033[1;31m',
            'pretoebranco':'\033[7:30m'}

print('-=-'*10)
print(cores['pretoebranco']+'_____INICIO_____'+cores['limpa'])
print('-=-'*10)

lista = []
par = []
imp = []
while True:
    lista.append( int(input("Digite um número: ")) )

    if lista[-1] % 2 == 0:
        par.append(lista[-1])
    else:
        imp.append(lista[-1])

    cont = ' '
    while cont not in 'SN':
        cont = str(input('Deseja continuar [S/N]? ')).upper().strip()[0]
    if cont == 'N':
        break

print(f'A lista completa é {lista}.')
print(f'Os números pares são {par}.')
print(f'Os números ímpares são {imp}.')


print('')

print('-=-'*10)
print(cores['pretoebranco']+'______FIM_______'+cores['limpa'])
print(cores['pretoebranco']+'_Code by Rafael_'+cores['limpa'])
print('-=-'*10)