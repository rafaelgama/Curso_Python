# Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.
import time
cores =  {'limpa':'\033[m',
            'bverde':'\033[1;32m',
            'roxo':'\033[35m',
            'bvermelho': '\033[1;31m',
            'pretoebranco':'\033[7:30m'}

print('-=-'*8)
print(cores['pretoebranco']+'_____INICIO_____'+cores['limpa'])
print('-=-'*8) 

n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo Valor: '))
opc = 0 
while opc != 5:
    print('[ 1 ] somar \n[ 2 ] multiplicar \n[ 3 ] maior \n[ 4 ] novos números \n[ 5 ] sair do programa')
    opc = int(input('Qual é a sua opção? ' ))

    if opc == 1:
        result = n1+n2
        print('A soma de {} e {} é: {}.'.format(n1,n2,result))
    elif opc == 2:
        result = n1*n2
        print('A multiplicação de {} e {} é: {}.'.format(n1,n2,result))
    elif opc == 3:
        if n1>n2:
            result = n1
        else:
            result = n2
        print('A número maior de {} e {} é: {}.'.format(n1,n2,result))
    elif opc == 4:
        print(cores['bvermelho']+'Informe os números novamente:'+cores['limpa'])
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo Valor: '))
    elif opc == 5:
        print('Finalizando...')        
    else:
        print('Opção inválida! Tente novamente.')
    time.sleep(2)
print(cores['bvermelho']+'Fim do programa, Volte sempre!'+cores['limpa'])

print('-=-'*8)
print(cores['pretoebranco']+'______FIM_______'+cores['limpa'])
print(cores['pretoebranco']+'_Code by Rafael_'+cores['limpa'])
print('-=-'*8)