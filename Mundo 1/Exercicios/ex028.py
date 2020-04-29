#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e 
# peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. 
#O programa deverá escrever na tela se o usuário venceu ou perdeu.
import random
from time import sleep
print('='*60)
print('\033[1;31;40mVou pensar em um numero de entre 0 e 5. Tente Adivinhar!\033[m')
print('='*60)
numpc = random.randint(0,5) #metodo para sortear um numero dentro do intervalo nos parametros.
numusr = int(input('Em qual número eu pensei? ')) #Jogador tenta adivinhar
print('PROCESSANDO...')
sleep(3) #função para parar a execução por 'n' segundos de acordo com o parâmetro.
if numpc == numusr:
    print('\033[1;36;40mParabéns, você acertou!\033[m')
else:
    print('\033[;31mErrou, Tente novamente!\033[m')
    print('Eu pensei no número {}'.format(numpc))

print('='*10)
print('\033[7;30m___FIM___\033[m')
print('='*10)
