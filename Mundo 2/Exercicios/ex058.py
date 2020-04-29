#Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. 
#Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
import random
cores =  {'limpa':'\033[m',
            'bverde':'\033[1;32m',
            'roxo':'\033[35m',
            'bvermelho': '\033[1;31m',
            'pretoebranco':'\033[7:30m'}

print('-=-'*8)
print(cores['pretoebranco']+'_____INICIO_____'+cores['limpa'])
print('-=-'*8) 

print('{:=^40}'.format(' Pense em um numero de 0 a 10 ')) # centraliza(^) o texto no meio do caracteres de '='

numusr = 11 # ou podia usar o varialvel = False or True
numpc = random.randint(0,10) #metodo para sortear um numero dentro do intervalo nos parametros.
count = 0
while numusr != numpc:
    numusr = int(input('Em qual número eu pensei? '))
    count += 1
    if numpc == numusr:
        print('\033[1;36;40mParabéns, você acertou!\033[m')
    elif numusr < numpc:
        print('Mais... tente de novo!')
    else:
        print('Menos... tente de novo!')
print('Acertou com {} tentativas.'.format(count))     

print('-=-'*8)
print(cores['pretoebranco']+'______FIM_______'+cores['limpa'])
print(cores['pretoebranco']+'_Code by Rafael_'+cores['limpa'])
print('-=-'*8)