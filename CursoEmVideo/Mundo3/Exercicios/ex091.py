# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python. 
# No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
from random import randint
from time import sleep
from operator import itemgetter
cores =  {'limpa':'\033[m',
            'bverde':'\033[1;32m',
            'bvermelho': '\033[1;31m',
            'pretoebranco':'\033[7:30m'}

print('-=-'*10)
print(cores['pretoebranco']+'_____INICIO_____'+cores['limpa'])
print('-=-'*10)

jogo = { 'jogador1':randint(1,6),
        'jogador2':randint(1,6),
        'jogador3':randint(1,6),
        'jogador4':randint(1,6)}
print(f'{"VALORES SORTEADOS":=^40}')
ranking = list()
for k, v in jogo.items():
    print(f'O {k} tirou {v} no dado. ')
    sleep(1)
print(f'{"RANKING DOS JOGADORES":=^40}')
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True )
for i, v in enumerate(ranking):
    print(f'O {i+1}º lugar {v[0]} com {v[1]}.')

print('')
print('-=-'*10)
print(cores['pretoebranco']+'______FIM_______'+cores['limpa'])
print(cores['pretoebranco']+'_Code by Rafael_'+cores['limpa'])
print('-=-'*10)