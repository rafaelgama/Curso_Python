# Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

cores =  {'limpa':'\033[m',
            'bverde':'\033[1;32m',
            'bvermelho': '\033[1;31m',
            'pretoebranco':'\033[7:30m'}

print('-=-'*10)
print(cores['pretoebranco']+'_____INICIO_____'+cores['limpa'])
print('-=-'*10)

jogo = dict()
gols = list()
partida = list()
while True: 
    jogo['nome'] = str(input('Qual o nome do Jogador? '))
    qtd = int(input(F'Quantas Partidas {jogo["nome"]} jogou? '))
    tot = 0
    for c in range(0,qtd):
        gols.append(int(input(f'Quantos Gols na Partida {c}: ')))
        tot += gols[c]
    jogo['gols'] = gols[:] # sempre colocar o fatiamente para a cópia, senão ele faz só uma referencia !
    jogo['total'] = tot  # pode-se utilizar o sum(gols)
    gols.clear()
    partida.append(jogo.copy())
   
    
    while True:
        cont = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
        if cont in 'SN':
            break
        print('ERRO!, Responde S ou N!')
    if cont == 'N':
        break

print('-~-'*20)
print(partida)
print('-~-'*20)
print('cod ',end='' )
for k in jogo.keys():
    print(f'{k:<15}',end='')
print()
print('-~-'*20)
for k, v in enumerate(partida):
    print(f'{k:>3}', end=' ')
    for d in v.values():
        print(f' {str(d):<15}', end='')
    print()
print('-~-'*20)

while True:
    busca = int(input('Mostrar os dados de qual Jogador (999 para sair) '))
    if busca == 999:
        break
    if busca >= len(partida):
        print(f'Erro!, não existe jogador com esse codigo {busca}.')
    else:
        print(f'--LEVANTAMENTO do Jogador {partida[busca]["nome"]}:')
    print(f'O jogador {partida[busca]["nome"]} jogou {len(partida[busca]["gols"])} partidas.')
    for c, v in enumerate(partida[busca]['gols']):
        print(f' => Na Partida {c}, fez {v} gols.')
    print(f'Marcou um total de {partida[busca]["total"]} gols.')

print('')
print('-=-'*10)
print(cores['pretoebranco']+'______FIM_______'+cores['limpa'])
print(cores['pretoebranco']+'_Code by Rafael_'+cores['limpa'])
print('-=-'*10)

