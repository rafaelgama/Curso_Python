# Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. 
# Seu programa tem que realizar três contagens através da função criada:
# a) de 1 até 10, de 1 em 1
# b) de 10 até 0, de 2 em 2
# c) uma contagem personalizada
from time import sleep
cores =  {'limpa':'\033[m',
            'bverde':'\033[1;32m',
            'bvermelho': '\033[1;31m',
            'pretoebranco':'\033[7:30m'}

print('-=-'*10)
print(cores['pretoebranco']+'_____INICIO_____'+cores['limpa'])
print('-=-'*10)

#função contador()
def contador(ini, fim, pas):
    
    if pas < 0:
        pas *= -1
    if pas == 0:
        pas = 1
    print('-~'*20)
    print(f'Contagam de {ini} até {fim} de {pas} em {pas}')

    if ini < fim:
        cnt = ini
        while cnt <= fim:
            print(f'{cnt}', end =' ', flush=True)  #função utilizada para não fazer o Buff com a função sleep na hora de executar o print dentro de uma repetição.
            sleep(0.2)
            cnt += pas
        print('FIM!')
    else:
        cnt = ini
        while cnt >= fim:
            print(f'{cnt}', end =' ', flush=True)  #função utilizada para não fazer o Buff com a função sleep na hora de executar o print dentro de uma repetição.
            sleep(0.2)
            cnt -= pas
        print('FIM!')
    print('-~'*20)


# chamada da função contador()
contador(1,10,1)
contador(10,0,2)

print('Agora é sua vez de personalizar a contagem.')
ini = int(input('Inicio: '))
fim = int(input('Fim: '))
pas = int(input('Passo: '))

contador(ini, fim, pas)

print('-=-'*10)
print(cores['pretoebranco']+'______FIM_______'+cores['limpa'])
print(cores['pretoebranco']+'_Code by Rafael_'+cores['limpa'])
print('-=-'*10)






