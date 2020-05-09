# Crie um programa que gerencie o aproveitamento de um jogador de futebol. 
# O programa vai ler o nome do jogador e quantas partidas ele jogou. 
# Depois vai ler a quantidade de gols feitos em cada partida. 
# No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

cores =  {'limpa':'\033[m',
            'bverde':'\033[1;32m',
            'bvermelho': '\033[1;31m',
            'pretoebranco':'\033[7:30m'}

print('-=-'*10)
print(cores['pretoebranco']+'_____INICIO_____'+cores['limpa'])
print('-=-'*10)

jogo = dict()
gols = list()
jogo['nome'] = str(input('Qual o nome do Jogador? '))
qtd = int(input(F'Quantas Partidas {jogo["nome"]} jogou? '))
tot = 0
for c in range(0,qtd):
    gols.append(int(input(f'Quantos Gols na Partida {c}: ')))
    tot += gols[c]
jogo['gols'] = gols[:] # sempre colocar o fatiamente para a cópia, senão ele faz só uma referencia !
jogo['total'] = tot  # pode-se utilizar o sum(gols)

print('-~-'*20)
print(jogo)
print('-~-'*20)
for k, v in jogo.items():
    print(F'O campo {k} tem o valor {v}')
print('-~-'*20)
print(f'O jogador {jogo["nome"]} jogou {len(jogo["gols"])} partidas.')

for c, v in enumerate(jogo['gols']):
    print(f' => Na Partida {c}, fez {v} gols.')
print('Foi um total de {jogo["total"]} gols.')

print('')
print('-=-'*10)
print(cores['pretoebranco']+'______FIM_______'+cores['limpa'])
print(cores['pretoebranco']+'_Code by Rafael_'+cores['limpa'])
print('-=-'*10)