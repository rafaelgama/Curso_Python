#Crie um programa que faça o computador jogar Jokenpô com você.
from random import randint
from time import sleep
cores =  {'limpa':'\033[m',
            'bverde':'\033[1;32m',
            'roxo':'\033[35m',
            'bvermelho': '\033[1;31m',
            'pretoebranco':'\033[7:30m'}

print('-=-'*8)
print(cores['pretoebranco']+'_____INICIO_____'+cores['limpa'])
print('-=-'*8)
print('{:=^40}'.format(' JOKENPO ')) # centraliza(^) o texto no meio do caracteres de '='

print('Suas opções são: \n[ 0 ] - Pedra \n[ 1 ] - Papel \n[ 2 ] - Tesoura')

jogador = int(input('Qual a sua jogada? '))

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(1)

if jogador <= 2:
    print('-=-'*8)
    itens = ('Pedra','Papel','Tesoura')
    computer = randint(0, 2)
    print('O jogador escolheu {}'.format(itens[jogador]))
    print('O computador escolheu {}'.format(itens[computer]))
    print('-=-'*8)
    if computer == 0: #computador jogou PEDRA
        if jogador == 0:
            print('Houve um EMPATE')
        elif jogador == 1:
            print('Jogador VENCE')
        else:
            print('Computador VENCE')
    elif computer == 1: #computador jogou PAPEL
        if jogador == 0:
            print('Computador VENCE')
        elif jogador == 1:
            print('Houve um EMPATE')
        else:
            print('Jogador VENCE')
    else: #computador jogou TESOURA
        if jogador == 0:
            print('Jogador VENCE')
        elif jogador == 1:
            print('Computador VENCE')
        else:
            print('Houve um EMPATE')

else:
    print('Opção inválida!')


print('-=-'*8)
print(cores['pretoebranco']+'______FIM_______'+cores['limpa'])
print(cores['pretoebranco']+'_Code by Rafael_'+cores['limpa'])
print('-=-'*8)