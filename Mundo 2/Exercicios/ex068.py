# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, 
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo. 
import random
cores =  {'limpa':'\033[m',
            'bverde':'\033[1;32m',
            'roxo':'\033[35m',
            'bvermelho': '\033[1;31m',
            'pretoebranco':'\033[7:30m'}

print('-=-'*8)
print(cores['pretoebranco']+'_____INICIO_____'+cores['limpa'])
print('-=-'*8) 
print('{:=^40}'.format(' PAR ou ÍMPAR ')) # centraliza(^) o texto no meio do caracteres de '='

qtd = 0
while True:
    jogador = int(input('Digite um número de 0 a 10: '))
    comput = random.randint(0,10)
    parimp = ' '
    while parimp not in 'PI':
        parimp = str(input('Digite Par ou Ímpar [P/I]: ')).upper().strip()[0]
    soma = jogador + comput
    if soma % 2 == 0:
        print(f'Voce jogou {jogador} e o computador {comput}. Total de {soma}. Deu PAR!')
        if parimp == 'P':
            print('Você Venceu!')
            qtd += 1
        else:
            print('Você Perdeu!')
            break
    else:
        print(f'Voce jogou {jogador} e o computador {comput}. Total de {soma}. Deu ÍMPAR!')
        if parimp == 'I':
            print('Você Venceu!')
            qtd += 1
        else:
            print('Você Perdeu!')
            break
print('-^-'*8)
print(f'GAME OVER! Voce venceu {qtd} vezes.')

print('-=-'*8)
print(cores['pretoebranco']+'______FIM_______'+cores['limpa'])
print(cores['pretoebranco']+'_Code by Rafael_'+cores['limpa'])
print('-=-'*8)