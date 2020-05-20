# Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. 
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

from time import sleep
cores =  {'limpa':'\033[m',
            'bverde':'\033[1;32m',
            'bvermelho': '\033[1;31m',
            'pretoebranco':'\033[7:30m'}

print('-=-'*10)
print(cores['pretoebranco']+'_____INICIO_____'+cores['limpa'])
print('-=-'*10)

#função maior()
def maior(* val):
    print('Analisando os valores passados...')
    tam = len(val) 
    maior = 0
    for v in val:
        print(f'{v} ',end='', flush=True) #função utilizada para não fazer o Buff com a função sleep na hora de executar o print dentro de uma repetição.
        sleep(0.3)
        if v > maior or maior == 0:
            maior = v
    print(f'Foram informados {tam} valores ao todo.')
    print(f'O Maior valor passado foi {maior}.')
    print('-=' * 20)

# chamada da função maior()
maior(2,9,4,5,7,1)
maior(4,7,0)
maior(1,2)
maior(6)
maior()

print()
print('-=-'*10)
print(cores['pretoebranco']+'______FIM_______'+cores['limpa'])
print(cores['pretoebranco']+'_Code by Rafael_'+cores['limpa'])
print('-=-'*10)